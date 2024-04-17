#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel


class Place(BaseModel):
    """A place to stay"""

    def __init__(
        self,
        city_id="",
        user_id="",
        name="",
        description="",
        number_rooms=0,
        number_bathroom=0,
        max_guest=0,
        price_by_night=0,
        latitude=0.0,
        longitude=0.0,
        amenity_ids=[],
        *args,
        **kwargs
    ):
        """Init function"""
        super().__init__(*args, **kwargs)

        self.city_id = city_id
        self.user_id = user_id
        self.name = name
        self.description = description
        self.number_rooms = number_rooms
        self.number_bathroom = number_bathroom
        self.max_guest = max_guest
        self.price_by_night = price_by_night
        self.latitude = latitude
        self.longitude = longitude
        self.amenity_ids = amenity_ids
