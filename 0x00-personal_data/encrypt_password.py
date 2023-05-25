#!/usr/bin/env python3
'''
A module for encrypting passwords
'''


import bcrypt


def hash_password(password: str) -> bytes:
    '''method that hashes password'''
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    '''method that compares a hashed password and a given password'''
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
