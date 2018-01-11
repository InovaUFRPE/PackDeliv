import re
from Models.DAO.vehicle_DAO import VehicleDao

LICENSE_PLATE_REGEX = re.compile("[A-Z][A-Z][A-Z]\-\d\d\d\d")
dao = VehicleDao()

class VehicleControl:
    @staticmethod
    def find(id_vehicle):
        try:
            response = dao.select(id_vehicle)
            return response
        except Exception as error:
            raise ValueError('Unable to find vehicle: ' + str(error))

    @staticmethod
    def register(vehicle):
        VehicleControl.validate_license_plate(vehicle)

        try:
            id_vehicle = dao.save(vehicle)
            return id_vehicle
        except Exception as error:
            raise ValueError('Unable to register vehicle: ' + str(error))

    @staticmethod
    def update(vehicle):
        VehicleControl.validate_license_plate(vehicle)

        try:
            success = dao.update(vehicle)
            return success
        except Exception as error:
            raise ValueError('Unable to update vehicle: ' + str(error))

    @staticmethod
    def delete(id_vehicle):
        try:
            success = dao.delete(id_vehicle)
            return success
        except Exception as error:
            raise ValueError('Unable to remove vehicle: ' + str(error))

    @staticmethod
    def validate_license_plate(vehicle):
        if vehicle.licence_plate != None and re.match(LICENSE_PLATE_REGEX, vehicle.licence_plate) == None:
            raise ValueError('Invalid license plate, please use the format AAA-9999')
