import requests
# from requests.cookies import RequestsCookieJar
#
# url = 'http://210.38.250.43/login!doLogin.action'
#
# import json
#
# cookie_jar = RequestsCookieJar()
#
data = {'account' :'17034480137' , 'pwd': '159874xzh', 'verifycode': ''}

r = requests.post('http://210.38.250.43/login!doLogin.action', data=data)
cookies = r.cookies.get_dict()
e = requests.post('http://210.38.250.43/login!doLogin.action', data=data,cookies=cookies)

x = requests.get('http://210.38.250.43/xjkpxx!xjkpList.action', cookies=cookies)
print(x.text)


# e = requests.get()
# print(r.text)
#
# url = 'http://210.38.250.43/login!doLogin.action'
# res = requests.post('http://210.38.250.43/login!doLogin.action')
# print(res.cookies)