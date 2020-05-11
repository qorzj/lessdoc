from typing import List, Optional
import time
from lessweb import interceptor
from lessweb.plugin.dbplugin import DbServ
from api.util import markdownlib
from api.vo import ArticleVo
from api.po import Article, Directory, Major
from api.service import DirServ, MajorServ
from api.dealer.auth import admin_only
from api.processor import page_view
from api.config import Config


def preview_article(contentMd: str):
    return {'contentHtml': markdownlib.parse(contentMd)}


@interceptor(admin_only)
def admin_create_article(
        dbServ: DbServ,
        majorServ: MajorServ,
        articleKey: str,
        title: str,
        contentMd: str,
        dirId: int,
        posInDir: int,
):
    contentHtml = markdownlib.parse(contentMd)
    article = Article()
    article.articleKey = articleKey
    article.title = title
    article.contentMd = contentMd
    article.contentHtml = contentHtml
    article.dirId = dirId
    article.posInDir = posInDir
    article.createdAt = article.updatedAt = int(time.time())
    dbServ.mapper(Article).insert(article)
    majorServ.update_first_article()
    return {}


@interceptor(admin_only)
def admin_edit_article(
        dbServ: DbServ,
        majorServ: MajorServ,
        articleId: int,
        articleKey: str,
        title: str,
        contentMd: str,
        dirId: int,
        posInDir: int,
):
    contentHtml = markdownlib.parse(contentMd)
    article = Article()
    article.articleKey=articleKey
    article.title=title
    article.contentMd=contentMd
    article.contentHtml=contentHtml
    article.dirId=dirId
    article.posInDir=posInDir
    article.updatedAt=int(time.time())
    dbServ.mapper(Article).by_id(articleId).update(article)
    majorServ.update_first_article()
    return {}


@interceptor(admin_only)
def admin_delete_article(dbServ: DbServ, articleId: int):
    dbServ.mapper(Article).by_id(articleId).delete()
    return {}


@interceptor(admin_only)
def admin_detail_article(dbServ: DbServ, articleId: int) -> Optional[ArticleVo]:
    return dbServ.mapper(ArticleVo).by_id(articleId).select_first()


@interceptor(admin_only)
def admin_list_article(dbServ: DbServ) -> List[ArticleVo]:
    return dbServ.mapper(ArticleVo).order_by('majorPosition,dirPosition,posInDir').select()


@interceptor(page_view('tpl/article_page.mako'))
def user_detail_article(
        dbServ: DbServ,
        dirServ: DirServ,
        majorServ: MajorServ,
        articleKey: str=''):
    if articleKey:
        article_vo = dbServ.mapper(ArticleVo).and_equal({'articleKey': articleKey}).select_first()
    else:
        article_vo = dbServ.mapper(ArticleVo).order_by('majorPosition,dirPosition,posInDir').select_first()
    assert article_vo, '文章不存在'
    return {
        'article': article_vo,
        'dirIndex': dirServ.make_dir_index(article_vo.majorId, article_vo.articleId),
        'majorIndex': majorServ.make_major_index(article_vo.majorId),
        'config': {
            'site_name': Config.site_name,
            'ga_id': Config.ga_id,
            'icp_beian': Config.icp_beian,
        },
    }

