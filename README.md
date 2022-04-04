### 天眼查、企查查 
### 公司信息爬虫


------

## 使用说明

1. 设置用户状态
   
   抓包工具抓包天眼查、企查查小程序，设置请求头用户鉴权信息，在各自目录的<code>__init__.py</code>文件中
   
2. 设置数据源
    ```pydocstring
    MysqlConfig = {
        'develop': {
            'host': '192.168.1.103',
            'port': 3306,
            'db': 'enterprise',
            'username': 'root',
            'password': 'root@123'
        }
    }
    ```
3. 执行```db/data.sql```生成数据结构
4. 配置IP代理```config/settings```
    ```pydocstring
    # 全局代理控制
    GLOBAL_PROXY = True
    PROXY_POOL_URL = "http://localhost:5010"
    ```
5. 入口函数设置db写入方法
   ```python
   def start():
    def __printall(items):
        for elem in items:
            logging.info(elem.__str__()
    keys = globals().get('keywords', [])
    for key in keys:
        logging.info('正在采集[%s]...' % key)
        companies = TycClient().search(key).companies
        # 写入db
        # insert_company(companies)
        __printall(companies)
    logging.info("completed")
   ```
6. 设置爬取关键字```qichacha```&```tianyancha```
    ```pydocstring
    keys = ['Google'] # 设置爬取列表
    crawler.load_keys(keys)
    crawler.start()
    ```
   

###**推荐使用IP代理 + 随机UA**
1. 随机UA[fake_useragent](https://github.com/hellysmile/fake-useragent)
2. 代理池[proxy_pool](https://github.com/jhao104/proxy_pool.git)

