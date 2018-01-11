from Models.DAO.address_DAO import AddressDao
from Models.DAO.DAO_utils import printError
from Models.DB.DB_helper import Address
from Controlers.deliveryman_control import DeliverymanControl

dao = AddressDao()

class AddressControl:
    @staticmethod
    def find(id_address):
        try:
            response = dao.select(id_address)
            return response
        except Exception as error:
            raise ValueError('Unable to find address: ' + str(error))

    @staticmethod
    def register(address):
        AddressControl.validate(address)

        try:
            id_address = dao.save(address)

            return id_address
        except Exception as error:
            printError()
            raise ValueError('Unable to register address: ' + str(error))

    @staticmethod
    def update(address):
        AddressControl.validate(address)

        try:
            success = dao.update(address)
            return success
        except Exception as error:
            raise ValueError('Unable to update address: ' + str(error))

    @staticmethod
    def delete(id_address):
        try:
            success = dao.delete(id_address)
            return success
        except Exception as error:
            raise ValueError('Unable to remove address: ' + str(error))

    @staticmethod
    def validate(address):
        DeliverymanControl.validate_lat(address)
        DeliverymanControl.validate_long(address)
        AddressControl.validate_and_update_type(address)

    @staticmethod
    def validate_and_update_type(address):
        if address.type.__class__ == int:
            try:
                address.type = Address.AddressType(address.type)
            except ValueError:
                raise ValueError('Invalid type, please use one of the options: ' + str([e.value for e in Address.AddressType]))
