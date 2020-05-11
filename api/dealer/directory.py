from typing import List, Optional
import time
from lessweb import interceptor
from lessweb.plugin.dbplugin import DbServ
from api.vo import DirectoryVo
from api.po import Directory
from api.po import Major
from api.po import Article
from api.dealer.auth import admin_only


@interceptor(admin_only)
def admin_list_dir(dbServ: DbServ) -> List[DirectoryVo]:
    return dbServ.mapper(DirectoryVo).order_by('majorPosition,position').select()


@interceptor(admin_only)
def admin_detail_dir(dbServ: DbServ, dirId: int) -> Optional[Directory]:
    return dbServ.mapper(Directory).by_id(dirId).select_first()


@interceptor(admin_only)
def admin_create_dir(
        dbServ: DbServ,
        dirName: str,
        majorId: int,
        position: int) -> Directory:
    directory = Directory()
    directory.dirName = dirName
    directory.majorId = majorId
    directory.position = position
    directory.createdAt = int(time.time())
    dbServ.mapper(Directory).insert(directory)
    return directory


@interceptor(admin_only)
def admin_edit_dir(
        dbServ: DbServ,
        dirId: int,
        dirName: str,
        majorId: int,
        position: int):
    directory = Directory()
    directory.dirName = dirName
    directory.majorId = majorId
    directory.position = position
    dbServ.mapper(Directory).by_id(dirId).update(directory)
    return {}


@interceptor(admin_only)
def admin_delete_dir(dbServ: DbServ, dirId: int):
    total = dbServ.mapper(Article).and_equal({'dirId': dirId}).select_count()
    assert total == 0, '不能删除非空的目录，请先删除文章'
    dbServ.mapper(Directory).by_id(dirId).delete()
    return {}
