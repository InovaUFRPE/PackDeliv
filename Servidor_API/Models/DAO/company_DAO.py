from Rest_utils.entities_atributes_Names import *
from Models.DB.DB_helper import getSession
from Models.DAO.DAO_utils import printError

class adressDao():

    def __init__(self):
        session = getSession()

    def save(self,adress):
        try:
            
            self.session.add(adress)
            self.session.commit()
            self.session.refresh(adress)
            id=adress.id
            session.close()
            return id

        except:
            printError()
            return False
    
    def update(self,adress):
        try:
            self.session.add(adress)
            self.session.commit()
            self.session.refresh(adress)
            session.close()
            return True
        except:
            printError()
            return False
    
    def delete(self,id):
        try:
            self.session.query(Adress).filter(Adress.id == id).delete()
            self.session.commit()
            self.session.close()
            return True
        except:
            printError()
            return False

    def select(self,id=None):
        try:
            if id == None:
                response=self.session.query(Adress).all()
            else:
                response=self.session.query(Adress).filter(Adress.id == id).all()
                adress=response[0]
            return adress
        except:
            printError()
            return False