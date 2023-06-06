#!/usr/bin/env python3
"""
A module for user authentication
"""


import bcrypt


def _hash_password(password: str) -> bytes:
    """ method that hashes a password
    """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
