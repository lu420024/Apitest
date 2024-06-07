import pytest
import requests

# # 通过session来保持登陆状态
# token = requests.Session()
# url = "http://sellshop.5istudy.online/sell/user/login"
#
# data = {
#     "username": "test01",
#     "password": "123456"
# }
#
# res = requests.post(url, data=data)
#
# url2 = "http://sellshop.5istudy.online/sell/seller/order/list?page=2&size=10"
# res1 = token.get(url2)
# print(res.status_code)
# print(res.text)

# 通过headers来保持登陆
# url = "http://sellshop.5istudy.online/sell/seller/order/list"
#
# headers = {
#     "Cookie": "token=6c75a7b4-025a-4013-b8fe-ccafab0670db"
# }
#
# res = requests.get(url, headers=headers)
# print(res.status_code)
# print(res.text)

# 豆瓣电影接口返回
# url = "https://movie.douban.com/j/search_subjects"
#
# data = {
#     "type": "tv",
#     "tag": "热门",
#     "page_limit": 50,
#     "page_start": 0
# }
#
# headers = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
#                   "Chrome/125.0.0.0 Safari/537.36"
# }
#
# res = requests.get(url, params=data, headers=headers)
# print(res.status_code)
# print(res.json())

# get请求接口
# res = "https://api.github.com/events"
# ress = requests.get(res)
# print(ress.status_code)
# print(ress.json())

# # json请求接口
# url = "https://jsonplaceholder.typicode.com/posts"
#
# data = {
#     "title": "foo",
#     "body": "bar",
#     "userID": "1",
# }
#
# r = requests.post(url, json=data)
# print(r.status_code)
# print(r.json())
#
# # json请求之数据表
# url = "https://dict.youdao.com/keyword/key"
#
# data = {
#     "text":"你好"
# }
#
# re = requests.post(url, data=data)
# print(re.status_code)
# print(re.json())

# 手机归属地查询
# params = {
#     "shouji":"15032341111",
#     "appkey":"0c818521d38759e1"
# }
#
# url = "http://sellshop.5istudy.online/sell/shouji/query"
# 
# r = requests.post(url,params=params)
# print(r.status_code)
# print(r.json())

