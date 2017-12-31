from Models.DB.DB_helper import getSession, Vehicle

class VehicleDAO:
    @staticmethod
    def find(id_vehicle):
        session=getSession()
        
        try:
            vehicle = session.query(Vehicle).get(id_vehicle)
            return vehicle
        except Exception as error:
            raise error
        finally:
            session.close()
    
    @staticmethod
    def insert(vehicle):
        session=getSession()
        
        try:
            session.add(vehicle)
            session.commit()
            session.refresh(vehicle)
        except Exception as error:
            raise error
        finally:
            session.close()

        return vehicle
    
    @staticmethod
    def update(vehicle):
        session=getSession()
        
        try:
            update_dict = {}
            if vehicle.licence_plate != None:
                update_dict[Vehicle.licence_plate] = vehicle.licence_plate
            if vehicle.year != None:
                update_dict[Vehicle.year] = vehicle.year
            if vehicle.model != None:
                update_dict[Vehicle.model] = vehicle.model
            if vehicle.color != None:
                update_dict[Vehicle.color] = vehicle.color
            if vehicle.ready != None:
                update_dict[Vehicle.ready] = vehicle.ready
            if vehicle.volume != None:
                update_dict[Vehicle.ready] = vehicle.volume
                
            updated_rows = session.query(Vehicle).filter(Vehicle.id == vehicle.id).update(update_dict)
            session.commit()
            return updated_rows
        except Exception as error:
            raise error
        finally:
            session.close()

        return vehicle
    
    @staticmethod
    def remove(id_vehicle):
        session=getSession()
        
        try:
            records_deleted = session.query(Vehicle).filter(Vehicle.id == id_vehicle).delete()
            session.commit()
            return records_deleted
        except Exception as error:
            raise error
        finally:
            session.close()
