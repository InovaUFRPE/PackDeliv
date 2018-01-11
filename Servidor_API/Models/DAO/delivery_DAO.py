from Models.DB.DB_helper import getSession, Delivery
from Models.DAO.DAO_utils import printError,checkType, changeEditedAttr

class DeliveryDao():
    def __init__(self):
        pass

    def save(self,delivery):
        session = getSession()
        checkType('Delivery',delivery)
        session.add(delivery)
        session.commit()
        session.refresh(delivery)
        session.close()
        return delivery.id

    def update(self,editedDelivery):
        session = getSession()
        response = None
        try:
            checkType('Delivery',editedDelivery)
            delivery=session.query(Delivery).filter(Delivery.id == editedDelivery.id).first()
            if delivery != None:
                delivery=changeEditedAttr(delivery,editedDelivery)
                session.add(delivery)
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
            deleted_rows = session.query(Delivery).filter(Delivery.id == id).delete()
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
                response=session.query(Delivery).all()
                response=[delivery for delivery in response]

            else:
                response=session.query(Delivery).filter(Delivery.id == id).all()
                response=response[0]
            return response
        except:
            printError()
            return None
