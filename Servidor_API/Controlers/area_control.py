from Models.DAO.area_DAO import AreaDao
from Models.DAO.DAO_utils import printError
from Models.DB.DB_helper import Area
from Controlers.deliveryman_control import DeliverymanControl
from Controlers.package_control import PackageControl

AREA_RADIUS_MINIMUM_VALUE = 1 # metro
AREA_RADIUS_MAXIMUM_VALUE = 5000 # metros

dao = AreaDao()

class AreaControl:
    @staticmethod
    def find(id_area):
        try:
            response = dao.select(id_area)
            return response
        except Exception as error:
            raise ValueError('Unable to find area: ' + str(error))

    @staticmethod
    def register(area):
        AreaControl.validate(area)

        try:
            id_area = dao.save(area)

            return id_area
        except Exception as error:
            printError()
            raise ValueError('Unable to register area: ' + str(error))

    @staticmethod
    def update(area):
        AreaControl.validate(area)

        try:
            success = dao.update(area)

            return success
        except Exception as error:
            raise ValueError('Unable to update area: ' + str(error))

    @staticmethod
    def delete(id_area):
        try:
            success = dao.delete(id_area)
            return success
        except Exception as error:
            raise ValueError('Unable to remove area: ' + str(error))

    @staticmethod
    def validate(area):
        DeliverymanControl.validate_lat(area)
        DeliverymanControl.validate_long(area)
        AreaControl.validate_area_radius(area)
        AreaControl.validate_packages(area)

    @staticmethod
    def validate_area_radius(area):
        if area.area_radius != None and (area.area_radius < AREA_RADIUS_MINIMUM_VALUE or area.area_radius > AREA_RADIUS_MAXIMUM_VALUE):
            raise ValueError('Invalid area_radius, please use one within the range of ' + str(AREA_RADIUS_MINIMUM_VALUE) + ' to ' + str(AREA_RADIUS_MAXIMUM_VALUE))

    @staticmethod
    def validate_packages(area):
        # A verificacao do id de area é para checar se o objeto esta sendo criado ou atualizado
        if area.packages != None and area.id == None and len(area.packages) == 0:
            raise ValueError('Invalid packages, please provide at least one')

        for package in area.packages:
            PackageControl.validate(package)
