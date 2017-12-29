#!/usr/bin/python3.5
"""Combination Controller module, create the controller for combination."""

from app.dao.combination import CombinationDAO

combinationDAO = CombinationDAO()


class CombinationController:
    """The class responsible to control the combination process."""

    def join_packages(self, vehicle):
        """Method responsible for the match of the packages."""
        packages = combinationDAO.select_packages(vehicle['position'])
        # service_order = Service_order()
        pack_list = {}
        available_vol = 0.8 * vehicle['vol']
        available_weight = 0.8 * vehicle['weight']

        count = 0
        while available_vol > 0 and count < len(packages['bairro1']) and available_weight > 0:
            package = packages['bairro1'][count]
            # pprint(pack_list)
            if (package.vol <= available_vol) and (package.weight <= available_weight):
                available_vol -= package.vol
                available_weight -= package.weight
                pack_list[package.id] = package.get()
            count += 1

        # service_order.list_package = pack_list
        # service_order.shipping_date = datetime.datetime.today()
        return pack_list
