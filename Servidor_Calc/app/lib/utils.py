#!/usr/bin/python3.5
"""Library for utilities functions for the calc server."""

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def getEngine():
    """Create and return the engine."""
    user = "root"
    password = ""
    adress = "localhost"
    database_name = "packDeliv"
    engine = create_engine('mysql+pymysql://%s:%s@%s/%s' % (user, password, adress, database_name), echo=True)
    return engine


def getSession():
    """Return sessionmaker object."""
    engine = getEngine()
    return sessionmaker(bind=engine)


class LatLng:
    """Class for use with coordinates."""

    def __init__(self, lat, lng):
        """Init the LatLng object."""
        self.__lat = int(lat)
        self.__lng = int(lng)

    def get_lat(self):
        """Get latitude value."""
        return self.__lat

    def get_lng(self):
        """Get longitude value."""
        return self.__lng
