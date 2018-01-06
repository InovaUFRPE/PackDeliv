
from Models.DB.DB_helper import getSession, Service_order
from Models.DAO.DAO_utils import printError,checkType, changeEditedAttr


class ServiceOrderDao():

    def __init__(self):
        pass

    def save(self,serviceOrder):
        session = getSession()
        response = None
        try:
            checkType('Service_order',serviceOrder)
            session.add(serviceOrder)
            session.commit()
            session.refresh(serviceOrder)
            id=serviceOrder.id
            session.close()
            response = id

        except:
            printError()
            response = False
        
        return response
    
    def update(self,editedServiceOrder):
        session = getSession()
        response = None
        try:
            checkType('Service_order',editedServiceOrder)
            pacserviceOrderkage=session.query(Service_order).filter(Service_order.id == editedServiceOrder.id).first()
            serviceOrder=changeEditedAttr(serviceOrder,editedServiceOrder)
            session.add(serviceOrder)
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
            
            session.query(Service_order).filter(Service_order.id == id).delete()
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
                response=session.query(Service_order).all()
                response=[serviceOrder for serviceOrder in response]

            else:
                response=session.query(Service_order).filter(Service_order.id == id).all()
                response=response[0]
            return response
        except:
            printError()
            return False    
