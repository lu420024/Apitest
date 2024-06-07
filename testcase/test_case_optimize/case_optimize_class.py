import os

import allure
import pytest
import requests

from api.api import mobile_query
from utils.read import base_path

url = base_path.read_ini()['host']['api_sit_url']


@allure.epic('数据进制项目epic')
@allure.feature('手机号模块feature')
class TestMobile:
    # @allure.story('杭州手机号story1')
    # @allure.title('测试手机号归属地title')
    @allure.testcase('http://www.baidu.com')
    @allure.issue('http://www.hao123.com')
    @allure.description('当前手机号是13444223123，归属地是杭州的description')
    @allure.step('先进性归属地的操作step')
    @allure.link('https://mdnf.qq.com/main.shtml', name='dnf手游')
    @allure.severity(severity_level='critical')
    def test_mobile1(self):
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

    @allure.story('杭州手机号story2')
    @allure.title('测试手机号归属地title')
    @allure.testcase('http://www.baidu.com')
    @allure.issue('http://www.hao123.com')
    @allure.description('当前手机号是13444223123，归属地是杭州的description')
    @allure.step('先进性归属地的操作step')
    @allure.severity(severity_level='blocker')
    @pytest.mark.skip(reason='跳过测试用例')
    def test_mobile2(self):
        param = base_path.read_data()['mobile_belong']
        result = mobile_query(param)
        assert result.success is True
        assert result.body["status"] == 0
        assert result.body["msg"] == "no"
        assert result.body["result"]["shouji"] == "15032341111"
        assert result.body["result"]["province"] == "北京"
        assert result.body["result"]["city"] == "北京"
        assert result.body["result"]["company"] == "中国移动"
        assert result.body["result"]["areacode"] == "0571"

    @allure.story('杭州手机号story3')
    @allure.title('测试手机号归属地title')
    @allure.testcase('http://www.baidu.com')
    @allure.issue('http://www.hao123.com')
    @allure.description('当前手机号是13444223123，归属地是杭州的description')
    @allure.step('先进性归属地的操作step')
    @allure.severity(severity_level='blocker')
    def test_mobile3(self):
        param = base_path.read_data()['mobile_belong']
        result = mobile_query1(param)
        assert result.success is True
        assert result.body["status"] == 0
        assert result.body["msg"] == "ok"
        assert result.body["result"]["shouji"] == "15032341111"
        assert result.body["result"]["province"] == "北京"
        assert result.body["result"]["city"] == "北京"
        assert result.body["result"]["company"] == "中国移动"
        assert result.body["result"]["areacode"] == "0000"



    @allure.story('杭州手机号story1')
    @allure.title('测试手机号归属地title')
    @allure.testcase('http://www.baidu.com')
    @allure.issue('http://www.hao123.com')
    @allure.description('当前手机号是13444223123，归属地是杭州的description')
    @allure.step('先进性归属地的操作step')
    @allure.link('https://mdnf.qq.com/main.shtml', name='dnf手游')
    @allure.severity(severity_level='critical')
    def test_mobile1_dynamic(self):
        param = base_path.read_data()['mobile_belong_dynamic']['params']
        title = base_path.read_data()['mobile_belong_dynamic']['title']
        allure.dynamic.title(title)
        story = base_path.read_data()['mobile_belong_dynamic']['story']
        allure.dynamic.story(story)
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
