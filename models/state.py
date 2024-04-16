#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class State(BaseModel):
    """State class"""

    name = ""

    def __init__(self, name, **kwargs):
        super().__init__(**kwargs)
        self.name = name
