#!/usr/bin/python3.5
"""Combination Controller module, create the controller for combination."""

from app.dao.combination import CombinationDAO
from app.lib.utils import ServiceOrder
from datetime import datetime, timedelta

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
        date = datetime(3000, 1, 1)
        district = self.choose_district(packages, date)
        while available_vol > 0 and count < len(district) and available_weight > 0:
            package = district[count]
            if (package.vol <= available_vol) and (package.weight <= available_weight):
                available_vol -= package.vol
                available_weight -= package.weight
                pack_list.append(package.get())
            count += 1
        dateNow = datetime.now()
        shipping_date = dateNow.strftime('%d/%m/%Y')
        finalization_date = (dateNow + timedelta(days=2)).strftime('%d/%m/%Y')
        service_order = ServiceOrder(pack_list, shipping_date, finalization_date)

        # service_order.list_package = pack_list
        # service_order.shipping_date = datetime.datetime.today()
        return service_order.get()

    def choose_district(self, packages, date):
        print(date)
        newKey = 'bairro3'
        for key, value in packages.items():
            districtKey = newKey
            allDistrict = value
            for qtPackage in range(len(allDistrict)):
                packageFinalDate = allDistrict[qtPackage].final_date
                if packageFinalDate.year < date.year:
                    districtKey = key
                    if packageFinalDate.month < date.month:
                        districtKey = key
                        if packageFinalDate.day < date.day:
                            date = packageFinalDate
                            districtKey = key
        return packages[districtKey]
