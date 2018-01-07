from Models.DB.DB_helper import getSession,Address
from Models.DAO.DAO_utils import printError,checkType, changeEditedAttr


class AddressDao():
    def __init__(self):
        pass

    def save(self,address):
        session = getSession()
        checkType('Address',address)
        session.add(address)
        session.commit()
        session.refresh(address)
        session.close()
        return address.id

    def update(self,editedAddress):
        session = getSession()
        response = None
        try:
            checkType('Address',editedAddress)
            address=session.query(Address).filter(Address.id == editedAddress.id).first()
            if address != None:
                address=changeEditedAttr(address,editedAddress)
                session.add(address)

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
            delete_rows = session.query(Address).filter(Address.id == id).delete()
            session.commit()
            session.close()
            return delete_rows == 1
        except:
            printError()
            return False

    def select(self,id=None):
        session = getSession()
        try:
            if id == None:
                response=session.query(Address).all()
                response=[address for address in response]
            else:
                response=session.query(Address).filter(Address.id == id).all()
                response=response[0]
            return response
        except:
            printError()
            return None
