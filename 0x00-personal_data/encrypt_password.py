#!/usr/bin/env python3
"""encrypt_password module"""
import bcrypt


def hash_password(password: str) -> bytes:
    """returns a salted, hashed password"""
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed


def is_valid(
             hashed_password: bytes,
             password: str) -> bool:
    """validates provided pswd matches hashed pswd"""
    if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
        return True
    return False
