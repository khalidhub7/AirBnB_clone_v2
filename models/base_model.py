#!/usr/bin/python3
""" base class for all models in our hbnb clone """
import uuid
from models import storage
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BaseModel(Base):
    """ base class for all hbnb models """
    id = Column(String(60), nullable=False, primary_key=True, unique=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """ Initializes a new model """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at':
                    self.created_at = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == 'updated_at':
                    self.updated_at = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key != '__class__':
                    setattr(self, key, value)

    def __str__(self):
        """ Returns a string representation of the instance """
        class_name = str(type(self)).split(".")[-1].split("'")[0]
        return '[{}] ({}) {}'.format(class_name, self.id, self.__dict__)

    def save(self):
        """ Updates updated_at with current time when instance is changed """
        self.updated_at = datetime.now()
        storage.new(self)  # add the instance to the storage
        storage.save()  # save the changes to the storage

    def to_dict(self):
        """ Convert instance to dict """
        new_dict = self.__dict__.copy()
        class_name = str(type(self)).split('.')[-1].split('\'')[0]
        new_dict['__class__'] = class_name
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        if '_sa_instance_state' in new_dict:
            del new_dict['_sa_instance_state']
        return new_dict

    def delete(self):
        """ Delete current instance from storage """
        storage.delete(self)
