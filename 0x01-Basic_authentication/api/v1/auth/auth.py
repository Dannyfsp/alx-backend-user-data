#!/usr/bin/env python3
"""
Authentication module to manage the API
"""


from flask import request
from typing import List, TypeVar


class Auth:
    """ class to manage the API authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ function that checks if a pth requires authentication
        """
        return False

    def authorization_header(self, request=None) -> str:
        """ method to get the authorization header field from the request
        """
        return None

    def current_user(self, request=None) -> TypeVar('Users'):
        """ method that gets current user from the request
        """
        return None
