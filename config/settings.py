# "develop", "test", "prod"
ENV = "develop"

PROXY_POOL_URL = "http://localhost:5010"

""" mysql 配置 """
MysqlConfig = {
    'develop': {
        'host': '192.168.1.103',
        'port': 3307,
        'db': 'enterprise',
        'username': 'root',
        'password': 'root@123'
    }
}




