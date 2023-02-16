天眼查、企查查公司信息爬虫 
===


## 使用说明

1. 设置用户状态
   
   抓包工具抓包天眼查、企查查小程序，设置请求头用户鉴权信息，在各自目录的<code>__init__.py</code>文件中。可在此处配置随机UA，项目地址：[fake_useragent](https://github.com/hellysmile/fake-useragent)
   
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
4. 配置IP代理```config/settings```, 开启global proxy前请先自行部署ip代理池，项目地址：[proxy_pool](https://github.com/jhao104/proxy_pool.git)
    ```pydocstring
    # 全局代理控制, 
    GLOBAL_PROXY = True
    PROXY_POOL_URL = "http://localhost:5010"
    ```
5. 设置爬取关键字```qichacha```&```tianyancha```
    ```pydocstring
    keys = ['Google'] # 设置爬取列表
    crawler.load_keys(keys)
    crawler.start()
    ```


## Schedule List
|功能|日期|状态|备注|
|---|---|---|---|
|鉴权Token提取||待完成||
|内置IP代理||待完成||
|防封策略||待完成||
|容器化运行||待完成||

<br />
<br />

Please Kindly Note
===

我建立了一个，程序员技术交流的tg群，欢迎大家加入！！！

内有技术交流！工作内推！远程工作！兼职、私活儿！！。

Telegram群链接：[程序员社区https://t.me/+iZK2y8zMUiE0NDE1](https://t.me/+iZK2y8zMUiE0NDE1)

Telegram群二维码：

<img width='200' src='https://i.imgur.com/R62JrQX.png'>
