#!/usr/bin/python3.5
"""Combination Controller module, create the controller for combination."""
from dao import combination
from utils import LatLng

combinationDAO = combination.CombinationDAO()


class CombinationController:
    """The class responsible to control the combination process."""

    def join_packages(self, vol, position):
        """Method responsible for the match of the packages."""
        packages = combinationDAO.select_packages(position)
