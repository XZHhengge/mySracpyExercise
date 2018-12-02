# -*- coding: utf-8 -*-
import pymysql
from urllib import request
import re
req = request.Request('http://www.xicidaili.com/')
req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1')
db = pymysql.connect("localhost", "数据库用户名", "密码", "数据库名")
cursor = db.cursor()
with request.urlopen(req) as f:
    readText = f.read().decode('utf-8')
    #正则表达式
    compileModels =('''
    <td>(.*?)</td>
    <td>(.*?)</td>
    <td>(.*?)</td>
    <td class="country">(.*?)</td>
    <td>(.*?)</td>''')
    pattern = re.compile(compileModels)
    compileText = pattern.findall(readText)
    for i in compileText:
        print(list(i))
        sql = """INSERT INTO xicidaili(代理IP地址,
                  端口, 服务器地址, 是否匿名, 类型)
                  VALUES (%s,%s,%s,%s,%s)"""
        cursor.execute(sql,(i))
        db.commit()
db.close()