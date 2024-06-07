import pytest
import requests

# phone = "13000000000"
#
#
# # 手机归属地请求
# @pytest.mark.skip()
# def test_get_phone():
#     print("这是get请求")
#     url = "http://sellshop.5istudy.online/sell/shouji/query"
#
#     data = {
#         "shouji": "15032341111",
#         "appkey": "0c818521d38759e1"
#     }
#
#     response = requests.get(url, params=data)
#     assert response.status_code == 200
#     responses = response.json()
#
#     assert responses["status"] == 0
#     assert responses["msg"] == "ok"
#
#     assert responses["result"]["shouji"] == "15032341111"
#     assert responses["result"]["province"] == "北京"
#     assert responses["result"]["city"] == "北京"
#     assert responses["result"]["company"] == "中国移动"
#     assert responses["result"]["areacode"] == "0571"
#
#
# @pytest.mark.skipif("len(phone)==10")
# def test_post_phone():
#     print("这是post请求")
#     url = "http://sellshop.5istudy.online/sell/shouji/query"
#
#     data = {
#         "shouji": "15032341111",
#         "appkey": "0c818521d38759e1"
#     }
#
#     response = requests.post(url, params=data)
#     assert response.status_code == 200
#     responses = response.json()
#
#     assert responses["status"] == 0
#     assert responses["msg"] == "ok"
#
#     assert responses["result"]["shouji"] == "15032341111"
#     assert responses["result"]["province"] == "北京"
#     assert responses["result"]["city"] == "北京"
#     assert responses["result"]["company"] == "中国移动"
#     assert responses["result"]["areacode"] == "0571"
#
#
# if __name__ == "__main__":
#     pytest.main()

# 通过给测试用例打标签，在终端执行标签测试用例
# @pytest.mark.p1
# def test_one():
#     one = 1
#     two = 2
#     assert one == two
#
#
# @pytest.mark.test1
# def test_two1111():
#     one = 1
#     one1 = 2
#     assert one == one1

# 通过return的参数来进行验证
# import requests
#
# class TestUser:
#     token = ""
#     username = ""
#
#     def test_login(self):
#         username = "laobai"
#         password = "123456"
#         response = requests.post("/login", json={"username": username, "password": password})
#         assert response.status_code == 200
#         data = response.json()
#         TestUser.token = data.get("token")
#         TestUser.username = username
#
#     def test_userinfo(self):
#         self.test_login()  # 先登录获取 token
#         headers = {
#             "token": TestUser.token  # 正确的键名应该是 "token"
#         }
#         response = requests.post("/get_user", headers=headers)
#         assert response.status_code == 200
#         data = response.json()
#         assert data.get("username") == TestUser.username



