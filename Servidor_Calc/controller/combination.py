#!/usr/bin/python3.5

from dao import combination
from utils import LatLng

combinationDAO = combination.CombinationDAO()

class CombinationController:

    def join_packages(self, vol, position):
        packages = combinationDAO.select_packages(position)
        
