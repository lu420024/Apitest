import requests

# 手机归属地查询接口
param = {
    "shouji":"15032341111",
    "appkey":"0c818521d38759e1"
}
r = requests.post("http://sellshop.5istudy.online/sell/shouji/query", params=param) #post请求
print(r.status_code)
print(r.json())