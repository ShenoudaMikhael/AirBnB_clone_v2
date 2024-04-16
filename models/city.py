#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel


class City(BaseModel):
    """The city class, contains state ID and name"""

    def __init__(self, name, state_id, *args, **kwargs):
        """Init new City """

        super().__init__(**kwargs)
        self.name = name
        self.state_id = state_id
