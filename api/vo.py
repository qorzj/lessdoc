from lessweb.plugin.dbplugin import table


# 文章
@table(name='(SELECT TblArticle.*, '
            ' TblDirectory.dirName, '
            ' TblDirectory.position AS dirPosition, '
            ' TblDirectory.majorId, '
            ' TblMajor.majorName, '
            ' TblMajor.gitUrl, '
            ' TblMajor.position AS majorPosition '
            ' FROM TblArticle '
            ' LEFT JOIN TblDirectory ON TblDirectory.dirId=TblArticle.dirId '
            ' LEFT JOIN TblMajor ON TblMajor.majorId=TblDirectory.majorId) V')
class ArticleVo:
    articleId: int  # 文章ID
    articleKey: str  # URL唯一标识
    title: str  # 文章标题
    contentMd: str  # 文章正文(markdown格式)
    contentHtml: str  # 文章正文(html格式)
    dirId: int  # 所属的目录ID
    posInDir: int  # 目录内的排序位置，从小到大排序
    createdAt: int  # 创建时间
    updatedAt: int  # 最近修改时间

    dirName: str  # 目录名称
    dirPosition: int  # 目录排序位置
    majorId: int  # 专栏ID
    majorName: str  # 专栏名称
    gitUrl: str  # git项目地址
    majorPosition: int  # 专栏排序位置


# 目录
@table(name='(SELECT TblDirectory.*, '
            ' TblMajor.majorName, '
            ' TblMajor.position AS majorPosition '
            ' FROM TblDirectory '
            ' LEFT JOIN TblMajor ON TblMajor.majorId=TblDirectory.majorId) V')
class DirectoryVo:
    dirId: int  # 目录ID
    majorId: int  # 专栏ID
    dirName: str  # 目录名称
    position: int  # # 在专栏中的排序位置，从1开始
    createdAt: int  # 创建时间

    majorName: str  # 专栏名称
    majorPosition: int  # 专栏排序位置
