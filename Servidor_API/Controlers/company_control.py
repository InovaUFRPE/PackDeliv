import re, bcrypt
from Models.DAO.company_DAO import CompanyDao
from Models.DAO.DAO_utils import printError

NAME_MINIMUM_LENGTH = 6
LOGIN_MINIMUM_LENGTH = 6
PASSWORD_MINIMUM_LENGTH = 6
EMAIL_MINIMUM_LENGTH = 6
EMAIL_REGEX = re.compile("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
UCI_EXACT_LENGTH = 14
UCI_REGEX = re.compile("[0-9]{14}")

dao = CompanyDao()

class CompanyControl:
    @staticmethod
    def find(id_company):
        try:
            response = dao.select(id_company)
            return response
        except Exception as error:
            raise ValueError('Unable to find company: ' + str(error))

    @staticmethod
    def register(company):
        CompanyControl.validate(company)

        try:
            company.password = CompanyControl.encrypt_password(company.password)
            id_company = dao.save(company)

            return id_company
        except Exception as error:
            printError()
            raise ValueError('Unable to register company: ' + str(error))

    @staticmethod
    def update(company):
        CompanyControl.validate(company)

        try:
            if company.password != None:
                company.password = CompanyControl.encrypt_password(company.password)

            success = dao.update(company)
            return success
        except Exception as error:
            raise ValueError('Unable to update company: ' + str(error))

    @staticmethod
    def delete(id_company):
        try:
            success = dao.delete(id_company)
            return success
        except Exception as error:
            raise ValueError('Unable to remove company: ' + str(error))

    @staticmethod
    def validate(company):
        CompanyControl.validate_name(company)
        CompanyControl.validate_login(company)
        CompanyControl.validate_password(company)
        CompanyControl.validate_email(company)
        CompanyControl.validate_uci(company)

    @staticmethod
    def validate_name(company):
        if company.name_company != None and len(company.name_company) < NAME_MINIMUM_LENGTH:
            raise ValueError('Invalid name, please use one with at least ' + str(NAME_MINIMUM_LENGTH) + ' characters')

    @staticmethod
    def validate_login(company):
        if company.login != None and len(company.login) < LOGIN_MINIMUM_LENGTH:
            raise ValueError('Invalid login, please use one with at least ' + str(LOGIN_MINIMUM_LENGTH) + ' characters')

    @staticmethod
    def validate_password(company):
        if company.password != None and len(company.password) < PASSWORD_MINIMUM_LENGTH:
            raise ValueError('Invalid password, please use one with at least ' + str(PASSWORD_MINIMUM_LENGTH) + ' characters')

    @staticmethod
    def validate_email(company):
        if company.email != None:
            if len(company.email) < EMAIL_MINIMUM_LENGTH:
                raise ValueError('Invalid email, please use one with at least ' + str(EMAIL_MINIMUM_LENGTH) + ' characters')
            if re.match(EMAIL_REGEX, company.email) == None:
                raise ValueError('Invalid email, please use the format aaaa@bbbb.ccc')

    @staticmethod
    def validate_uci(company):
        if company.uci != None:
            if len(company.uci) < UCI_EXACT_LENGTH:
                raise ValueError('Invalid uci, please use one with exactly ' + str(UCI_EXACT_LENGTH) + ' digits')
            if re.match(UCI_REGEX, company.uci) == None:
                raise ValueError('Invalid uci, please use only digits')

    @staticmethod
    def encrypt_password(password):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
