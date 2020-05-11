from lessweb.plugin.dbplugin import table, transient


# 文章
@table(name='TblArticle')
class Article:
    articleId: int  # 文章ID
    articleKey: str  # URL唯一标识
    title: str  # 文章标题
    contentMd: str  # 文章正文(markdown格式)
    contentHtml: str  # 文章正文(html格式)
    dirId: int  # 所属的目录ID
    posInDir: int  # 目录内的排序位置，从小到大排序
    createdAt: int  # 创建时间
    updatedAt: int  # 最近修改时间


# 目录
@table(name='TblDirectory')
class Directory:
    dirId: int  # 目录ID
    majorId: int  # 专栏ID
    dirName: str  # 目录名称
    position: int  # # 在专栏中的排序位置，从1开始
    createdAt: int  # 创建时间


# 专栏
@transient('selected')
@table(name='TblMajor')
class Major:
    majorId: int  # 专栏ID
    majorName: str  # 专栏名称
    gitUrl: str  # git项目地址
    position: int  # 排序位置，从1开始
    firstArticle: str  # 第一篇文章的key
    createdAt: int  # 创建时间
    selected: bool  # 是否被选中
