#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import ForeignKey
from models.base_model import BaseModel, Column, String, Base


class City(BaseModel, Base):
    """The city class, contains state ID and name"""

    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)

    def __init__(self, *args, state_id="", name="", **kwargs):
        """Init function"""
        super().__init__(*args, **kwargs)
        self.state_id = state_id
        self.name = name
