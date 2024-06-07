import pytest


@pytest.mark.usefixtures("use_fixture1")
@pytest.mark.usefixtures("use_fixture2")
# 离测试方法距离近的先运行，这里会先运行2然后是1
# @pytest.mark.usefixtures("use_fixture1", "use_fixture2") 顺序执行
# usefixtures 没有办法接收返回值
def test_usefixture():
    print("usefixtures")