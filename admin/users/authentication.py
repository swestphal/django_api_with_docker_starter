import jwt
import datetime
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.handlers import exception
from rest_framework.authentication import BaseAuthentication


def generate_access_token(user):
    payload = {
        'user_id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        'iat': datetime.datetime.utcnow()
    }

    return jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256').decode('utf-8')


class JWTAuthentication(BaseAuthentication):

    def authenticate(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            return None

        try:
            # get payload
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise exception.AuthentificationFailed('not authenticated')

        user = get_user_model().objects.filter(id=payload['user_id']).first()

        if user is None:
            raise exception.AuthenticationFailed('User not found')

        return (user, None)
