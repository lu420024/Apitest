import logging
import pytest  # 导入 pytest 以便执行测试
from utils.log_util import logger  # 从自定义日志工具中导入 logger 对象

from api.api import tesx_json  # 从 api.api 模块导入 tesx_json 方法
from utils.read import base_path  # 从 utils.read 模块导入 base_path 对象


def test_post():

    json_data = base_path.read_data()['json_data']
    result = tesx_json(json_data)
    assert result['id'] == 101



if __name__ == '__main__':
    pytest.main()  # 如果此文件作为主程序运行，则执行 pytest.main() 以运行测试
