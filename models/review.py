#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel


class Review(BaseModel):
    """Review classto store review information"""

    def __init__(self, place_id, user_id, text, *args, **kwargs):
        """init new Review"""
        super().__init__(**kwargs)

        self.place_id = place_id
        self.user_id = user_id
        self.text = text
