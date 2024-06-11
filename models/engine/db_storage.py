#!/usr/bin/python3
""" DBStorage(sqlalchemy) """
import models
import sqlalchemy
from os import getenv
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import create_engine
from models.base_model import BaseModel, Base
from sqlalchemy.orm import scoped_session, sessionmaker
classes = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "State": State, "User": User}


class DBStorage:
    """ interacts with the MySQL database """
    __engine = None
    __session = None

    def __init__(self):
        """ initializing """
        HBNB_ENV = getenv('HBNB_ENV')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_TYPE_STORAGE = getenv('HBNB_TYPE_STORAGE')
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                HBNB_MYSQL_USER,
                HBNB_MYSQL_PWD,
                HBNB_MYSQL_HOST,
                HBNB_MYSQL_DB),
            pool_pre_ping=True)

        if HBNB_ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ retieve current database session """
        new_dict = {}
        for i in classes:
            if cls is None or cls is classes[i] or cls is i:
                all_obj = self.__session.query(classes[i]).all()
                for obj in all_obj:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """ add obj in current database """
        self.__session.add(obj)

    def save(self):
        """ commit changes """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete obj in current database """
        if obj is None:
            return
        self.__session.delete(obj)

    def reload(self):
        """ reload data in current database """
        # create all tables in the classes like User, Place
        Base.metadata.create_all(self.__engine)
        # create temporary session to add or update or something
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        # this is used to avoid conflicts because a lot of users can making
        # sessions requests
        Sess = scoped_session(session_factory)
        self.__session = Sess

    def close(self):
        """ Close current working SQLAlchemy session """
        self.__session.remove()
