#!/usr/bin/python3.5
"""Combination Controller module, create the controller for combination."""

from app.dao.combination import CombinationDAO
from app.lib.utils import ServiceOrder
from datetime import datetime

combinationDAO = CombinationDAO()


class CombinationController:
    """The class responsible to control the combination process."""

    def join_packages(self, vehicle):
        """Method responsible for the match of the packages."""
        packages = combinationDAO.select_packages(vehicle['position'])
        # service_order = Service_order()
        pack_list = []
        available_vol = 0.8 * vehicle['vol']
        available_weight = 0.8 * vehicle['weight']

        count = 0
        while available_vol > 0 and count < len(packages['bairro1']) and available_weight > 0:
            package = packages['bairro1'][count]
            # pprint(pack_list)
            if (package.vol <= available_vol) and (package.weight <= available_weight):
                available_vol -= package.vol
                available_weight -= package.weight
                pack_list.append(package.get())
            count += 1
        dateNow = datetime.now()
        shipping_date = str(dateNow.day) + "/" + str(dateNow.month) + "/" + str(dateNow.year)
        finalization_date = str(dateNow.day + 2) + "/" + str(dateNow.month) + "/" + str(dateNow.year)
        service_order = ServiceOrder(pack_list, shipping_date, finalization_date)

        # service_order.list_package = pack_list
        # service_order.shipping_date = datetime.datetime.today()
        return service_order.get()
