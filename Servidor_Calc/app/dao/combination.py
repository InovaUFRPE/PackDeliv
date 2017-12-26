#!/usr/bin/python3.5
"""Combination Data Access Object module, create the CombinationDAO class."""

# SQLAlchemy related imports
from lib.utils import getSession


class CombinationDAO:
    """The DAO class for combination."""

    def select_packages(self, position):
        """Function responsible for the selection of packages from the DB."""
        Session = getSession()
        session = Session()
        response = session.query(Package).filter()
