#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """This class defines a user by various attributes"""

    email = ("",)
    password = ("",)
    first_name = ("",)
    last_name = ("",)

    def __init__(
        self, *args, email="",
        password="", first_name="", last_name="", **kwargs
    ):

        super().__init__(*args, **kwargs)
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
