from Models.DB.DB_helper import getSession, Package
from Models.DAO.DAO_utils import printError,checkType, changeEditedAttr

class PackageDao():
    def __init__(self):
        pass

    def save(self,package):
        session = getSession()
        checkType('Package',package)
        session.add(package)
        session.commit()
        session.refresh(package)
        session.close()
        return package.id

    def update(self,editedPackage):
        session = getSession()
        response = None
        try:
            checkType('Package',editedPackage)
            package=session.query(Package).filter(Package.id == editedPackage.id).first()
            if package != None:
                package=changeEditedAttr(package,editedPackage)
                session.add(package)
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
            deleted_rows = session.query(Package).filter(Package.id == id).delete()
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
                response=session.query(Package).all()
                response=[package for package in response]
            else:
                response=session.query(Package).filter(Package.id == id).all()
                response=response[0]
            return response
        except:
            printError()
            return None
