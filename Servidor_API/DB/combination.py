from DB.DB_helper import *
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from Rest_utils.entities_atributes_Names import *

class LatLng:
    """docstring for LatLng."""
    def __init__(self, lat, lng):
        self.__lat = int(lat)
        self.__lng = int(lng)

    def get_lat(self):
        return self.__lat

    def get_lng(self):
        return self.__lng


class CombinationController:

    def join_packages(self, vol, position):
        combinationDAO = CombinationDAO()
        packages = combinationDAO.select_packages(position)
        volInicial = vol
        service_order = Service_order()
        pack_list = []

        for package in packages:
            volPackage = package.width * package.height * package.lenght
            if vol == 0:
                break
            elif volPackage <= vol:
                vol = vol - volPackage
                pack_list.append(package)

        else:
            service_order.list_package = pack_list
            service_order.shipping_date = datetime.datetime.today()
            return service_order


class CombinationDAO:

    def select_packages(self, position):
        Session = getSession()
        session = Session()
        packages = session.query(Package).group_by(Package.id_adress_start).order_by(asc(Package.started_date)).all()
        return packages
