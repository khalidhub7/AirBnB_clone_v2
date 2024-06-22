#!/usr/bin/python3
""" City class """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name
    Update City for sqlalchemy"""
    __tablename__ = "cities"
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship('Place', backref="cities",
                              cascade="all, delete-orphan")
    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        name = ""
        state_id = ""
