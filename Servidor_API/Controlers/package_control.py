from Models.DAO.package_DAO import PackageDao
from Models.DAO.DAO_utils import printError
from Models.DB.DB_helper import Package

dao = PackageDao()

class PackageControl:
    @staticmethod
    def find(id_package):
        try:
            response = dao.select(id_package)
            return response
        except Exception as error:
            raise ValueError('Unable to find package: ' + str(error))

    @staticmethod
    def register(package):
        PackageControl.validate(package)

        try:
            id_package = dao.save(package)

            return id_package
        except Exception as error:
            printError()
            raise ValueError('Unable to register package: ' + str(error))

    @staticmethod
    def update(package):
        PackageControl.validate(package)

        try:
            success = dao.update(package)
            return success
        except Exception as error:
            raise ValueError('Unable to update package: ' + str(error))

    @staticmethod
    def delete(id_package):
        try:
            success = dao.delete(id_package)
            return success
        except Exception as error:
            raise ValueError('Unable to remove package: ' + str(error))

    @staticmethod
    def validate(package):
        PackageControl.validate_and_update_status(package)

    @staticmethod
    def validate_and_update_status(package):
        if package.status.__class__ == int:
            try:
                package.status = Package.PackageStatus(package.status)
            except ValueError:
                raise ValueError('Invalid status, please use one of the options: ' + str([e.value for e in Package.PackageStatus]))
