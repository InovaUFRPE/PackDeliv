#!/usr/bin/python3.5
"""Combination Controller module, create the controller for combination."""

import datetime
from dao.combination import CombinationDAO
from model.model import Service_order

combinationDAO = CombinationDAO()


class CombinationController:
    """The class responsible to control the combination process."""

    def join_packages(self, vehicle_vol, position):
        """Method responsible for the match of the packages."""
        packages = combinationDAO.select_packages(position)
        service_order = Service_order()
        pack_list = []
        available_vol = 0.8 * vehicle_vol

        count = 0
        while available_vol > 0 or count < len(packages):
            package = packages[count]
            if package.vol <= available_vol:
                available_vol = available_vol - package.vol
                pack_list.append(package)
            count += 1

        service_order.list_package = pack_list
        service_order.shipping_date = datetime.datetime.today()
        return service_order
