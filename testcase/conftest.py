# import pytest


# @pytest.fixture(scope="session", autouse=True)  # 如果不加上autouse=True，则需要每一个测试文件里加入test_session()
# def test_session():
#     print("我是session级别的fixture")


# 使用终端运行
# 使用session级别的时候，文件名要为conftest.py
# conftest.py只在当前文件夹有效

'''
function（默认）：每个测试函数调用前后运行一次。
class：每个测试类的所有测试方法调用前后运行一次。
module：每个测试模块的所有测试函数调用前后运行一次。
session：整个测试会话的所有测试模块调用前后运行一次。
'''


# @pytest.fixture(scope="function")
# def test_func():
#     print("这是function级别的方法")
#
# @pytest.fixture(scope="function")
# def test_func1():
#     print("这是function1级别的方法")


import pytest

from utils.log_util import logger


@pytest.fixture(scope='function', autouse=True)
def func():
    logger.info('开始执行测试用例')
    yield
    logger.info('测试用例执行完毕')
