# -*- coding:utf-8 -*-
# Author: cmzz
# @Time :2019/4/27
from selenium import webdriver
from bs4 import BeautifulSoup
# 抓取豆瓣长评论
# ***selenium 自动操作网页***
options = webdriver.ChromeOptions()
options.add_argument('user-agent="Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                     'Chrome/27.0.1453.94 Safari/537.36"')  # 设置设备代理
driver = webdriver.Chrome(chrome_options=options)

driver.get('https://movie.douban.com/subject/1292052/')

ahref = driver.find_element_by_id('toggle-1000369-copy')
ahref.click()
html = driver.page_source
content = BeautifulSoup(html, 'lxml')
title = content.find_all(class_='review-content clearfix')
content2 = BeautifulSoup(str(title), 'lxml')
print(content2)