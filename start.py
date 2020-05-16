import os
from lessweb.utils import makedir
from api.config import Config

if __name__ == '__main__':
    if not Config.leancloud_app_id:
        print('请在api/config.py中设置Leancloud APP_ID')
        exit(1)
    if not Config.leancloud_app_key:
        print('请在api/config.py中设置Leancloud APP_KEY')
        exit(1)
    makedir('data')
    os.system('alembic upgrade head')
    from api.index import app
    app.run()
