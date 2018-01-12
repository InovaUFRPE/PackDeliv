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
        district = self.choose_district(packages)
        while available_vol > 0 and count < len(district) and available_weight > 0:
            package = district[count]
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

    def choose_district(packages):
        districtNumber = 0
        packageChosen = None
        date = datetime(2000, 1, 1)
        for qtDistrict in range(len(packages)):
            allDistrict = packages[qtDistrict]
            for qtPackage in range(len(allDistrict)):
                package = allDistrict[qtPackage]
                packageFinalDate = allDistrict[qtPackage].final_date
                packageStartDate = allDistrict[qtPackage].start_date
                if packageFinalDate.year < date.year:
                    date = packageFinalDate
                    districtNumber = qtDistrict
                    packageChosen = package
                else:
                    if packageFinalDate.month < date.month:
                        date = packageFinalDate
                        districtNumber = qtDistrict
                        packageChosen = package
                    else:
                        if packageFinalDate.day < date.day:
                            date = packageFinalDate
                            districtNumber = qtDistrict
                            packageChosen = package
                        elif packageFinalDate.day == date.day:
                            startDate = packageChosen.startDate
                            if packageStartDate.year < startDate.year:
                                date = packageFinalDate
                                districtNumber = qtDistrict
                                packageChosen = package
                            else:
                                if packageStartDate.month < startDate.month:
                                    date = packageFinalDate
                                    districtNumber = qtDistrict
                                    packageChosen = package
                                else:
                                    if packageStartDate.day < startDate.day:
                                        date = packageFinalDate
                                        districtNumber = qtDistrict
                                        packageChosen = package
        return packages[districtNumber]
