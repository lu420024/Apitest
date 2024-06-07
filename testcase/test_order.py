import pytest


# 1.登陆 2.查找商品 3.下单 4.支付
# 按顺序执行测试用例
# 如果执行的是文件的话, 那么按照文件目录下的测试用例的顺序执行
# 在文件目录下通过添加@pytest.mark.run(order=1)可以指定测试用例运行顺序

class TestOrder:

    def test_login(self):
        print("login...")

    def test_search(self):
        print("search...")

    @pytest.mark.run(order=1)
    def test_order(self):
        print("order...")

    def test_pay(self):
        print("pay...")
