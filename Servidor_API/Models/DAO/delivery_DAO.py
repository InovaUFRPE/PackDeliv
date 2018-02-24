from Models.DB.DB_helper import getSession, Delivery
from Models.DAO.DAO_utils import printError,checkType, changeEditedAttr
from random import choice


class DeliveryDao():
    def __init__(self):
        pass

    def save(self,delivery):
        session = getSession()
        checkType('Delivery',delivery)
        while True:
            delivery_code = self.generate_code(15)
            if session.query(Delivery).filter(Delivery.code == delivery_code).first() == None:
                break
        delivery.code = delivery_code
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
            deleted_rows = session.query(Delivery).filter(Delivery.id == int(id)).delete()
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
                if self.isInt(id):
                    response=session.query(Delivery).filter(Delivery.id == int(id)).first()
                else:
                    response=session.query(Delivery).filter(Delivery.code == id).first()
            return response
        except:
            printError()
            return None
    def generate_code(self, size):
            caracters = '0123456789abcdefghijklmnopqrstuwvxyz'
            code = 'd'
            for char in range(size):
                    code += choice(caracters)
            return  code

    def isInt(self, x):
        try:
            int(x)
            return True
        except:
            return False