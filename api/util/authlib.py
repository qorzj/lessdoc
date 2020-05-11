import base64
import os


def urandom(*, length) -> str:
    byte_size = length * 3 // 4
    return base64.urlsafe_b64encode(os.urandom(byte_size)).decode()
