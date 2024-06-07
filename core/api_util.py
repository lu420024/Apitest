from core.rest_client import RestClient  # 从 core.rest_client 模块导入 RestClient 类


class Api(RestClient):
    def __init__(self):
        super().__init__()  # 调用父类的初始化方法

    def get_mobile_belong(self, **kwargs):

        return self.get('sell/shouji/query', **kwargs)

    def post_data(self, **kwargs):

        return self.post('/posts', **kwargs)

    # 实战短信验证码
    def get_code(self, **kwargs):

        return self.post('code/', **kwargs)

    def register_mobile(self, **kwargs):

        return self.post('users/', **kwargs)

    def user_login(self, **kwargs):

        return self.post('login/', **kwargs)

    def shopping_add(self, **kwargs):

        return self.post('shopcarts/', **kwargs)

#   goods banner
    def banner(self, **kwargs):

        return self.get('banners/', **kwargs)

    def add_message(self, **kwargs):

        return self.post('messages/', **kwargs)


# 实例化 Api 类，创建 api_util 对象
api_util = Api()
