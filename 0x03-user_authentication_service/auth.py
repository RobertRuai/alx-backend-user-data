#!/usr/bin/env python3
"""auth module"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """takes in password arguments,returns salted bytes"""
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed
