from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Date
from sqlalchemy_utils import database_exists, create_database
from Rest_utils.entities_atributes_Names import *
from DB.DB_helper import getSession

Session=getSession()

    @staticmethod
    def save(adress):
        session=Session()
        
        session.add(adress)
        session.commit()
        session.refresh(adress)
        id=adress.id
        session.close()
        return id
