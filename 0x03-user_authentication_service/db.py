#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound

from user import Base, User
from typing import Dict

VALID_FIELDS = ['id', 'email', 'hashed_password',
                'session_id', 'reset_token']


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ Adds a user to a databse and returns the User object
        """
        if not email or not hashed_password:
            return None
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs: Dict) -> User:
        """ Finds a user from the database based on the
        filters supplied as keyword arguments `kwargs`
        """
        result = self._session.query(User).filter_by(**kwargs).first()
        if not result:
            raise NoResultFound
        return result

    def update_user(self, user_id: int, **kwargs: Dict) -> None:
        """ Updates a user's attributes on the database
        """
        user = self.find_user_by(id=user_id)
        for attr, val in kwargs.items():
            if attr not in VALID_FIELDS:
                raise ValueError
            setattr(user, attr, val)
        self._session.commit()
