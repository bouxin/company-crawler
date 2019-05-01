## 企业信息爬虫
>天眼查数据爬虫通过搜索关键字爬取企业详细信息

---
#### 运行项目
1. 安装依赖
    ```bash
    pip install -r requirements.txt    # 当提示权限不足时，使用sudoer权限执行即可
    ```
2. 生成数据结构  
执行data.sql脚本生成数据结构，修改环境配置
3. 设置关键字  
在tianyancha.py中配置keys关键字集合
3. 运行脚本
    ```bash
    python3 tianyancha.py
    ```
#### 项目结构
```
├── LICENSE
├── README.md
├── config
│   ├── __init__.py
│   ├── env.py
│   └── settings.py
├── db
│   ├── __init__.py
│   ├── data.sql
│   └── mysql_connector.py
├── qichacha
│   ├── __init__.py
│   └── crawler.py
├── requirements.txt
├── tianyancha
│   ├── __init__.py
│   └── crawler.py
├── tianyancha.py
└── util
    ├── __init__.py
    ├── date.py
    ├── httpclient.py
    └── log.py

```



***声明：本项目仅做技术交流，本人不担当任何侵犯他人利益及其他违反国家法律等行为的技术支持角色，
如因使用该项目代码另做他途产生任何后果本人概不负责。***
