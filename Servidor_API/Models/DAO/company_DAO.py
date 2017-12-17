from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Date
from sqlalchemy_utils import database_exists, create_database
from Rest_utils.entities_atributes_Names import *
from DB.DB_helper import *
from Models.adress import *

class Company(Base):
    __tablename__=COMPANY

    id=Column(COMPANY_ID, Integer, primary_key=True)
    id_adress=Column(COMPANY_ID_ADRESS,Integer,ForeignKey(Adress.id),nullable=False)
    name_company=Column(COMPANY_NAME,String(255),nullable=False)
    password = Column(COMPANY_PASSWORD,String(255),nullable=False)
    login=Column(COMPANY_LOGIN,String(255),unique=True,nullable=False)
    email=Column(COMPANY_EMAIL,String(255),unique=True,nullable=False)
    uci=Column(COMPANY_UCI,String(14),unique=True)#unique company identifier
    type=Column(COMPANY_TYPE, String(255))
    __mapper_args__ = {
        'polymorphic_identity': COMPANY,
        'polymorphic_on':type
    }
    
    @staticmethod
    def save(company):
        session=Session()
        
        session.add(company)
        response = False
        try:
            session.commit()
            session.refresh(company)
            response = company.id
        except:
            deleteAdress(company.id_adress)

        session.close()
        return response
    


def getCompany(json_company):
    login=json_company['login']
    senha=json_company['senha']
    Session=getSession()
    session=Session()
    response= session.query(Company).filter(Company.login == login , Company.password==senha).all()
    if len(response)==1:
        c=response[0]
        adress=getAdress(c.id_adress)["response"]
        #dic= company.__dict__
        #dicCompany={key : value for key, value in dic.items() if key != '_sa_instance_state' }
        dicCompany={COMPANY_ID :c.id , ADRESS : adress, COMPANY_TYPE : c.type, COMPANY_NAME: c.name_company,COMPANY_LOGIN: c.login,COMPANY_EMAIL:c.email,COMPANY_UCI:c.uci , COMPANY_TYPE:c.type}
        response= dicCompany
    else:
        response=False
    return response
