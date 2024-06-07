import pytest


# @pytest.fixture(scope="session", autouse=True)  # 如果不加上autouse=True，则需要每一个测试文件里加入test_session()
# def test_session():
#     print("我是session级别的fixture")


# 使用终端运行
# 使用session级别的时候，文件名要为conftest.py
# conftest.py当前目录及其所有子目录中的测试中可用。

'''
function（默认）：每个测试函数调用前后运行一次。
class：每个测试类的所有测试方法调用前后运行一次。
module：每个测试模块的所有测试函数调用前后运行一次。
session：整个测试会话的所有测试模块调用前后运行一次。
和传的参数顺序没有关系，执行时按照作用域来，fixture作用域：session>module>class>function
'''


@pytest.fixture(scope="function")
def test_func():
    print("这是function级别的方法")


@pytest.fixture(scope="function")
def test_func1():
    print("这是function1级别的方法")


@pytest.fixture(scope="function")
def get_params():
    param = {
        "shouji": "15032341111",
        "appkey": "0c818521d38759e1"
    }
    return param


@pytest.fixture(scope="function")
def func2():
    print("这是func2的前置步骤")
    yield  # 也可以返回数据，但一般不用
    print("这是func2的后置步骤")


@pytest.fixture(scope="function")
def use_fixture1():
    print("我现在使用use——fixtures1")
    return "fixture"

@pytest.fixture(scope="function")
def use_fixture2():
    print("我现在使用use——fixtures2")