#!/usr/bin/python3
"""DBStorage Module"""
from os import getenv
import urllib.parse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """DBStorage Class"""

    __engine = None
    __session = None

    def __init__(self) -> None:
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(
                getenv("HBNB_MYSQL_USER"),
                urllib.parse.quote_plus(getenv("HBNB_MYSQL_PWD")),
                getenv("HBNB_MYSQL_HOST"),
                getenv("HBNB_MYSQL_DB"),
            ),
            pool_pre_ping=True,
        )
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on curret database"""
        classes = {
            "City": City,
            "State": State,
            "User": User,
            "Place": Place,
            "Review": Review,
            "Amenity": Amenity,
        }
        qr = {}
        query_rows = []

        if cls:

            if type(cls) is str:
                cls = eval(cls)
            query_rows = self.__session.query(cls)
            for row in query_rows:
                k = "{}.{}".format(type(row).__name__, row.id)
                qr[k] = row
            return qr

        for name, value in classes.items():
            query_rows = self.__session.query(value)
            for row in query_rows:
                k = "{}.{}".format(name, row.id)
                qr[k] = row
        return qr

    def new(self, obj):
        """Add obj to database"""

        self.__session.add(obj)

    def save(self):
        """Commit all changes to database"""

        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from database"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in database and initialize new session"""
        Base.metadata.create_all(self.__engine)
        SessionFactory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(SessionFactory)()

    def close(self):
        """Close SQLAlchemy session"""
        self.__session.close()
