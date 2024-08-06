#!/usr/bin/env python3
"""The Auth class"""
from flask import request
from typing import List, TypeVar


class Auth:
    """A class that performs authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if the path requires authentication

        Returns:
            True: if
                    - path is None
                    - excluded_paths is None or empty
            False: if
                    - path is in excluded_paths
        """
        if not (path and excluded_paths):
            return True
        if path[-1] != '/':
            path += '/'
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """Return the value  of authorization header"""
        if request is None:
            return None
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """A template that will be used to return the current user"""
        return None
