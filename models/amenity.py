#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base, Column, String
from models.place import place_amenity


class Amenity(BaseModel, Base):
    """This class defines a Amenity by various attributes"""

    __tablename__ = "amenities"

    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity)
