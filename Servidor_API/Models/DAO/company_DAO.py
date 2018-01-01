
from Models.DB.DB_helper import getSession,Company
from Models.DAO.DAO_utils import printError,checkType


class CompanyDao():

    def __init__(self):
        pass

    def save(self,company):
        session = getSession()
        response = None
        try:
            checkType('Company',company)
            session.add(company)
            session.commit()
            session.refresh(company)
            id=company.id
            session.close()
            response = id

        except:
            printError()
            response = False
        
        return response
    
    def update(self,company):
        session = getSession()
        response = None
        try:
            checkType('Company',company)
            session.add(company)
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
            session.query(Company).filter(Company.id == id).delete()
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
                response=session.query(Company).all()
                response=[company for company in response]
            else:
                response=session.query(Company).filter(Company.id == id).all()
                response=response[0]
            return response
        except:
            printError()
            return False 