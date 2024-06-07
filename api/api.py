import json

import requests  # 导入 requests 库以进行 HTTP 请求
from core.api_util import api_util  # 从 core.api_util 模块导入 api_util 对象
from utils.log_util import logger
from utils.response_util import process_response


def mobile_query(params):
    # 调用 api_util 对象的 get_mobile_belong 方法并传入参数
    response = api_util.get_mobile_belong(params=params)
    result = process_response(response)
    return result


def tesx_json(json_data):
    response = api_util.post_data(json=json_data)
    process_response(response)
    return response.json()
