#!/usr/bin/env python3
"""The Basic Auth class"""
from .auth import Auth


class BasicAuth(Auth):
    """A class that performs basic authentication"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Return the Base64 part of the Authorization header"""
        if (authorization_header is None
                or type(authorization_header) is not str):
            return None
        fields = authorization_header.split()
        if fields[0] != 'Basic':
            return None
        return fields[1]
