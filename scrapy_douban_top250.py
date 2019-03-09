# -*- coding:utf-8 -*-
import json
import re
from time import time
import multiprocessing
import requests
from requests.exceptions import RequestException


def get_one_page(url):
    try:
        response = requests.get(url)
        if response.status_code ==200:
            return response.text
        return response
    except RequestException as e:
        return e


def parse_opne_page(html):
    # 匹配顺序 排名,图片地址,电影名称,
    pattern = re.compile('<li>.*?class.*?>(\d*)</em>.*?src="(.*?)".*?title">(.*?)</span>.*?<p class.*?>'
                         '(.*?)<br>(.*?)</p>.*?average">(.*?)</span>.*?'
                         '<span>(.*?)</span>.*?<span class.*?>(.*?)</span>.*?</li>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            '排名': item[0],
            '图片地址': item[1],
            '电影名字': item[2],
            '导演，主演': item[3].strip()[3:].replace('&nbsp;','').replace('...', ''),
            '上映时间，地区，类型': item[4].strip().replace('&nbsp;/&nbsp',''),
            '评分': item[5],
            '点评人数': item[6],
            '简介': item[7],
        }

def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False)+ '\n')
        f.close()

def main(start):
    url = 'https://movie.douban.com/top250?start={}&filter='.format(start)
    html = get_one_page(url)
    for item in parse_opne_page(html):
        print(item)
        write_to_file(item)

if __name__ == '__main__':
    startTime = time()
    # for i in range(10):
    #     main(i*25)
    # pool = multiprocessing.Pool(multiprocessing.cpu_count())
    # for i in range(10):
    #     pool.apply_async(main, (i*25,))
    # pool.close()
    # pool.join()
    # 第二种多线程写法
    pool = multiprocessing.Pool()
    pool.map(main, [i*25 for i in range(10)])
    endTime = time()

    print('Done, Time cost:{}'.format(endTime-startTime))
