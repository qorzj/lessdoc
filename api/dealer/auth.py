import leancloud  # type: ignore
from enum import Enum
import time
from lessweb import BadParamError, Context, interceptor, HttpStatus
from api.processor import page_view


class Security:
    try_count = 0
    cooldown_time = 0

    @classmethod
    def incre(cls):
        cls.cooldown_time += 1
        if cls.cooldown_time >= 3:
            cls.cooldown_time = 0
            cls.cooldown_time = int(time.time()) + 60


class AuthKey(Enum):
    me = 1


def admin_only(ctx: Context):
    request, response = ctx.request, ctx.response
    token = request.get_auth_bearer() or '!'
    try:
        user = leancloud.User.become(token)
    except leancloud.LeanCloudError:
        response.set_status(HttpStatus.Forbidden)
        return {}
    if user.get_username() != 'admin':
        response.set_status(HttpStatus.Forbidden)
        return {}
    ctx.box[AuthKey.me] = user
    return ctx()


def admin_login(username: str, password: str):
    now_time = int(time.time())
    if now_time < Security.cooldown_time:
        raise BadParamError(message=f'用户名密码错误过多，{Security.cooldown_time - now_time}秒后重试')
    user = leancloud.User()
    try:
        Security.try_count = 0
        user.login(username, password)
    except leancloud.LeanCloudError as e:
        Security.incre()
        raise BadParamError(message=str(e.error), param='')
    return {'token': user.get_session_token()}


@interceptor(admin_only)
def admin_logout(ctx: Context):
    ctx.box[AuthKey.me].logout()
    return {}


@interceptor(admin_only)
def admin_me(ctx: Context):
    user = ctx.box[AuthKey.me]
    return {'username': user.get_username()}


@interceptor(page_view('tpl/manage_home.mako'))
def admin_home():
    return {}
