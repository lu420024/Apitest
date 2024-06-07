import pytest

@pytest.mark.pro
class TestThree:
    def test_one(self):
        one = 1
        one1 = 1
        assert one == one1

    def test_two(self):
        one = 2
        two = 2
        assert one == two

# 一种点击三角符号进行测试用例运行
# 另一种通过终端运行命令pytest 文件名

# 以test为准来运行
# def there():
#     assert 1 == 2  # 失败，函数不被运行
# pytest 可以不用导入，只要文件名带有test的前缀，pytest就会自动运行
