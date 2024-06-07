import requests

r = requests.get('https://api.github.com/events')
print(r.status_code)    # 接口状态码
print(r.json())         # 接口返回的json
print(r.text)           # 接口返回的文本