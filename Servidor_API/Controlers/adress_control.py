from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Date
from sqlalchemy_utils import database_exists, create_database
from Rest_utils.entities_atributes_Names import *
from DB.DB_helper import *

class Adress(Base):
    __tablename__= ADRESS
    
    id= Column(ADRESS_ID,Integer,primary_key=True)
    street = Column(ADRESS_STREET, String(255))
    number = Column(ADRESS_NUMBER,String(255), nullable=False)
    complement = Column(ADRESS_COMPLEMENT,String(255))
    district = Column(ADRESS_DISTRICT,String(255), nullable=False)
    postal_code= Column(ADRESS_POSTAL_CODE, String(255), nullable= False)
    city = Column(ADRESS_CITY, String(255), nullable=False)
    state = Column(ADRESS_STATE, String(255),nullable=False)
    country = Column(ADRESS_COUNTRY,String(255),nullable=False)
    
    
    @staticmethod
    def save(adress):
        session=Session()
        
        session.add(adress)
        session.commit()
        session.refresh(adress)
        id=adress.id
        session.close()
        return id
