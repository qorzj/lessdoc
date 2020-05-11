from typing import List, Optional
import time
from lessweb import interceptor
from lessweb.plugin.dbplugin import DbServ
from api.po import Directory
from api.po import Major
from api.dealer.auth import admin_only


@interceptor(admin_only)
def admin_list_major(dbServ: DbServ) -> List[Major]:
    return dbServ.mapper(Major).order_by('position').select()


@interceptor(admin_only)
def admin_detail_major(dbServ: DbServ, majorId: int) -> Optional[Major]:
    return dbServ.mapper(Major).by_id(majorId).select_first()


@interceptor(admin_only)
def admin_create_major(
        dbServ: DbServ,
        majorName: str,
        gitUrl: str,
        position: int) -> Major:
    major = Major()
    major.majorName = majorName
    major.gitUrl = gitUrl
    major.position = position
    major.createdAt = int(time.time())
    dbServ.mapper(Major).insert(major)
    return major


@interceptor(admin_only)
def admin_edit_major(
        dbServ: DbServ,
        majorId: int,
        majorName: str,
        gitUrl: str,
        position: int):
    major = Major()
    major.majorName = majorName
    major.gitUrl = gitUrl
    major.position = position
    dbServ.mapper(Major).by_id(majorId).update(major)
    return {}


@interceptor(admin_only)
def admin_delete_major(dbServ: DbServ, majorId: int):
    total = dbServ.mapper(Directory).and_equal({'majorId': majorId}).select_count()
    assert total == 0, '不能删除非空的专栏，请先删除目录'
    dbServ.mapper(Major).by_id(majorId).delete()
    return {}
