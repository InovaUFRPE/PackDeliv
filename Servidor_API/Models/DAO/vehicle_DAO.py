

from Models.DB.DB_helper import getSession, Vehicle
from Models.DAO.DAO_utils import printError,checkType, changeEditedAttr


class VehicleDAO():

    def __init__(self):
        pass

    def save(self,vehicle):
        session = getSession()
        response = None
        try:
            checkType('Vehicle',vehicle)
            session.add(vehicle)
            session.commit()
            session.refresh(vehicle)
            id=vehicle.id
            session.close()
            response = id

        except:
            printError()
            response = False
        
        return response
    
    def update(self,editedVehicle):
        session = getSession()
        response = None
        try:
            checkType('Vehicle',editedVehicle)
            vehicle=session.query(Vehicle).filter(Vehicle.id == editedVehicle.id).first()
            vehicle=changeEditedAttr(vehicle,editedVehicle)
            session.add(vehicle)
            session.commit()
            session.close()
            response = True

        except:
            printError()
            response = False
        
        return response
    
    def delete(self,id):
        session = getSession()
        try:
            
            session.query(Vehicle).filter(Vehicle.id == id).delete()
            session.commit()
            session.close()
            return True
        except:
            printError()
            return False

    def select(self,id=None):
        session = getSession()
        try:
            if id == None:
                response=session.query(Vehicle).all()
                response=[vehicle for vehicle in response]

            else:
                response=session.query(Vehicle).filter(Vehicle.id == id).all()
                response=response[0]
            return response
        except:
            printError()
            return False    
