import json

from utils.AssertUtil import AssertUtil
from utils.YamlUtil import YamlUtils
from utils.log_util import logger


class ExtractUtil:

    def __init__(self):
        self.jsonpath_util = AssertUtil()
        self.yaml_util = YamlUtils()

    def extract_data(self, res, extract):
        """
        根据extract表达式，获取接口内容并存入yaml
        :param res: res.json()
        :param extract: eg $.token
        :return:
        """
        if extract:
            for key, expression in extract.items():
                try:
                    value = self.jsonpath_util.extract_by_jsonpath(res, expression)

                    # 写入value
                    self.yaml_util.write_extra_yaml({key: value})
                except Exception as e:
                    logger.error(f"变量{key}写入extract.yaml失败，请检查，error={e}")

    def get_extract_value(self, key):
        """从extract.yaml中获取内容"""
        try:
            data = self.yaml_util.read_extract_yaml()
            return data[key]
        except Exception as e:
            logger.error(f"从extract.yaml中获取{key}失败，请检查，error={e}")

    def extract_url(self, url):
        # orders/${get_extract_value(order_id)}/
        if '${' in url and '}' in url:
            return self.process_data(url)
        return url

    def process_data(self, data):
        """处理函数"""
        for i in range(data.count('${')):

            if '${' in data and '}' in data:
                start_index = data.index('$')
                end_index = data.index('}')
                # 获取函数中的方法
                func_full_name = data[start_index:end_index + 1]
                # 获取函数名
                func_name = data[start_index + 2:data.index('(')]
                # 获取参数
                func_params = data[data.index('(') + 1:data.index(')')]
                # 先进行getattr
                extract_data = getattr(self, func_name, None)
                if extract_data is not None:
                    # 将参数拆分为列表
                    func_params = func_params.split(',') if func_params else []
                    # 尝试将参数转换为整数，能转则进行转换
                    func_params = [int(param) if param.isdigit() else param for param in func_params]
                    extract_data = extract_data(*func_params)

                # 不支持函数为int类型
                # extract_data = getattr(self, func_name)(*func_params.split(',') if func_params else '')
                data = data.replace(func_full_name, str(extract_data))
            return data

    def extract_case(self, case_info):
        # 转换str类型
        str_case_info = json.dumps(case_info)
        data = self.process_data(str_case_info)
        # 换回json类型
        return json.loads(data)


if __name__ == '__main__':
    print(ExtractUtil().get_extract_value('order_id'))
