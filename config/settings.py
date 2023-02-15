# "dev", "test", "prod"
ENV = "dev"

# 全局代理控制
GLOBAL_PROXY = True
PROXY_POOL_URL = "http://127.0.0.1:5010"

""" mysql 配置 """
MysqlConfig = {
    'dev': {
        'host': '192.168.1.103',
        'port': 3306,
        'db': 'enterprise',
        'password': 'root@123'
    },
    'test': {

        'username': 'root',
    },
    'prod': {

    }
}




