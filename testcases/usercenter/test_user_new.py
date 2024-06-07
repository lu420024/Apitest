import allure
import pytest

from core.ApiService import ApiService
from utils.YamlUtil import YamlUtils


@allure.feature('用户中心模块')
class TestUser:
    @pytest.mark.parametrize("data", YamlUtils().extract_case('user_canter.yaml', 'user_long_new'))
    def test_user_new(self, data):
        ApiService().handle_case(data)
