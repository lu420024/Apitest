import allure
import pytest

from api.goods_api import get_banner
from core.ApiService import ApiService
from testcases.goodscenter.conftest import banner_num
from utils.YamlUtil import YamlUtils


@allure.feature('用户运营模块')
class TestGoods:
    @allure.story('首页')
    @allure.title('Banner')
    def test_banner(self,banner_num):
        # num = banner_num()
        result = get_banner()
        assert result.success is True
        assert len(result.body) == banner_num

    @pytest.mark.parametrize("data", YamlUtils().extract_case('good_center.yaml', 'get_banner'))
    def test_banner_new(self, data):
        ApiService().handle_case(data)

