# -*- coding:utf-8 -*-
# Author: cmzz
# @Time :2019/4/21
import re
import urllib.robotparser as robotparser
import collections
from urllib.parse import urlparse, urljoin
import requests
import time
from datetime import datetime


def link_crawler(seed_url, link_regex=None, delay=5, max_depth=-1, max_urls=-1, headers=None, user_agent='wswp',
                 proxy=None, num_retries=1):
    """Crawl from the given seed URL following links matched by link_regex
    """
    # the queue of URL's that still need to be crawled
    crawl_queue = collections.deque([seed_url])
    # the URL's that have been seen and at what depth
    seen = {seed_url: 0}
    # track how many URL's have been downloaded
    global num_urls
    num_urls = 0
    rp = get_robots(seed_url)
    throttle = Throttle(delay)
    headers = headers or {}
    if user_agent:
        headers['User-agent'] = user_agent

    while crawl_queue:
        url = crawl_queue.pop()
        # check url passes robots.txt restrictions
        if rp.can_fetch(user_agent, url):
            throttle.wait(url)
            html = download(url, headers, proxy=proxy, num_retries=num_retries)
            links = []

            depth = seen[url]
            if depth != max_depth:
                # can still crawl further
                if link_regex:
                    # filter for links matching our regular expression

                    links.extend(link for link in get_links(url, html))
                    # links.extend(link for link in get_links(html) if re.match(link_regex, link))

                for link in links:
                    link = normalize(seed_url, link)
                    # check whether already crawled this link
                    if link not in seen:
                        seen[link] = depth + 1
                        # check link is within same domain
                        # if same_domain(seed_url, link):

                            # success! add this new link to queue
                        crawl_queue.append(link)

            # check whether have reached downloaded maximum
            num_urls += 1
            if num_urls == max_urls:
                break
        else:
            print('Blocked by robots.txt:', url)
    return num_urls


class Throttle:
    """Throttle downloading by sleeping between requests to same domain
    """

    def __init__(self, delay):
        # amount of delay between downloads for each domain
        self.delay = delay
        # timestamp of when a domain was last accessed
        self.domains = {}

    def wait(self, url):
        domain = urlparse(url).netloc
        last_accessed = self.domains.get(domain)

        if self.delay > 0 and last_accessed is not None:
            sleep_secs = self.delay - (datetime.now() - last_accessed).seconds
            if sleep_secs > 0:
                time.sleep(sleep_secs)
        self.domains[domain] = datetime.now()


def download(url, headers, proxy, num_retries, data=None):
    print('Get', url)
    try:
        response = requests.get(url, data, headers=headers, proxies=proxy, timeout=2)
        html = response.text
        code = response.status_code
    except Exception as e:
        print('Download error:', e)
        print('error link', url)
        html = ''
        if hasattr(e, 'code'):
            code = response.status_code
            if num_retries > 0 and 500 <= code < 600:
                # retry 5XX HTTP errors
                return download(url, headers, proxy, num_retries - 1, data)
        else:
            code = None
    return html


def normalize(seed_url, link):
    """Normalize this URL by removing hash and adding domain
    """
    # link, _ = urlparse(link) # remove hash to avoid duplicates

    spilt = urlparse(link)
    # print('spilt.netloc',spilt.netloc)
    if spilt.netloc == '':
        return urljoin(seed_url, link)
    else:
        return link


def same_domain(url1, url2):
    """返回相同服务器域名的链接
    """
    return urlparse(url1).netloc == urlparse(url2).netloc


def get_robots(url):
    """Initialize robots parser for this domain
    """
    rp = robotparser.RobotFileParser()
    rp.set_url(urljoin(url, '/robots.txt'))
    rp.read()
    return rp


def get_links(url, html):
    """返回当前页面的全部链接
    """
    # a regular expression to extract all links from the webpage
    regex_links = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE).findall(html)
    clear_links = list(set(regex_links))  # 一个页面上去除重复链接
    link = []
    for i in clear_links:
        reslut = urlparse(i)
        if reslut.netloc == '':
            link.append(urljoin(url, i))
        else:
            link.append(i)  # 加入补充后的链接
    return link


if __name__ == '__main__':
    # delay 为睡眠时间, num_retries为重试次数, max_depth为深度, user-agent为代理
    num = link_crawler('http://www.gdupt.edu.cn/', '.*?', delay=0, num_retries=1, max_depth=2, user_agent='Mozilla/4.0')
    print(num)
