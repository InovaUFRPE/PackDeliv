from Models.DAO.service_order_DAO import ServiceOrderDao
from Models.DAO.DAO_utils import printError
from Models.DB.DB_helper import ServiceOrder

dao = ServiceOrderDao()

class ServiceOrderControl:
    @staticmethod
    def find(id_service_order):
        try:
            response = dao.select(id_service_order)
            return response
        except Exception as error:
            raise ValueError('Unable to find service_order: ' + str(error))

    @staticmethod
    def register(service_order):
        ServiceOrderControl.validate(service_order)

        try:
            id_service_order = dao.save(service_order)

            return id_service_order
        except Exception as error:
            printError()
            raise ValueError('Unable to register service_order: ' + str(error))

    @staticmethod
    def update(service_order):
        ServiceOrderControl.validate(service_order)

        try:
            success = dao.update(service_order)
            return success
        except Exception as error:
            raise ValueError('Unable to update service_order: ' + str(error))

    @staticmethod
    def delete(id_service_order):
        try:
            success = dao.delete(id_service_order)
            return success
        except Exception as error:
            raise ValueError('Unable to remove service_order: ' + str(error))

    @staticmethod
    def validate(service_order):
        ServiceOrderControl.validate_and_update_status(service_order)

    @staticmethod
    def validate_and_update_status(service_order):
        if service_order.status.__class__ == int:
            try:
                service_order.status = ServiceOrder.ServiceOrderStatus(service_order.status)
            except ValueError:
                raise ValueError('Invalid status, please use one of the options: ' + str([e.value for e in ServiceOrder.ServiceOrderStatus]))
