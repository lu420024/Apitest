import configparser  # 导入 configparser 库以读取 INI 文件
import os  # 导入 os 库以处理文件路径
import yaml  # 导入 yaml 库以处理 YAML 文件

from utils.read_data import read_data  # 从 utils.read_data 模块导入 read_data 函数
from utils.read_ini import read_ini  # 从 utils.read_ini 模块导入 read_ini 函数

# 定义数据文件和配置文件的路径
data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "data", "data.yaml")
ini_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "config", "settings.ini")
file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "file", "caixukun.jpeg")


class FileRead:
    def __init__(self):
        self.data_path = data_path  # 初始化数据文件路径
        self.ini_path = ini_path  # 初始化配置文件路径
        self.file_path = file_path  # 初始化文件路径

    def read_data(self):
        # 打开数据文件并读取内容
        with open(self.data_path, encoding="utf8") as f:
            data = yaml.safe_load(f)
        return data  # 返回数据内容

    def read_ini(self):
        # 创建 ConfigParser 对象并读取配置文件内容
        config = configparser.ConfigParser()
        config.read(self.ini_path, encoding='utf8')
        return config  # 返回配置文件内容

    def read_file(self):
        file = open(self.file_path, 'rb')
        return {'file': ('caixukun.jpeg', file, 'image/jpeg')}


# 实例化 FileRead 类，创建 base_path 对象
base_path = FileRead()
