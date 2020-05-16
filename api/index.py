import leancloud  # type: ignore
from lessweb import Application
from lessweb.plugin.dbplugin import DbPlugin
from api.processor import global_processor
from api.config import Config


leancloud.init(Config.leancloud_app_id, Config.leancloud_app_key)
app = Application()
app.add_plugin(DbPlugin('data/main.db'))
app.add_interceptor('.*', method='*', dealer=global_processor)

import api.dealer.auth
app.add_post_mapping('/public/mgr/login', dealer=api.dealer.auth.admin_login)
app.add_post_mapping('/mgr/logout', dealer=api.dealer.auth.admin_logout)
app.add_get_mapping('/mgr/me', dealer=api.dealer.auth.admin_me)
app.add_get_mapping('/manage/?', dealer=api.dealer.auth.admin_home)

import api.dealer.article
app.add_put_mapping('/public/article/preview', dealer=api.dealer.article.preview_article)
app.add_post_mapping('/mgr/article', dealer=api.dealer.article.admin_create_article)
app.add_put_mapping('/mgr/article', dealer=api.dealer.article.admin_edit_article)
app.add_get_mapping('/mgr/article/list', dealer=api.dealer.article.admin_list_article)
app.add_get_mapping('/mgr/article/detail', dealer=api.dealer.article.admin_detail_article)
app.add_delete_mapping('/mgr/article/{articleId}', dealer=api.dealer.article.admin_delete_article)
app.add_get_mapping('/', dealer=api.dealer.article.user_detail_article)
app.add_get_mapping('/note/{articleKey}', dealer=api.dealer.article.user_detail_article)

import api.dealer.directory
app.add_post_mapping('/mgr/dir', dealer=api.dealer.directory.admin_create_dir)
app.add_put_mapping('/mgr/dir', dealer=api.dealer.directory.admin_edit_dir)
app.add_get_mapping('/mgr/dir/list', dealer=api.dealer.directory.admin_list_dir)
app.add_get_mapping('/mgr/dir/detail', dealer=api.dealer.directory.admin_detail_dir)
app.add_delete_mapping('/mgr/dir/{dirId}', dealer=api.dealer.directory.admin_delete_dir)

import api.dealer.major
app.add_post_mapping('/mgr/major', dealer=api.dealer.major.admin_create_major)
app.add_put_mapping('/mgr/major', dealer=api.dealer.major.admin_edit_major)
app.add_get_mapping('/mgr/major/list', dealer=api.dealer.major.admin_list_major)
app.add_get_mapping('/mgr/major/detail', dealer=api.dealer.major.admin_detail_major)
app.add_delete_mapping('/mgr/major/{majorId}', dealer=api.dealer.major.admin_delete_major)
