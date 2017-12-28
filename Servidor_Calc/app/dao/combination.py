#!/usr/bin/python3.5
"""Combination Data Access Object module, create the CombinationDAO class."""

# import requests
from lib.utils import popular


class CombinationDAO:
    """The DAO class for combination."""

    def select_packages(self, position):
        """Function responsible for the selection of packages from the DB."""
        # data = {}
        # data['position'] = position.get_lat() + "" + position.get_lng()
        # url = 'localhost:5000/select_packages'
        # response = requests.api.post(url, data, json=True)
        return popular()
