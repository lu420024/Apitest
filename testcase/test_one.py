import pytest


@pytest.mark.p0
def test_one():
    one = 2
    one1 = 1
    assert one == one1


@pytest.mark.test
def test_two():
    one = 2
    two = 2
    assert one == two

# 一种点击三角符号进行测试用例运行
# 另一种通过终端运行命令pytest 文件名

# 以test为准来运行
# def there():
#     assert 1 == 2  # 失败，函数不被运行
# pytest 可以不用导入，只要文件名带有test的前缀，pytest就会自动运行

'''
ini配置里有执行路径，通过pytest -k 执行关键字查询，当关键字符合文件名时，
将执行该文件里的测试用例，如果文件名没有关键字，将查询测试用例方法名称。例如：
class 或者def
'''

