from Models.DAO.delivery_DAO import DeliveryDao
from Models.DAO.DAO_utils import printError
from Models.DB.DB_helper import Delivery

dao = DeliveryDao()

class DeliveryControl:
    @staticmethod
    def find(id_delivery):
        try:
            response = dao.select(id_delivery)
            return response
        except Exception as error:
            raise ValueError('Unable to find delivery: ' + str(error))

    @staticmethod
    def register(delivery):
        DeliveryControl.validate(delivery)

        try:
            id_delivery = dao.save(delivery)

            return id_delivery
        except Exception as error:
            printError()
            raise ValueError('Unable to register delivery: ' + str(error))

    @staticmethod
    def update(delivery):
        DeliveryControl.validate(delivery)

        try:
            success = dao.update(delivery)
            return success
        except Exception as error:
            raise ValueError('Unable to update delivery: ' + str(error))

    @staticmethod
    def delete(id_delivery):
        try:
            success = dao.delete(id_delivery)
            return success
        except Exception as error:
            raise ValueError('Unable to remove delivery: ' + str(error))

    @staticmethod
    def validate(delivery):
        DeliveryControl.validate_and_update_type(delivery)
        DeliveryControl.validate_and_update_status(delivery)

    @staticmethod
    def validate_and_update_type(delivery):
        if delivery.type.__class__ == int:
            try:
                delivery.type = Delivery.DeliveryType(delivery.type)
            except ValueError:
                raise ValueError('Invalid type, please use one of the options: ' + str([e.value for e in Delivery.DeliveryType]))

    @staticmethod
    def validate_and_update_status(delivery):
        if delivery.status.__class__ == int:
            try:
                delivery.status = Delivery.DeliveryStatus(delivery.status)
            except ValueError:
                raise ValueError('Invalid status, please use one of the options: ' + str([e.value for e in Delivery.DeliveryStatus]))
