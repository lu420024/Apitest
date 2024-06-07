import requests

url = "https://movie.douban.com/j/search_subjects"

param = {
    "type": "movie",
    "tag": "热门",    #%E7%83%AD%E9%97%A8 使用url解码便可以知道内容了
    "page_limit": 50,
    "page_start": 0
}

headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                 "Chrome/125.0.0.0 Safari/537.36"
}

r = requests.get(url=url, params=param, headers=headers)    #加入请求头参数就不会返回418错误了
print(r.status_code)
print(r.json())
