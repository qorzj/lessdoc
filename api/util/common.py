import hashlib


def get_admin_token() -> str:
    return 'MS7jyDGTLi0OPJ6BY5ARDkL5R7qa'


def check_admin_pwd(pwd) -> bool:
    pwd = f'0OP{pwd}J.qw'
    return hashlib.sha1(pwd.encode()).hexdigest() == 'eb44cdbe6878b6cee3e3cd07e111670e0d4c5f00'


def ok_result(*, message='success', result=None):
    ret = {'code': 200, 'message': message}
    if result is not None:
        ret['result'] = result
    return ret
