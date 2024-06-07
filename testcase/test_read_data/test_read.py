import os

import pytest
import requests

from utils.read import base_path

def test_mobile():
    # 手机归属地查询接口.get请求
    param = base_path.read_data()['mobile_belong']
    url = base_path.read_ini()['host']['api_sit_url']
    print("手机归属地查询接口.get请求")

    r = requests.get(url + 'sell/shouji/query', params={
        "shouji": param['shouji'],
        "appkey": param['appkey']
    })  # 插入params参数 在postman中
    print(r.status_code)
    assert r.status_code == 200
    result = r.json()
    assert result["status"] == 0
    assert result["msg"] == "ok"
    assert result["result"]["shouji"] == "15032341111"
    assert result["result"]["province"] == "北京"
    assert result["result"]["city"] == "北京"
    assert result["result"]["company"] == "中国移动"
    assert result["result"]["areacode"] == "0571"


# 运行测试用例，‘文件名.py’
if __name__ == '__main__':
    pytest.main()
