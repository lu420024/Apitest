import pytest
import requests


# fixture function 每一个函数和方法都会被调用


# @pytest.fixture(scope="function", autouse=True)  # 不填默认为function
# # @pytest.fixture(autouse=True)的情况下所有方法都默认使用。不需要传参数
# # @pytest.fixture(scope="function") 默认scope是function
# def func():
#     print("我是前置步骤~")


def test_mobile():
    # 手机归属地查询接口.get请求
    print("手机归属地查询接口.get请求")
    param = {
        "shouji": "15032341111",
        "appkey": "0c818521d38759e1"
    }
    r = requests.get("http://sellshop.5istudy.online/sell/shouji/query", params=param)  # 插入params参数 在postman中
    print(r.status_code)
    assert r.status_code == 200
    result = r.json()
    assert result["status"] == 0
    assert result["msg"] == "ok"
    assert result["result"]["shouji"] == "15032341111"
    assert result["result"]["province"] == "北京"
    assert result["result"]["city"] == "北京"
    # assert result["result"]["city"] == "上海"
    assert result["result"]["company"] == "中国移动"
    assert result["result"]["areacode"] == "0571"
    # 如果返回的参数是null的情况下，可以用is None来判断
    # assert result["result"]["postconsonantal"] is None


def test_mobile_post():
    # 手机归属地查询接口.post请求
    print("手机归属地查询接口.post请求")
    param = {
        "shouji": "15032341111",
        "appkey": "0c818521d38759e1"
    }
    r = requests.post("http://sellshop.5istudy.online/sell/shouji/query", params=param)  # post请求
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
