from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker


class CombinationDAO:

    def select_packages(self, position):
        Session = getSession()
        session = Session()
        response = session.query(Package).filter()
