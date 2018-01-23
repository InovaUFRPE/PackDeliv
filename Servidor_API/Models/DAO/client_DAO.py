from Models.DB.DB_helper import getSession,Client
from Models.DAO.DAO_utils import printError,checkType, changeEditedAttr

class ClientDao():
    def __init__(self):
        pass

    def save(self,client):
        session = getSession()
        checkType('Client',client)
        session.add(client)
        session.commit()
        session.refresh(client)
        id=client.id
        session.close()
        return client.id

    def update(self,editedClient):
        session = getSession()
        response = None
        try:
            checkType('Client',editedClient)
            client=session.query(Client).filter(Client.id == editedClient.id).first()
            if client != None:
                client=changeEditedAttr(client,editedClient)
                session.add(client)
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
            deleted_rows = session.query(Client).filter(Client.id == id).delete()
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
                response=session.query(Client).all()
                response=[client for client in response]
            else:
                response=session.query(Client).filter(Client.upi == id).all()
                response=response[0]
            return response
        except:
            printError()
            return None
