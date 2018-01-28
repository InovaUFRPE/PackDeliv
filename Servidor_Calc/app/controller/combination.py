#!/usr/bin/python3.5
"""Combination Controller module, create the controller for combination."""

from app.dao.combination import CombinationDAO
from app.lib.utils import ServiceOrder, Area
from datetime import datetime, timedelta
from math import radians, cos, sin, asin, sqrt

combinationDAO = CombinationDAO()


class CombinationController:
    """The class responsible to control the combination process."""
    region = []

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
        area = self.create_region(packages)
        if(area is not None):
            lista = area.packages
            while available_vol > 0 and count and available_weight > 0:
                package = lista[count]
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
        else:
            return {"error": "Rota pacote retornou JSON nulo, não tem pacotes cadastrados"}

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

    def create_micro_region(self, list_packages):
        trash_packages = []
        min_number_packages = 10
        if(isinstance(list_packages, list)):
            if(len(list_packages) == 0):
                return self.region
            elif(len(list_packages == 1)):
                trash_packages.append(list_packages[0])
                list_packages.pop(0)
            elif(len(list_packages) < 10):
                min_number_packages = 1
            else:
                old_package = list_packages[0]
                old_address = old_package["address_destiny"]
                center_lat = old_address["lat"]
                center_long = old_address["long"]
                real_distance = 1000
                isAdd = 0
                min_distance = 0
                micro_region = [old_package["id"]]
                list_packages.pop(0)
                while (len(micro_region) < min_number_packages) and (real_distance <=  5000) and (len(list_packages) != 0):
                    for pos in range(len(list_packages)):
                        package = list_packages[pos]
                        address = package["address_destiny"]
                        lat = address["lat"]
                        long = address["long"]
                        distance = self.haversine(center_lat, center_long, lat, long)
                        if (distance <= real_distance):
                            list_packages.pop(pos)
                            micro_region.append(package["id"])
                            isAdd += 1
                    if (isAdd == 0):
                        min_distance += 1000
                        if (min_distance == 2000):
                            if (len(micro_region) == 1):
                                trash_packages.append(old_package)
                            else:
                                list_packages.append(old_package)
                    real_distance += 1000

                area = {"long": center_long, "lat": center_long, "packages": micro_region, "area_radius": real_distance }
                self.region.append(area)
                return self.create_micro_region(list_packages)
        else:
            print(type(list_packages))

    def create_area(self):
        packages = combinationDAO.get_packages()
        region = self.create_micro_region(packages)
        self.region = []
        for area in len(region):
            combinationDAO.send_area(area)

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
