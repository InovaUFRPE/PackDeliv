from Models.DB.DB_helper import getSession,Company
from Models.DAO.DAO_utils import printError,checkType, changeEditedAttr

class CompanyDao():
    def __init__(self):
        pass

    def save(self,company):
        session = getSession()
        checkType('Company',company)
        session.add(company)
        session.commit()
        session.refresh(company)
        session.close()

        return company.id

    def update(self,editedCompany):
        session = getSession()
        response = None
        try:
            checkType('Company',editedCompany)
            company=session.query(Company).filter(Company.id == editedCompany.id).first()
            if company != None:
                company=changeEditedAttr(company,editedCompany)
                session.add(company)
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
            deleted_rows = session.query(Company).filter(Company.id == id).delete()
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
                response=session.query(Company).all()
                response=[company for company in response]
            else:
                response=session.query(Company).filter(Company.id == id).all()
                response=response[0]
            return response
        except:
            printError()
            return None
