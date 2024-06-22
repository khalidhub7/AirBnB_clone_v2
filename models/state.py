#!/usr/bin/python3
"""State model for Airbnb project"""
import os
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel


class State(BaseModel, Base):
    """State class"""
    __tablename__ = 'states'
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship(
            'City',
            backref='state',
            cascade='all, delete-orphan'
        )
    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        name = ''

        @property
        def cities(self):
            from models import storage
            all_cities = storage.all("City").values()
            list_cities = []

            for city in all_cities:
                if city.state_id == self.id:
                    list_cities.append(city)
            return list_cities
