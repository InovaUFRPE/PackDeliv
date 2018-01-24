#!/usr/bin/python3.5
"""Combination Controller module, create the controller for combination."""

from app.dao.combination import CombinationDAO
from app.lib.utils import ServiceOrder, Area
from datetime import datetime, timedelta
from math import radians, cos, sin, asin, sqrt

combinationDAO = CombinationDAO()


class CombinationController:
    """The class responsible to control the combination process."""

    def join_packages(self, vehicle):
        """Method responsible for the match of the packages."""
        packages = combinationDAO.get_packages()
        # service_order = Service_order()
        pack_list = []
        available_vol = 0.8 * vehicle['vol']
        available_weight = 0.8 * vehicle['weight']
        count = 0
        # date = datetime(3000, 1, 1)
        # district = self.choose_district(packages, date)
        while available_vol > 0 and count and available_weight > 0:
            package = packages[count]
            if (package.vol <= available_vol) and (package.weight <= available_weight):
                available_vol -= package.volume
                available_weight -= package.weight
                pack_list.append(package)
            count += 1
        dateNow = datetime.now()
        shipping_date = dateNow.strftime('%d/%m/%Y')
        finalization_date = pack_list[0].delivery_date
        # finalization_date = (dateNow + timedelta(days=2)).strftime('%d/%m/%Y')
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

    def create_region(self, list_packages):
        old_package = list_packages[0]
        old_address = old_package.address_destiny
        center_lat = old_address.lat
        center_long = old_address.long
        minimum_distance = 1000
        region = [old_package]
        list_packages.pop(0)
        while len(region) < 10 and minimum_distance < 11000:
            for pos in range(len(list_packages)):
                package = list_packages[pos]
                address = package.address_destiny
                lat = address.lat
                long = address.long
                distance = self.haversine(center_lat, center_long, lat, long)
                if (distance <= minimum_distance):
                    list_packages.pop(pos)
                    region.append(package)
            minimum_distance += 3000
        area = Area(region, center_lat, center_long, minimum_distance)
        return area.get()

    def haversine(self, lat1, lon1, lat2, lon2):
        # convert decimal degrees to radians

        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

        # haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        constant = 2 * asin(sqrt(a))
        radius_earth = 6371
        distance = (constant * radius_earth) * 1000
        return distance
