#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel


class Review(BaseModel):
    """Review classto store review information"""

    def __init__(self, *args, place_id="", user_id="", text="", **kwargs):
        """Init function"""
        super().__init__(*args, **kwargs)

        self.place_id = place_id
        self.user_id = user_id
        self.text = text
