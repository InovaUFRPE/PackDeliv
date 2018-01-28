import re, bcrypt
from Models.DAO.client_DAO import ClientDao
from Models.DAO.DAO_utils import printError

NAME_MINIMUM_LENGTH = 3
UPI_EXACT_LENGTH = 11
UPI_REGEX = re.compile("[0-9]{11}")

dao = ClientDao()

class ClientControl:
    @staticmethod
    def find(id_client):
        try:
            response = dao.select(id_client)
            return response
        except Exception as error:
            raise ValueError('Unable to find client: ' + str(error))

    @staticmethod
    def register(client):
        ClientControl.validate(client)

        try:
            id_client = dao.save(client)
            return id_client
        except Exception as error:
            printError()
            raise ValueError('Unable to register client: ' + str(error))

    @staticmethod
    def update(client):
        ClientControl.validate(client)

        try:
            success = dao.update(client)
            return success
        except Exception as error:
            raise ValueError('Unable to update client: ' + str(error))

    @staticmethod
    def delete(id_client):
        try:
            success = dao.delete(id_client)
            return success
        except Exception as error:
            raise ValueError('Unable to remove client: ' + str(error))

    @staticmethod
    def validate(client):
        ClientControl.validate_name(client)
        ClientControl.validate_upi(client)

    @staticmethod
    def validate_name(client):
        if client.name != None and len(client.name) < NAME_MINIMUM_LENGTH:
            raise ValueError('Invalid name, please use one with at least ' + str(NAME_MINIMUM_LENGTH) + ' characters')

    @staticmethod
    def validate_upi(client):
        if client.upi != None:
            if len(client.upi) < UPI_EXACT_LENGTH:
                raise ValueError('Invalid upi, please use one with exactly ' + str(UPI_EXACT_LENGTH) + ' digits')
            if re.match(UPI_REGEX, client.upi) == None:
                raise ValueError('Invalid upi, please use only digits')
