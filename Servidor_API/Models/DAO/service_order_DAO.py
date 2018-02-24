from Models.DB.DB_helper import getSession, ServiceOrder, Delivery
from Models.DAO.DAO_utils import printError,checkType, changeEditedAttr
from random import choice

class ServiceOrderDao():
    def __init__(self):
        pass



    def save(self,service_order):
        session = getSession()
        response = None
        checkType('ServiceOrder',service_order)
        code_list = []
        for delivery in  service_order.deliveries :
            delivery.id_deliveryman = service_order.id_deliveryman
            while True:
                delivery_code = self.generate_code(15)
                if (delivery_code not in code_list) and (session.query(Delivery).filter(Delivery.code == delivery_code).first() == None):
                    delivery.code = delivery_code
                    code_list.append(delivery_code)
                    break
        while True:
            service_code = self.generate_code(10)
            if session.query(ServiceOrder).filter(ServiceOrder.code == service_code).first() == None :
                service_order.code = service_code
                break
        session.add(service_order)
        session.commit()
        session.refresh(service_order)
        session.close()
        return service_order.id

    def update(self,edited_service_order):
        session = getSession()
        response = None
        try:
            checkType('ServiceOrder',edited_service_order)
            service_order=session.query(ServiceOrder).filter(ServiceOrder.id == edited_service_order.id).first()
            if service_order != None:
                service_order=changeEditedAttr(service_order,edited_service_order)
                session.add(service_order)
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
            deleted_rows = session.query(ServiceOrder).filter(ServiceOrder.id == id).delete()
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
                response=session.query(ServiceOrder).all()
                response=[service_order for service_order in response]

            else:
                response=session.query(ServiceOrder).filter(ServiceOrder.id == id).all()
                response=response[0]
            return response
        except:
            printError()
            return None
    def generate_code(self, size):
            caracters = '0123456789abcdefghijklmnopqrstuwvxyz'
            code = ''
            for char in range(size):
                    code += choice(caracters)
            return  code        
