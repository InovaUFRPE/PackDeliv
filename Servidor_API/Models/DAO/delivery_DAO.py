

from Models.DB.DB_helper import getSession, Delivery
from Models.DAO.DAO_utils import printError,checkType, changeEditedAttr


class DeliveryDao():

    def __init__(self):
        pass

    def save(self,delivery):
        session = getSession()
        response = None
        try:
            checkType('Delivery',delivery)    
            session.add(delivery)
            session.commit()
            session.refresh(delivery)
            id=adress.id
            session.close()
            response = id

        except:
            printError()
            response = False
        
        return response
    
    def update(self,editedDelivery):
        session = getSession()
        response = None
        try:
            checkType('Delivery',editedDelivery)
            delivery=session.query(Delivery).filter(Delivery.id == editedDelivery.id).first()
            delivery=changeEditedAttr(delivery,editedDelivery)
            session.add(delivery)
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
            checkType('Delivery',delivery)
            self.session.query(Delivery).filter(Delivery.id == id).delete()
            self.session.commit()
            self.session.close()
            return True
        except:
            printError()
            return False

    def select(self,id=None):
        session = getSession()
        try:
            if id == None:
                response=self.session.query(Delivery).all()
                response=[delivery for delivery in response]

            else:
                response=self.session.query(Delivery).filter(Delivery.id == id).all()
                response=response[0]
            return response
        except:
            printError()
            return False    
