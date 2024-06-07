import pytest


# 单参数单次插入数据

@pytest.mark.parametrize("name", ["牛"])
def test_parametrize1(name):
    print("我的生肖年是" + name)

# 单参数多次插入数据 也叫循环数据
# 运行时分别把数组里的值依次传给name，每传递一次运行一次
@pytest.mark.parametrize("name", ["牛", "虎", "鸡"])
def test_parametrize2(name):
    print("我的生肖年是" + name)
    assert name == "牛"
