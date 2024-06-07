import os

import pytest
import requests

from api.api import mobile_query
from utils.read import base_path
url = base_path.read_ini()['host']['api_sit_url']
def test_mobile():
    param = base_path.read_data()['mobile_belong']
    result = mobile_query(param)
    assert result.success is True
    assert result.body["status"] == 0
    assert result.body["msg"] == "ok"
    assert result.body["result"]["shouji"] == "15032341111"
    assert result.body["result"]["province"] == "北京"
    assert result.body["result"]["city"] == "北京"
    assert result.body["result"]["company"] == "中国移动"
    assert result.body["result"]["areacode"] == "0571"


# 运行测试用例，‘文件名.py’
if __name__ == '__main__':
    pytest.main()
