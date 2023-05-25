from datetime import datetime, timedelta

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import ValidationError
from passlib.hash import bcrypt
from jose import jwt, JWTError

from server.settings import settings
from server.schemas import User, Token


class AuthError(HTTPException):
    def __init__(self):
        super().__init__(
            status.HTTP_401_UNAUTHORIZED,
            headers={'WWW-Authenticate': 'Bearer'}
        )


class TokenValidationError(AuthError):
    def __init__(self):
        super().__init__()
        self.detail = 'Could not validate credentials'


class IncorrectUsernameError(AuthError):
    def __init__(self):
        super().__init__()
        self.detail = 'Incorrect username'


class IncorrectPasswordError(AuthError):
    def __init__(self):
        super().__init__()
        self.detail = 'Incorrect password'


class UsernameAlreadyExistsError(HTTPException):
    def __init__(self):
        super().__init__(
            status.HTTP_422_UNPROCESSABLE_ENTITY,
            headers={'WWW-Authenticate': 'Bearer'},
            detail='Username already exists'
        )


def get_current_user(token: str = Depends(OAuth2PasswordBearer(tokenUrl='/auth/sign-in'))) -> User:
    return Auth.verify_token(token)


class Auth:

    @classmethod
    def hash_password(cls, password: str) -> str:
        return bcrypt.hash(password)

    @classmethod
    def verify_password(cls, password: str, password_hash: str) -> bool:
        return bcrypt.verify(password, password_hash)

    @classmethod
    def create_token(cls, user_id: int, username: str) -> Token:
        now = datetime.utcnow()
        payload = {
            'iat': now,
            'nbf': now,
            'exp': now + timedelta(seconds=settings.jwt_expiration),
            'sub': str(user_id),
            'user': {'id': user_id, 'username': username}
        }

        token = jwt.encode(payload, settings.jwt_secret, algorithm=settings.jwt_algorithm)
        return Token(access_token=token)

    @classmethod
    def verify_token(cls, token: str) -> User:
        try:
            payload = jwt.decode(token, settings.jwt_secret, algorithms=[settings.jwt_algorithm])
        except JWTError:
            raise TokenValidationError

        user_data = payload.get('user')

        try:
            user = User.parse_obj(user_data)
        except ValidationError:
            raise TokenValidationError

        return user
