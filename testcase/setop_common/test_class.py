import pytest
import requests


# setup_class和teardown_class只在类中前后运行一次（在类中）

class TestClass:

    def setup_class(self):
        print("准备测试数据")

    def teardown_class(self):
        print("清理测试数据")

    def test_mobile(self):
        # 手机归属地查询接口.get请求
        print("手机归属地查询接口.get请求")
        param = {
            "shouji": "15032341111",
            "appkey": "0c818521d38759e1"
        }
        r = requests.get("http://sellshop.5istudy.online/sell/shouji/query", params=param)  # 插入params参数 在postman中
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

    def test_mobile_post(self):
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
