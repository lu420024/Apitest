import pytest

from utils.read_data import get_data

# 单参数
# @pytest.mark.parametrize("name", get_data["heroes_name"])
# def test_parametrize_02(name):
#     print(name)

# 多参数
@pytest.mark.parametrize("name,word", get_data["heroes_name_list1"])
def test_parametrize_02(name,word):
    print(name,word)