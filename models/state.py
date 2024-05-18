#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base, Column, String


class State(BaseModel, Base):
    """State class"""

    __tablename__ = "states"

    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
        name = ""

        @property
        def cities(self):
            """Get list of cities for this state"""
            from models import storage
            from models.city import City

            cities = []
            city_dict = storage.all(City)

            for city in city_dict.values():
                if city.state_id == self.id:
                    cities.append(city)
            return cities
