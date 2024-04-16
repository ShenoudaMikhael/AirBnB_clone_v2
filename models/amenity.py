#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class Amenity(BaseModel):

    def __init__(self, name, *args, **kwargs):
        """Init new Amenity"""
        super().__init__(**kwargs)
        self.name = name
