

from Models.DB.DB_helper import getSession, Deliveryman
from Models.DAO.DAO_utils import printError,checkType, changeEditedAttr


class DeliverymanDao():

    def __init__(self):
        pass
    def save(self,deliveryman):
        session = getSession()
        response = None
        try:
            checkType('Deliveryman',deliveryman)
            
            session.add(deliveryman)
            session.commit()
            session.refresh(deliveryman)
            id=deliveryman.id
            session.close()
            response = id

        except:
            printError()
            response = False
        
        return response
    
    def update(self,editedDeliveryman):
        session = getSession()
        response = None
        try:
            checkType('Deliveryman',editedDeliveryman)
            deliveryman=session.query(Deliveryman).filter(Deliveryman.id == editedDeliveryman.id).first()
            deliveryman=changeEditedAttr(deliveryman,editedDeliveryman)
            session.add(deliveryman)
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
            checkType('Deliveryman',deliveryman)
            session.query(Deliveryman).filter(Deliveryman.id == id).delete()
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
                response=session.query(Deliveryman).all()
                response=[deliveryman for deliveryman in response]

            else:
                response=session.query(Deliveryman).filter(Deliveryman.id == id).all()
                response=response[0]
            return response
        except:
            printError()
            return False    
