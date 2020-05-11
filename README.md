# lesswebcn

www.lessweb.cn

## alembic
https://alembic.sqlalchemy.org/en/latest/tutorial.html

init
```bash
alembic init alembic

vim alembic.ini
- sqlalchemy.url =
+ sqlalchemy.url = sqlite:///data/main.db

vim alembic/versions
- target_metadata = None

vim alembic/env.py
+ import sys
+ sys.path.insert(0, '.')
+ from ... import Tbl...  # import all Tbl...
+ target_metadata = (Tbl...).metadata

rm alembic/versions/*.py
```

commit version
```bash
alembic revision --autogenerate -m "create table"  # 如果失败，请检查main.db的version与当前PO是否冲突
```

touch database
```
alembic upgrade head
```