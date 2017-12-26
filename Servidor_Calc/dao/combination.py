#!/usr/bin/python3.5
"""Combination Data Access Object module, create the CombinationDAO class."""
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker


class CombinationDAO:
    """The DAO class for combination."""

    def select_packages(self, position):
        """Function responsible for the selection of packages from the DB."""
        Session = getSession()
        session = Session()
        response = session.query(Package).filter()
