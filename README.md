
---
#### 运行项目
1. 安装依赖
 >    ```bash
 >    pip install -r requirements.txt    # 当提示权限不足时，使用sudoer权限执行即可
 >    ```
2. 生成数据结构  
 >执行data.sql脚本生成数据结构，在```config/settings.py```中修改数据库连接
3. 设置关键字  
 >在```tianyancha.py```中添加关键字，或从缓存、数据库读取关键字
3. 后台运行, 自定义了日志收集，不需要nohup的标准输出日志
 >   ```bash
 >   # 天眼查
 >   nohup python3 tianyancha.py >/dev/null 2>&1 &
 >   # 企查查
 >   nohup python3 qichacha.py >/dev/null 2>&1 &
 >   ```
     
#### 项目结构
```
├── LICENSE
├── README.md
├── config
│   ├── __init__.py
│   ├── env.py
│   └── settings.py
├── const
│   ├── __init__.py
│   └── constants.py
├── db
│   ├── __init__.py
│   ├── data.sql
│   ├── model
│   │   ├── __init__.py
│   │   └── model.py
│   └── mysql_connector.py
├── qichacha
│   ├── __init__.py
│   ├── client.py
│   ├── crawler.py
│   └── manager.py
├── qichacha.log
├── qichacha.py
├── requirements.txt
├── tianyancha
│   ├── __init__.py
│   ├── client.py
│   ├── crawler.py
│   └── manager.py
├── tianyancha.log
├── tianyancha.py
├── tree.md
└── util
    ├── __init__.py
    ├── date.py
    ├── httpclient.py
    └── log.py

```



***声明：本项目仅做技术交流，本人不担当任何侵犯他人利益及其他违反国家法律等行为的技术支持角色，
如因使用该项目代码另做他途产生任何后果本人概不负责。***
