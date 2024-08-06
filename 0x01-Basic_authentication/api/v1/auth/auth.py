#!/usr/bin/env python3
"""The Auth class"""
from flask import request
from typing import List, TypeVar


class Auth:
    """A class that performs authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """A template that will be used to check if the path requires auth"""
        return False

    def authorization_header(self, request=None) -> str:
        """A template that will be used to return authorization header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """A template that will be used to return the current user"""
        return None
