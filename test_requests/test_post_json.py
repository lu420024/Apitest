import requests

json_data = {
    "title": "foo",
    "body": "bar",
    "userID": "1",
}

r = requests.post("https://jsonplaceholder.typicode.com/posts",json=json_data) #使用body里的raw Json数据
print(r.status_code)
print(r.json())

datas = {
    "text":"hello world"
}

d = requests.post("https://dict.youdao.com/keyword/key", data=datas)  #使用form-data数据
print(d.status_code)
print(d.json())