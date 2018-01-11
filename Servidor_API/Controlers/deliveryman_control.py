import re, bcrypt
from Models.DAO.deliveryman_DAO import DeliverymanDao
from Models.DAO.DAO_utils import printError
from Controlers.company_control import CompanyControl

NAME_MINIMUM_LENGTH = 6
DUI_MINIMUM_LENGTH = 6
LAT_MINIMUM_VALUE = -90.0
LAT_MAXIMUM_VALUE = 90.0
LONG_MINIMUM_VALUE = -180.0
LONG_MAXIMUM_VALUE = 180.0

dao = DeliverymanDao()

class DeliverymanControl:
    @staticmethod
    def find(id_deliveryman):
        try:
            response = dao.select(id_deliveryman)
            return response
        except Exception as error:
            raise ValueError('Unable to find deliveryman: ' + str(error))

    @staticmethod
    def register(deliveryman):
        DeliverymanControl.validate(deliveryman)

        try:
            deliveryman.password = DeliverymanControl.encrypt_password(deliveryman.password)
            id_deliveryman = dao.save(deliveryman)

            return id_deliveryman
        except Exception as error:
            printError()
            raise ValueError('Unable to register deliveryman: ' + str(error))

    @staticmethod
    def update(deliveryman):
        DeliverymanControl.validate(deliveryman)

        try:
            if deliveryman.password != None:
                deliveryman.password = DeliverymanControl.encrypt_password(deliveryman.password)

            success = dao.update(deliveryman)
            return success
        except Exception as error:
            raise ValueError('Unable to update deliveryman: ' + str(error))

    @staticmethod
    def delete(id_deliveryman):
        try:
            success = dao.delete(id_deliveryman)
            return success
        except Exception as error:
            raise ValueError('Unable to remove deliveryman: ' + str(error))

    @staticmethod
    def validate(deliveryman):
        CompanyControl.validate(deliveryman)

        DeliverymanControl.validate_name(deliveryman)
        DeliverymanControl.validate_dui(deliveryman)
        DeliverymanControl.validate_lat(deliveryman)
        DeliverymanControl.validate_long(deliveryman)

    @staticmethod
    def validate_name(deliveryman):
        if deliveryman.name_deliveryman != None and len(deliveryman.name_deliveryman) < NAME_MINIMUM_LENGTH:
            raise ValueError('Invalid name, please use one with at least ' + str(NAME_MINIMUM_LENGTH) + ' characters')

    @staticmethod
    def validate_dui(deliveryman):
        if deliveryman.dui != None and len(deliveryman.dui) < DUI_MINIMUM_LENGTH:
            raise ValueError('Invalid dui, please use one with at least ' + str(DUI_MINIMUM_LENGTH) + ' characters')

    @staticmethod
    def validate_lat(deliveryman):
        if deliveryman.lat != None and (deliveryman.lat < LAT_MINIMUM_VALUE or deliveryman.lat > LAT_MAXIMUM_VALUE):
            raise ValueError('Invalid lat, please use one within the range of ' + str(LAT_MINIMUM_VALUE) + ' to ' + str(LAT_MAXIMUM_VALUE))

    @staticmethod
    def validate_long(deliveryman):
        if deliveryman.long != None and (deliveryman.long < LONG_MINIMUM_VALUE or deliveryman.long > LONG_MAXIMUM_VALUE):
            raise ValueError('Invalid long, please use one within the range of ' + str(LONG_MINIMUM_VALUE) + ' to ' + str(LONG_MAXIMUM_VALUE))
