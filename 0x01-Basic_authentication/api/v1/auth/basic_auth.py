#!/usr/bin/env python3
"""The Basic Auth class"""
import binascii
import base64
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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """Return the decoded value of a Base64 string"""
        if (base64_authorization_header is None
                or type(base64_authorization_header) is not str):
            return None
        try:
            return base64.b64decode(base64_authorization_header,
                                    validate=True).decode('utf-8')
        except binascii.Error:
            None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """Extract the username and password"""
        if (decoded_base64_authorization_header is None
                or type(decoded_base64_authorization_header) is not str
                or ':' not in decoded_base64_authorization_header):
            return None, None
        return tuple(decoded_base64_authorization_header.split(':'))
