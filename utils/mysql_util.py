import pymysql
import pytest

from utils.log_util import logger
from utils.read import base_path

data = base_path.read_ini()['MYSQL']

DB_CONF = {
    'host': data['MYSQL_HOST'],
    'port': int(data['MYSQL_PORT']),
    'user': data['MYSQL_USER'],
    'password': data['MYSQL_PASSWD'],
    'db': data['MYSQL_DB']
}


class MysqlDb:
    # 连接数据库
    def __init__(self):
        self.conn = pymysql.connect(**DB_CONF, autocommit=True)
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 关闭数据库

    def __del__(self):
        self.cur.close()
        self.conn.close()

    # 查询一条
    def select_db_one(self, sql):
        logger.info(f'执行sql:{sql}')
        self.cur.execute(sql)
        # 获取数据
        result = self.cur.fetchone()
        logger.info(f'sql查询结果:{result}')
        return result

    # 查询多条
    def select_db_all(self, sql):
        logger.info(f'执行sql:{sql}')
        self.cur.execute(sql)
        # 获取数据
        result = self.cur.fetchall()
        logger.info(f'sql查询结果:{result}')
        return result

    def execute_db(self, sql):

        try:
            logger.info(f'执行sql:{sql}')
            self.cur.execute(sql)
            self.conn.commit()

        except Exception as e:
            logger.info('执行sql出错{}'.format(e))


db = MysqlDb()

if __name__ == '__main__':

    result = db.select_db_one('select code from users_verifycode where mobile = "15013680005" order by id desc;')
    print(result)
