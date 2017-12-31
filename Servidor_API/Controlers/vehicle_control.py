import re
from Models.DAO.vehicle_DAO import VehicleDAO

LICENSE_PLATE_REGEX = re.compile("[A-Z][A-Z][A-Z]\-\d\d\d\d")

class VehicleControl:
    @staticmethod
    def find(id_vehicle):
        try:
            response = VehicleDAO.find(id_vehicle)
            return response
        except Exception as error:
            raise ValueError('Unable to find vehicle: ' + error.message)
        
    @staticmethod
    def register(vehicle):
        VehicleControl.validate_license_plate(vehicle)
        
        try:
            response = VehicleDAO.insert(vehicle)
            return response
        except Exception as error:
            raise ValueError('Unable to register vehicle: ' + error.message)
        
    @staticmethod
    def update(vehicle):
        VehicleControl.validate_license_plate(vehicle)
        
        try:
            if VehicleDAO.update(vehicle) == 1:
                return VehicleDAO.find(vehicle.id)
            else:
                return None
        except Exception as error:
            raise ValueError('Unable to update vehicle: ' + error.message)
    
    @staticmethod
    def delete(id_vehicle):
        try:
            return VehicleDAO.remove(id_vehicle) == 1
        except Exception as error:
            raise ValueError('Unable to remove vehicle: ' + error.message)
    
    @staticmethod
    def validate_license_plate(vehicle):
        if vehicle.licence_plate != None and re.match(LICENSE_PLATE_REGEX, vehicle.licence_plate) == None:
            raise ValueError('Invalid license plate, please use the format AAA-9999')
