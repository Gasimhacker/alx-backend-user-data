#!/usr/bin/env python3
"""Create a hash of the current password"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """Hash a password"""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
