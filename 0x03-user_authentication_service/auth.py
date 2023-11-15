#!/usr/bin/env python3
"""auth module"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> bytes:
    """takes in password arguments,returns salted bytes"""
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed


def __generate_uuid() -> str:
    """generates uuid"""
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """registers new user to the db"""
        try:
            user = self._db.find_user_by(email=email)
            raise ValueError("User {} already exists".format(email))
        except NoResultFound:
            hashed = _hash_password(password)
            return self._db.add_user(email, hashed)

    def valid_login(self, email: str, password: str) -> bool:
        """validates user's credentials"""
        try:
            user = self._db.find_user_by(email=email)
            if user:
                if bcrypt.checkpw(
                                  password.encode('utf-8'),
                                  user.hashed_password):
                    return True
                return False
        except NoResultFound:
            return False
