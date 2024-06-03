#!/usr/bin/python3
""" holds class State"""
import models
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """Representation of state """
    if models.storage_t == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

    def save(self):
        """saves state instance"""
        models.storage.new(self)
        models.storage.save()

    def delete(self):
        """deletes state instance"""
        models.storage.delete(self)
        models.storage.save()

    if models.storage_t != "db":
        @property
        def cities(self):
            """getter for list of city instances related to the state"""
            return [city for city in models.storage.all(City).values() if city.state_id == self.id]

