#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class Amenity(BaseModel):

    def __init__(self, *args, name="", **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
