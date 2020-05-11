from typing import List
from lessweb.plugin.dbplugin import DbServ
from api.po import Directory, Article, Major
from api.vo import ArticleVo
from api.util.smart_list import SmartList


class DirServ:
    dbServ: DbServ

    def make_dir_index(self, majorId:int, articleId:int) -> SmartList:
        """
        result:dir[] => {name:str, dirId:int, articles:dir[] => {title:str, key:str, selected:bool}}
        """
        dir_tree = SmartList()
        articles = self.dbServ.mapper(ArticleVo).and_equal({'majorId': majorId})\
            .order_by('dirPosition,posInDir').select()
        for article in articles:
            try:
                dir_item = dir_tree.find(lambda x: x['dirId']==article.dirId)
            except IndexError:
                dir_item = {'name': article.dirName, 'dirId': article.dirId, 'articles': SmartList()}
                dir_tree.append(dir_item)
            dir_item['articles'].append({
                'title': article.title, 'key': article.articleKey, 'selected': article.articleId==articleId})
        return dir_tree


class MajorServ:
    dbServ: DbServ

    def make_major_index(self, majorId:int) -> List[Major]:
        majors = self.dbServ.mapper(Major).order_by('position').select()
        for major in majors:
            major.selected = (major.majorId == majorId)
        return majors

    def update_first_article(self) -> None:
        for major in self.dbServ.mapper(Major).select():
            first_article = self.dbServ.mapper(ArticleVo).and_equal({'majorId': major.majorId})\
                .order_by('dirPosition,posInDir').select_first()
            if first_article:
                major_up = Major()
                major_up.firstArticle = first_article.articleKey
                self.dbServ.mapper(Major).by_id(major.majorId).update(major_up)
