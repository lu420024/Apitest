import pytest


# 多个值插入同一个参数里
@pytest.mark.parametrize(["name", "word"], [["张三", "你好"], ["李四", "你好"], ["王五", "你好"]])
def test_parametrize_02(name, word):
    print("你所选择的英雄：{}，它的英雄台词是{}".format(name, word))


# 多个值插入同一个参数里 元组形式
@pytest.mark.parametrize(["name", "word"], [("张三", "你好"), ("李四", "你好"), ("王五", "你好")])
def test_parametrize_02(name, word):
    print("你所选择的英雄：{}，它的英雄台词是{}".format(name, word))


# 下面这种print打印的结果是不正确的，如果要打印正确的结果，需要将参数列表中的元素用元组包裹起来
@pytest.mark.parametrize(["name", "word"], ["张三", "你好"])
def test_parametrize_02(name, word):
    print("你所选择的英雄：{}，它的英雄台词是{}".format(name, word))


# 正确的
@pytest.mark.parametrize(["name", "word"], [("张三", "你好")])
def test_parametrize_02(name, word):
    print("你所选择的英雄：{}，它的英雄台词是{}".format(name, word))


# 字典形式,字典的key值为参数名
@pytest.mark.parametrize("hero", [{"name":"张三","word":"你好"},{"name":"李四"},{"name":"王五"}])
def test_parametrize_02(hero):
    print(hero["name"])
    print(hero["word"])     # 其他两个字典参数没有word键值，所以会报错
