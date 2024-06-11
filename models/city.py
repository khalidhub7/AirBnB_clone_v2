#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class City(BaseModel, Base):
    """ The city class, contains state ID and name
    Update City for sqlalchemy"""
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

    """ the next line mean:
     city obj can associated with mutiple places 
     (one-to-many relationship) """
    places = relationship("Place", backref='cities', cascade='delete')
