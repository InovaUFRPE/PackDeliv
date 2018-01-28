#!/usr/bin/python3.5
"""Combination Data Access Object module, create the CombinationDAO class."""

import requests
from app.lib.utils import popular


class CombinationDAO:
    """The DAO class for combination."""

    #def select_packages(self, position):
        #"""Function responsible for the selection of packages from the DB."""
        # data = {}
        # data['position'] = position.get_lat() + "" + position.get_lng()
        # url = 'localhost:5000/select_packages'
        # response = requests.api.post(url, data, json=True)
        #return popular()

    def get_packages(self):
        """Function responsible for the selection of packages from the DB."""
        order_list_package = requests.get("http://localhost:5000/package/")
        return order_list_package

    def send_area(self, area):
        requests.post("http://localhost:5000/area/", area)
