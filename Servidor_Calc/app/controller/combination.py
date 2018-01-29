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
    min_number_packages = 10

    def join_packages(self, vehicle):
        """Method responsible for the match of the packages."""
        areas = combinationDAO.get_area()
        # service_order = Service_order()
        area = self.choose_area(areas)
        pack_list = []
        available_vol = 0.8 * vehicle['vol']
        available_weight = 0.8 * vehicle['weight']
        count = 0
        # date = datetime(3000, 1, 1)
        # district = self.choose_district(packages, date)
        if(area is not None):
            lista = area["packages"]
            while available_vol > 0 and available_weight > 0 and count < len(lista):
                package = lista[count]
                if (package["volume"] <= available_vol) and (package["weight"] <= available_weight):
                    available_vol -= package["volume"]
                    available_weight -= package["weight"]
                    pack_list.append(package)
                count += 1
            dateNow = datetime.now()
            shipping_date = dateNow.strftime('%d/%m/%Y')
            if (len(pack_list) != 0):
                packageP = pack_list[0]
                finalization_date = packageP["delivery_date"]
                # finalization_date = (dateNow + timedelta(days=2)).strftime('%d/%m/%Y')
                service_order = ServiceOrder(pack_list, shipping_date, finalization_date)

                # service_order.list_package = pack_list
                # service_order.shipping_date = datetime.datetime.today()
                return service_order.get()
            else:
                return {"error": "Lista de pacotes escolhidos está vazia"}
        else:
            return {"error": "Rota pacote retornou JSON nulo, não tem pacotes cadastrados"}

    def choose_area(self, areas):
        cd_lat = -8.017658
        cd_long = -34.944438
        choosen = ""
        distanceP = 99999999999999999999
        for pos in range(len(areas)):
            area = areas[pos]
            lat = area["lat"]
            long = area["long"]
            distance = self.haversine(cd_lat, cd_long, lat, long)
            if (distance < distanceP):
                distanceP = distance
                choosen = area
        return choosen

    def create_micro_region(self, list_packages):
        trash_packages = []
        limit_distance = 5000
        if(len(list_packages) == 0):
            return self.region
        elif(len(list_packages) == 1):
            trash_package = list_packages.pop(0)
            trash_packages.append(trash_package)
            return self.create_micro_region(list_packages)
        elif(len(list_packages) < 10) and self.min_number_packages == 10:
            self.min_number_packages = 1
            return self.create_micro_region(list_packages)
        else:
            old_package = list_packages[0]
            old_address = old_package["address_destiny"]
            center_lat = old_address["lat"]
            center_long = old_address["long"]
            real_distance = 1000
            isAdd = 0
            min_distance = 0
            id_old_pack = {"id": old_package["id"]}
            micro_region = [id_old_pack]
            list_packages.pop(0)
            while (len(micro_region) <= self.min_number_packages) and (real_distance <=  limit_distance) and (len(list_packages) != 0):
                for pos in range(len(list_packages)):
                    package = list_packages[pos]
                    address = package["address_destiny"]
                    lat = address["lat"]
                    long = address["long"]
                    distance = self.haversine(center_lat, center_long, lat, long)
                    print(distance)
                    if (distance <= real_distance):
                        list_packages.pop(pos)
                        id_pack = {"id": package["id"]}
                        micro_region.append(id_pack)
                        isAdd += 1
                if (isAdd == 0):
                    min_distance += 1000
                    if (min_distance == 2000):
                        if (len(micro_region) == 1):
                            trash_packages.append(old_package)
                real_distance += 1000
            area = {"long": center_long, "lat": center_lat, "packages": micro_region, "area_radius": real_distance }
            self.region.append(area)
            return self.create_micro_region(list_packages)

    def create_area(self):
        packages = combinationDAO.get_packages()
        region_create = self.create_micro_region(packages)
        self.region = []
        if (region_create is None):
            print("Região não foi criada")
            print(packages)
            print(region_create)
        else:
            print(region_create)
            for pos in range(len(region_create)):
                area = region_create[pos]
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
