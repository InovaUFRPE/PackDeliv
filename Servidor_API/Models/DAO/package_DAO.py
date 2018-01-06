

from Models.DB.DB_helper import getSession, Package
from Models.DAO.DAO_utils import printError,checkType, changeEditedAttr


class PackageDao():

    def __init__(self):
        pass

    def save(self,package):
        session = getSession()
        response = None
        try:
            checkType('Package',package)

            session.add(package)
            session.commit()
            session.refresh(package)
            id=package.id
            session.close()
            response = id

        except:
            printError()
            response = False
        
        return response
    
    def update(self,editedPackage):
        session = getSession()
        response = None
        try:
            checkType('Package',editedPackage)
            package=session.query(Package).filter(Package.id == editedPackage.id).first()
            package=changeEditedAttr(package,editedPackage)
            session.add(package)
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
            checkType('Package',package)
            session.query(Package).filter(Package.id == id).delete()
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
                response=session.query(Package).all()
                response=[package for package in response]

            else:
                response=session.query(Package).filter(Package.id == id).all()
                response=response[0]
            return response
        except:
            printError()
            return False    
