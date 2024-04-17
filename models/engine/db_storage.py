#!/usr/bin/python3
"""DBStorage engine"""
import os
from sqlalchemy import create_engine
from models.base_model import Base

class DBStorage:
    """database storage engine"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes the SQL database storage"""
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db_name = os.getenv('HBNB_MYSQL_DB')
        env = os.getenv('HBNB_ENV')
        DATABASE_URL = "mysql+mysqldb://{}:{}@{}:3306/{} \
            ".format(user, pwd, host, db_name)
        self.__engine = create_engine(DATABASE_URL,pool_pre_ping=True)
        if env == 'test':
            Base.metadata.drop_all(self.__engine)