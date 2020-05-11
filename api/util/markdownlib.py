import bleach
import markdown  # type: ignore
from markdown.extensions.footnotes import FootnoteExtension  # type: ignore
from markdown.extensions.fenced_code import FencedCodeExtension  # type: ignore
from markdown.extensions.tables import TableExtension  # type: ignore
from markdown.extensions.nl2br import Nl2BrExtension  # type: ignore
from markdown.extensions.toc import TocExtension  # type: ignore
from markdown.extensions.codehilite import CodeHiliteExtension  # type: ignore
from mdx_truly_sane_lists import makeExtension as TrulySaneExt  # type: ignore
from pymdownx import tilde, caret, slugs  # type: ignore


def parse(text):
    """
    https://github.com/Python-Markdown/markdown/wiki/Third-Party-Extensions
    https://facelessuser.github.io/pymdown-extensions
    """
    text = markdown.markdown(text, extensions=[
        FootnoteExtension(),
        TableExtension(),
        FencedCodeExtension(),
        CodeHiliteExtension(),
        Nl2BrExtension(),
        TocExtension(slugify=slugs.uslugify, permalink=False),
        TrulySaneExt(),
        tilde.makeExtension(),
        caret.makeExtension(),
    ])
    tags = 'a,h1,h2,h3,h4,h5,h6,p,div,pre,code,span,img,br,' \
           'ul,ol,li,table,tr,th,td,thead,tbody,blockquote,' \
           'del,em,strong,sub,sup'
    attrs = {'*': ['class'], 'a': ['href', 'rel'], 'img': ['alt']}
    attrs.update({f'h{n}':['id'] for n in range(1, 7)})  # h1..h6 support TOC anchor
    text = bleach.clean(text, tags=tags.split(','), attributes=attrs,)  # HTML sanitizer
    return text


if __name__ == '__main__':
    text = """
First Header  | Second Header
------------- | -------------
Content Cell  | Content Cell
Content Cell  | Content Cell

    """
    print(parse(text))