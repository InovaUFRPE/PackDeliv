import enum
import datetime
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy import ForeignKey, Date, Float, Enum, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from Rest_utils.entities_atributes_Names import *  #(dont work in RestApi.py -->fix it)

Base = declarative_base()

class AdressTypeEnum(enum.Enum):
    adress_type_1=ADRESS_COMPANY_MATRIX
    adress_type_2=ADRESS_COMPANY
    adress_type_3=ADRESS_CLIENT

class Client(Base):
    __tablename__=CLIENT

    id= Column(CLIENT_ID,Integer,primary_key=True)
    upi=Column(CLIENTE_UPI,String(11),unique=True)#unique company identifier
    name=Column(CLIENTE_NAME,String(255),nullable=False)
    adress=relationship(ADRESS)

class Adress(Base):
    __tablename__= ADRESS
    
    id= Column(ADRESS_ID,Integer,primary_key=True)
    street = Column(ADRESS_STREET, String(255), nullable=False)
    number = Column(ADRESS_NUMBER,String(255), nullable=False)
    complement = Column(ADRESS_COMPLEMENT,String(255))
    district = Column(ADRESS_DISTRICT,String(255), nullable=False)
    postal_code= Column(ADRESS_POSTAL_CODE, String(255), nullable= False)
    city = Column(ADRESS_CITY, String(255), nullable=False)
    state = Column(ADRESS_STATE, String(255),nullable=False)
    country = Column(ADRESS_COUNTRY,String(255),nullable=False)
    lat=Column(LOCALIZATION_LAT,Float(), nullable=False)
    long=Column(LOCALIZATION_LONG,,Float(), nullable=False)

    id_company=Column(Integer, ForeignKey(COMPANY+'.'+COMPANY_ID))
    id_client=Column(Integer, ForeignKey(CLIENT+'.'+CLIENT_ID))

    type=Column(ADRESS_TYPE, Enum(AdressTypeEnum))

class Vehicle(Base):
    __tablename__= VEHICLE

    id= Column(VEHICLE_ID,Integer,primary_key=True)
    licence_plate = Column(VEHICLE_LICENSE_PLATE, String(255),unique=True, nullable=False)
    year=Column(VEHICLE_YEAR, Integer,nullable=False)
    model = Column(VEHICLE_MODEL,String(255),nullable=False)
    color =Column(VEHICLE_COLOR,String(255))
    ready=Column(VEHICLE_READY, Boolean, default=False)
    volume=Column(VEHICLE_VOLUME,Integer,nullable=False)


class Company(Base):
    __tablename__=COMPANY

    id=Column(COMPANY_ID, Integer, primary_key=True)
    #id_adress=Column(COMPANY_ID_ADRESS,Integer,ForeignKey(Adress.id),nullable=False)
    name_company=Column(COMPANY_NAME,String(255),nullable=False)
    password = Column(COMPANY_PASSWORD,String(255),nullable=False)
    login=Column(COMPANY_LOGIN,String(255),unique=True,nullable=False)
    email=Column(COMPANY_EMAIL,String(255),unique=True,nullable=False)
    uci=Column(COMPANY_UCI,String(14),unique=True)#unique company identifier
    type=Column(COMPANY_TYPE, String(255))
    adress=relationship(ADRESS)
    __mapper_args__ = {
        'polymorphic_identity': COMPANY,
        'polymorphic_on':type
    }
    #o enum ja trata sem precisar utilizar uma especialização
    #adicionar o relacionamento com endereço de empresa
    #utilizar  Query-Enabled Properties para os dois endereços,
    #pois desse modo daria para manter os enums?
    #adicionar o relacionamento com endereço(esse é pra multiplos endereços de entrega)

class Deliveryman(Company):
    __tablename__=DELIVERYMAN
    id = Column(DELIVERYMAN_ID,Integer, ForeignKey(Company.id), primary_key=True)
    name_deliveryman=Column(DELIVERYMAN_NAME,String(255),nullable=False)
    dui=Column(DELIVERYMAN_DUI,String(255),unique=True,nullable=False)
    status=Column(DELIVERYMAN_STATUS,Boolean, default=False)
    ready=Column(DELIVERYMAN_READY,Boolean, default=False)
    lat=Column(LOCALIZATION_LAT,Float(), nullable=False)
    long=Column(LOCALIZATION_LONG,,Float(), nullable=False)

    Id_veiculo=Column(DELIVERYMAN_ID_VEHICLE,Integer,ForeignKey(Vehicle.id))
    Vehicle=relationship(VEHICLE)
    __mapper_args__ = {
        'polymorphic_identity':DELIVERYMAN,
    }


    
    #adicionar o relacionamento com entregas para que possa se realizar a lista de pacotes


class Package(Base):
    __tablename__=PACKAGE
    id=Column(PACKAGE_ID, Integer, primary_key=True)
    width=Column(PACKAGE_WIDTH,Integer,nullable=False)
    height=Column(PACKAGE_HEIGHT,Integer,nullable=False)
    length=Column(PACKAGE_LENGTH,Integer,nullable=False)
    weight=Column(PACKAGE_WEIGHT,Integer,nullable=False)
    shiped=Column(PACKAGE_SHIPPED,Boolean, default=False)
    received=Column(PACKAGE_RECEIVED,Boolean, default=False)
    volume=Column(PACKAGE_VOLUME,Integer,nullable=False)
    id_adress_start=Column(PACKAGE_ID_START_ADRESS,Integer)
    id_adress_destiny=Column(PACKAGE_ID_ADRESS,Integer)
    static_location=Column(PACKAGE_CURRENT_STATIC_LOCATION,String(255))
    
    
    #adicionar o relacionamento com entrega
    #adcionar o relacionamento com endereço
    #utilizar  Query-Enabled Properties para os dois endereços,
    #pois desse modo daria para manter os enums?


class Delivery(Base):
    __tablename__=DELIVERY

    id=Column(DELIVERY_ID, Integer, primary_key=True)
    code=Column(DELIVERY_IDENTIFIER_CODE, String(255))
    shipping_date=Column(DELIVERY_SHIPPING_DATE,DateTime, default=datetime.datetime.utcnow)
    finalization_date=Column(DELIVERY_FINALIZATION_DATE,DateTime, default=False)
    id_service_order=Column(DELIVERY_ID_SERVICE_ORDER,Integer,ForeignKey(Service_order.id,onupdate="CASCADE", ondelete="CASCADE"))
    id_package=Column(DELIVERY_ID_PACKAGE,Integer,ForeignKey(Package.id,onupdate="CASCADE", ondelete="CASCADE"))
    #adionar o relacionamento com ordem de serviço e pacote

class Service_order(Base):
    __tablename__=SERVICE_ORDER
    
    id=Column(SERVICE_ORDER_ID, Integer, primary_key=True)
    code=Column(SERVICE_ORDER_IDENTIFIER_CODE,String(255),unique=True,nullable=False)
    shipping_date=Column(SERVICE_ORDER_SHIPPING_DATE,DateTime, default=datetime.datetime.utcnow)
    finalization_date=Column(SERVICE_ORDER_FINALIZATION_DATE,DateTime, default=False)

def getEngine():

    user ="root"
    password=""
    adress="localhost"
    database_name="packDeliv"
    engine = create_engine('mysql+pymysql://%s:%s@%s/%s'%(user, password, adress, database_name), echo=True)

    return engine

def INIT_API():
    engine = getEngine()
    if not database_exists(engine.url):
        create_database(engine.url)
    Base.metadata.create_all(bind=engine)
    return sessionmaker(bind=engine)

def getSession():
    engine = getEngine()
    return sessionmaker(bind=engine)



