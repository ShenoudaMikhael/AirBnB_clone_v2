#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """This class defines a Amenity by various attributes"""

    def __init__(self, *args, name="", **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
