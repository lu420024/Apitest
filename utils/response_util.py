import json

from core.ResultBase import ResultResponse
from utils.log_util import logger


def process_response(response):
    if response.status_code == 200 or response.status_code == 201:
        ResultResponse.success = True
        response.json()
        ResultResponse.body = response.json()
    else:
        ResultResponse.success = False
        logger.info('接口的返回码不是200或者201，检查错误')
    logger.info('接口返回的内容>>>\n' + json.dumps(response.json(), ensure_ascii=False))
    return ResultResponse()

