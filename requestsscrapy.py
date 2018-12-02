import requests
from bs4 import BeautifulSoup
'''使用requests和BeautifulSoup爬去广东石油化工学院的个人信息与课表'''


def get_info(info):
    account = info[0]
    pwd = info[1]
    week = info[2]
    term = info[3]
    if term == None:
        term = 201801
    else:
        pass
    data = {'account': account, 'pwd': pwd, 'verifycode': ''}
    try:

        r = requests.post('http://210.38.250.43/login!doLogin.action', data=data)
        cookies = r.cookies.get_dict()
        requests.post('http://210.38.250.43/login!doLogin.action', data=data,cookies=cookies)
        person_info = requests.get('http://210.38.250.43/xjkpxx!xjkpList.action',cookies=cookies)
        soup = BeautifulSoup(person_info.text, "lxml")
        info = soup.select("label")
        print('-----------------------------学籍信息--------------------------------')
        print()
        for i in info:
            print(i.parent.previous_element.previous_element + i.getText())
        x = requests.get('http://210.38.250.43/xsgrkbcx!getKbRq.action?xnxqdm={}&zc={}'.format(term, week), cookies=cookies)
        text = x.json()
        text = text[0]
        text1 = [text[i]['kcmc'] for i in range(len(text))]  #课名
        text2 = [text[i]['teaxms'] for i in range(len(text))] #老师
        text3 = [text[i]['jxbmc'] for i in range(len(text))] #班别
        text4 = [text[i]['jcdm2'] for i in range(len(text))]#课室
        text5 = [text[i]['xq'] for i in range(len(text))]#星期
        text6 = [text[i]['jxcdmc'] for i in range(len(text))]#课室
        text7 = [text[i]['sknrjj'] for i in range(len(text))]#内容

        ziplist = zip(text1, text2, text3, text4, text5, text6, text7)
        # txt = ['上课老师', '班别', '节时', '星期', '课室', '内容', '']
        for a, b, c, d, e, f, g in ziplist:
            print('---------------------第{}学期,第{}周的课表------------------------------'.format(term, week))
            print('---------------------------------------------------------------------')
            print({'星期':e, '节课':d, '课名':a,  '课室':f, '上课老师':b, '班别':c,'内容':g})
    except:
        print('----------------------------输入有误-------------------------------')

if __name__ == '__main__':
    info = []
    info.append(input('请输入你的学号:'))
    info.append(input('请输入你的密码：'))
    info.append(input('你需要第几周的课表：'))
    info.append(input('需要查询的学期（默认为本学期）格式:(201801)代表18年第一个学期:'))
    get_info(info)
