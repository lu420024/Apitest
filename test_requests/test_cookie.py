import requests

# 使用Session对象会自带cookie，不需要自己维护cookie
# req = requests.Session()
# url = "http://sellshop.5istudy.online/sell/user/login"
#
# data = {
#     "username": "test01",
#     "password": "123456"
# }
#
# res = req.post(url=url, data=data)
# #print(res.text)
#
# url2 = "http://sellshop.5istudy.online/sell/seller/order/list?page=2&size=10" #带有cookie的请求到第二页
# res2 = req.get(url2)
# print(res2.text)

url = "http://sellshop.5istudy.online/sell/seller/order/list"
headers = {
    "Cookie": "token=9af6ff75-0cab-4590-83ea-6c99fd076066"
}  # 带有cookie的请求

res = requests.get(url=url, headers=headers)
print(res.text)
