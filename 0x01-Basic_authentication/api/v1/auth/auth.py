#!/usr/bin/env python3
"""auth module"""
from flask import request
from typing import List, TypeVar


class Auth:
    """auth class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """returns args"""
        if path is None or not excluded_paths:
            return True
        if path[-1] != '/':
            path = path + '/'
        else:
            path
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """auth header function"""
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """current user function"""
        return None
	

class BasicAuth(Auth):
    """BasicAuth class """
