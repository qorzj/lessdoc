from mako.template import Template  # type: ignore
from lessweb import Context


def global_processor(ctx: Context):
    try:
        return ctx()
    except AssertionError as e:
        return {'code': 400, 'message': str(e)}


def page_view(tpl):
    def processor(ctx: Context):
        ret = ctx()
        if ctx.request.is_json():
            return ret
        else:
            return Template(filename=tpl, input_encoding='utf-8', output_encoding='utf-8').render(**ret)
    return processor
