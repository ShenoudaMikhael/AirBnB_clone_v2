#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base, Column, String


class Amenity(BaseModel, Base):
    """This class defines a Amenity by various attributes"""

    __tablename__ = "amenities"

    name = Column(String(128), nullable=False)
