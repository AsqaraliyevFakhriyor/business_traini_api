import sys

import jwt

from rest_framework.exceptions import AuthenticationFailed


def check_token(secret, alogrithm, request):
    try:
        token = request.COOKIES.get("token")
        if token is None:
            raise AuthenticationFailed("token missing")
        payload = jwt.decode(token, secret, alogrithm)
        return payload
    except jwt.ExpiredSignatureError:
        print(sys.exc_info())
        raise AuthenticationFailed("token expired")
