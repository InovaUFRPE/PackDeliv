from Models.DB.DB_helper import getSession, Vehicle
from Models.DAO.DAO_utils import printError,checkType, changeEditedAttr


class VehicleDao():
    def __init__(self):
        pass

    def save(self,vehicle):
        session = getSession()
        checkType('Vehicle',vehicle)
        session.add(vehicle)
        session.commit()
        session.refresh(vehicle)
        session.close()

        return vehicle.id

    def update(self,editedVehicle):
        session = getSession()
        response = False
        try:
            checkType('Vehicle',editedVehicle)
            vehicle = session.query(Vehicle).filter(Vehicle.id == editedVehicle.id).first()
            if vehicle != None:
                vehicle = changeEditedAttr(vehicle,editedVehicle)
                session.add(vehicle)
                session.commit()
                session.close()
                response = True
            else:
                response = False

        except:
            printError()
            response = False

        return response

    def delete(self,id):
        session = getSession()
        try:
            deleted_rows = session.query(Vehicle).filter(Vehicle.id == id).delete()
            session.commit()
            session.close()
            return deleted_rows == 1
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
            return None
