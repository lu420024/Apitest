import requests


class TestUser:
    token1 = ""
    username1 = ""
    def test_login(self):
        username = "laobai"
        password = "123456"
        # res = requests.post("/login",json={"username":username, "password":password})
        token = "token"
        assert token == "token"
        # return token, username
        TestUser.token1 = token
        TestUser.username1 = username
    # 使用前一口接口传回来的参数来进行验证
    def test_userinfo(self):
        #token, username = self.test_login()
        headers = {
            "taken": TestUser.token1
        }
        # res = requests.post("/get_user", headers=headers)
        # assert headers['taken'] == token
        assert headers['taken'] == TestUser.token1
        #assert username == "laobai22"
        assert TestUser.username1 == "laobai"
