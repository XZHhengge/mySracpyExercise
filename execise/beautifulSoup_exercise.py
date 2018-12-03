# -*- coding: utf-8 -*-
html = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
        <p class="story">...</p>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
# 返回节点列表
print(soup.p.contents)

#返回子节点迭代器
for i, child in enumerate(soup.p.children):
    print(i, child)

#返回子孙节点迭代器
for i, child in enumerate(soup.p.descendants):
    print(i, child)

#返回父节点
print(soup.a.parent)

#返回祖先节点
print(soup.a.parents)

#返回兄弟节点
print(list(enumerate(soup.a.next_siblings)))
print(list(enumerate(soup.a.previous_siblings)))

#find_all( name , attrs , recursive , text , **kwargs )的用法

# attrs

html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1" name="elements">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')

#两种用法相同
print(soup.find_all(attrs={'id': 'list-1'}))
print(soup.find_all(attrs={'name': 'elements'}))

print(soup.find_all(id='list-1'))
print(soup.find_all(class_='element'))

#直接匹配文字
print(soup.find_all(text='Foo'))


#css选择器
html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
print(soup.select('.panel .panel-heading')) #class选择 用.开头，
print(soup.select('ul li'))  #直接选择标签
print(soup.select('#list-2 .element')) #ID选择 用#开头

#获取属性
for ul in soup.select('ul'):
    print(ul['id'])
    print(ul.attrs['id'])

# 获取内容
for li in soup.select('li'):
    print(li.get_text())

'''总结
推荐使用lxml解析库，必要时使用html.parser
标签选择筛选功能弱但是速度快
建议使用find()、find_all() 查询匹配单个结果或者多个结果
如果对CSS选择器熟悉建议使用select()
记住常用的获取属性和文本值的方法'''