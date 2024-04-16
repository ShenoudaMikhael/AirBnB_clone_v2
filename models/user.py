#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """This class defines a user by various attributes"""

    def __init__(
        self, email="",
        password="", first_name="", last_name="", **kwarg
    ):
        """Init new User"""
        super().__init__(**kwarg)
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
