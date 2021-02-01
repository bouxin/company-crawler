### 天眼查、企查查 
### 公司信息爬虫


------

## 使用说明

1. 设置数据源
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
2. 执行```db/data.sql```生成数据结构
3. 配置IP代理```config/settings```
    ```pydocstring
    # 全局代理控制
    GLOBAL_PROXY = True
    PROXY_POOL_URL = "http://localhost:5010"
    ```
4. 设置爬取关键字```qichacha```&```tianyancha```
    ```pydocstring
    keys = ['Google'] # 设置爬取列表
    crawler.load_keys(keys)
    crawler.start()
    ```
   
PS：**建议使用IP代理 + 随机UA，否者一定会被ban**
1. 随机UA推荐[fake_useragent](https://github.com/hellysmile/fake-useragent)
2. 代理池推荐[proxy_pool](https://github.com/jhao104/proxy_pool.git)
