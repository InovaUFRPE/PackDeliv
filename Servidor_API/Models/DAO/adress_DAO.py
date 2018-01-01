
from Models.DB.DB_helper import getSession,Adress
from Models.DAO.DAO_utils import printError,checkType


class AdressDao():

    def __init__(self):
        pass

    def save(self,adress):
        session = getSession()
        response = None
        try:
            checkType('Adress',adress)
            session.add(adress)
            session.commit()
            session.refresh(adress)
            id=adress.id
            session.close()
            response = id

        except:
            printError()
            response = False
        
        return response
    
    def update(self,adress):
        session = getSession()
        response = None
        try:
            checkType('Adress',adress)
            session.add(adress)
            print(adress)
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
            checkType('Adress',adress)
            session.query(Adress).filter(Adress.id == id).delete()
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
                response=session.query(Adress).all()
                response=[adress for adress in response]
            else:
                response=session.query(Adress).filter(Adress.id == id).all()
                response=response[0]
            return response
        except:
            printError()
            return False    
