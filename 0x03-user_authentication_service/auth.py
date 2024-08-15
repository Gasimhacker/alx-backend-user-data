#!/usr/bin/env python3
"""Create a hash of the current password"""
import bcrypt
from db import DB
from user import User
from uuid import uuid4
from sqlalchemy.orm.exc import NoResultFound


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user in the database"""
        try:
            u = self._db.find_user_by(email=email)
            raise ValueError(f'User {email} already exists')
        except NoResultFound:
            password = _hash_password(password)
            u = self._db.add_user(email, password)
            return u

    def valid_login(self, email: str, password: str) -> bool:
        """Check if a user with there credentials exists"""
        try:
            u = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode(), u.hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """Create a session for this user"""
        try:
            u = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(u.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None


def _generate_uuid() -> str:
    """Generate a string representation of a new UUID"""
    return str(uuid4())


def _hash_password(password: str) -> bytes:
    """Hash a password"""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
