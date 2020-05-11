from sqlalchemy import Table, MetaData
from sqlalchemy import Column, Integer, TEXT


metadata = MetaData()


# 文章
tbl_article = Table(
    'TblArticle',
    metadata,
    Column('articleId', Integer, primary_key=True),  # 文章ID
    Column('articleKey', TEXT, unique=True),  # URL唯一标识
    Column('title', TEXT),  # 文章标题
    Column('contentMd', TEXT),  # 文章正文(markdown格式)
    Column('contentHtml', TEXT),  # 文章正文(html格式)
    Column('dirId', Integer),  # 所属的目录ID
    Column('posInDir', Integer),  # 目录内的排序位置
    Column('createdAt', Integer),
    Column('updatedAt', Integer),
)

# 目录
tbl_directory = Table(
    'TblDirectory',
    metadata,
    Column('dirId', Integer, primary_key=True),  # 目录ID
    Column('majorId', Integer),  # 工作区
    Column('dirName', TEXT),  # 目录名称
    Column('position', Integer),  # 在专栏中的排序位置，从1开始
    Column('createdAt', Integer),
)

# 专栏
tbl_major = Table(
    'TblMajor',
    metadata,
    Column('majorId', Integer, primary_key=True),  # 专栏ID
    Column('majorName', TEXT),  # 专栏名称
    Column('gitUrl', TEXT),  # git项目地址
    Column('position', Integer),  # 排序位置，从1开始
    Column('firstArticle', TEXT),  # 第一篇文章的key
    Column('createdAt', Integer),
)
