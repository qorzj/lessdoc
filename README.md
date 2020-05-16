# 简介
lessdoc是基于lessweb开发的在线文档搭建工具，[lessweb](http://www.lessweb.cn)网站本身就是用lessdoc搭建的。

# 创建leancloud应用
lessdoc的后台管理系统使用leancloud完成管理员登录鉴权功能。

1. 访问 https://leancloud.cn ，注册用户，可能需要完成实名认证。
2. 创建应用 → https://leancloud.cn/docs/dashboard_guide.html#hash650323347
3. 添加新用户
  1. 进入创建的应用，选择「存储 > 用户」。
  2. 点「添加用户」按钮，输入用户名和密码即可添加新用户。
4. 进入创建的应用，选择「设置 > 应用Keys」，保存AppID和AppKey，后面会用到。

# 如何启动？
## 启动virtualenv
什么是virtualenv？→ https://www.liaoxuefeng.com/wiki/1016959663602400/1019273143120480

注意：运行lessdoc的python版本最低要求为3.6.0

```bash
virtualenv venv
. venv/bin/activate
```

## 安装依赖
```bash
git clone https://github.com/qorzj/lessdoc.git
cd lessdoc
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
```

## 修改配置
编辑`api/config.py`，设置leancloud的AppID和AppKey，以及其他参数。

## 启动服务
```bash
python start.py
```
服务启动成功后，访问 http://localhost:8080/manage 进入管理后台，可以创建和编辑专栏、目录和文章。

创建文章后，就可以访问在线文档的首页 http://localhost:8080 

注意：如果还没有创建第一篇文章，则访问首页会返回400错误。

# 源码分析
lessdoc启动的入口是`start.py`，`start.py`会检查`api/config.py`是否设置了leancloud的参数，然后使用alembic把数据库schema版本migrate至最新，接着导入`api/index.py`的代码。

所以逐行阅读`api/index.py`，分析插件的初始化，以及路由配置即可。

## 数据库版本管理
lessdoc使用的是sqlite本地文件数据库。

lessdoc使用[alembic](https://alembic.sqlalchemy.org/en/latest/tutorial.html) 做数据库schema版本管理（即migrate）

数据库相关的文件和目录有：`api/tables.py`, `alembic/`, `alembic.ini`。`api/tables.py`按照[sqlalchemy](https://docs.sqlalchemy.org/en/latest/core/metadata.html) 的规则编写，其他文件和目录是按如下步骤生成的：

一. 运行命令：
```bash
alembic init alembic
```
会创建`alembic/`文件夹和`alembic.ini`文件。

二. 修改`alembic.ini`
把
```
sqlalchemy.url =
```
这一行改为
```
sqlalchemy.url = sqlite:///data/main.db
```

三. 修改`alembic/env.py`
把
```
target_metadata = None
```
这一行改为
```python
import sys
sys.path.insert(0, '.')
from api.tables import metadata
target_metadata = metadata
```

四. 修改`api/tables.py`，修改完成定型之后，需要自动生成versions源文件，即运行
```bash
alembic revision --autogenerate -m "..."  # 如果失败，则说明main.db已包含版本有冲突的数据，建议备份数据然后删除已有的main.db
```

五. 更新数据库版本
```
alembic upgrade head
```
运行此命令后如果没有`data/main.db`文件，则会自动创建。如果已经创建，则会尝试更新`data/main.db`的数据库schema。

直接运行
```
python start.py
```
也一样，因为`start.py`内包含了`os.system("alembic upgrade head")`语句。