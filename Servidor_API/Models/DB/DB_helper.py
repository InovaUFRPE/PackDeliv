# coding=utf-8
import datetime
import enum
from sqlalchemy import create_engine, inspect, Column, Integer, String, Boolean
from sqlalchemy import ForeignKey, Date, Float, Enum, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker, relationship
from Rest_utils.entities_atributes_Names import *

Base = declarative_base()

class Address(Base):
    __tablename__= ADDRESS
    AddressType = enum.Enum('AddressType', ['endereco_empresa_matriz', 'endereco_empresa', 'endereco_cliente'])

    id= Column(ADDRESS_ID,Integer,primary_key=True)
    street = Column(ADDRESS_STREET, String(255), nullable=False)
    number = Column(ADDRESS_NUMBER,String(255), nullable=False)
    complement = Column(ADDRESS_COMPLEMENT,String(255))
    district = Column(ADDRESS_DISTRICT,String(255), nullable=False)
    postal_code= Column(ADDRESS_POSTAL_CODE, String(255), nullable= False)
    city = Column(ADDRESS_CITY, String(255), nullable=False)
    state = Column(ADDRESS_STATE, String(255),nullable=False)
    country = Column(ADDRESS_COUNTRY,String(255),nullable=False)
    lat=Column(LOCALIZATION_LAT,Float(), nullable=False)
    long=Column(LOCALIZATION_LONG,Float(), nullable=False)
    type=Column(ADDRESS_TYPE, Enum(AddressType))
    id_company=Column(COMPANY+'_'+COMPANY_ID,Integer, ForeignKey(COMPANY+'.'+COMPANY_ID))
    id_client=Column(CLIENT+'_'+CLIENT_ID,Integer, ForeignKey(CLIENT+'.'+CLIENT_ID))

    def __str__(self):
        dic = self.as_dict()
        string='{ '
        for i,j in dic.items():
            string+= str(i) + ' : ' + str(j) + ',\n'
        string=string[:len(string)-2]
        string+=' }'
        return string

class Client(Base):
    __tablename__=CLIENT

    id= Column(CLIENT_ID,Integer,primary_key=True)
    upi=Column(CLIENT_UPI,String(11),unique=True)#unique company identifier
    name=Column(CLIENT_NAME,String(255),nullable=False)
    addresses=relationship(Address.__name__)

    def __str__(self):
        dic = self.as_dict()
        string='{ '
        for i,j in dic.items():
            string+= str(i) + ' : ' + str(j) + ',\n'
        string=string[:len(string)-2]
        string+=' }'
        return string

class Vehicle(Base):
    __tablename__= VEHICLE

    id= Column(VEHICLE_ID,Integer,primary_key=True)
    licence_plate = Column(VEHICLE_LICENSE_PLATE, String(255),unique=True, nullable=False)
    year=Column(VEHICLE_YEAR, Integer,nullable=False)
    model = Column(VEHICLE_MODEL,String(255),nullable=False)
    color =Column(VEHICLE_COLOR,String(255))
    ready=Column(VEHICLE_READY, Boolean, default=False)
    volume=Column(VEHICLE_VOLUME,Integer,nullable=False)


    def as_dict(self):
     return { VEHICLE_ID: self.id,
              VEHICLE_LICENSE_PLATE: self.licence_plate,
              VEHICLE_YEAR: self.year,
              VEHICLE_MODEL: self.model,
              VEHICLE_COLOR: self.color,
              VEHICLE_READY: self.ready,
              VEHICLE_VOLUME: self.volume}

    def __str__(self):
        dic = self.as_dict()
        string='{ '
        for i,j in dic.items():
            string+= str(i) + ' : ' + str(j) + ',\n'
        string=string[:len(string)-2]
        string+=' }'
        return string


    def as_dict(self):
     return { VEHICLE_ID: self.id,
              VEHICLE_LICENSE_PLATE: self.licence_plate,
              VEHICLE_YEAR: self.year,
              VEHICLE_MODEL: self.model,
              VEHICLE_COLOR: self.color,
              VEHICLE_READY: self.ready,
              VEHICLE_VOLUME: self.volume }

    def __str__(self):
        dic = self.as_dict()
        string='{ '
        for i,j in dic.items():
            string+= str(i) + ' : ' + str(j) + ',\n'
        string=string[:len(string)-2]
        string+=' }'
        return string

class Company(Base):
    __tablename__=COMPANY

    id=Column(COMPANY_ID, Integer, primary_key=True)
    name_company=Column(COMPANY_NAME,String(255),nullable=False)
    password = Column(COMPANY_PASSWORD,String(255),nullable=False)
    login=Column(COMPANY_LOGIN,String(255),unique=True,nullable=False)
    email=Column(COMPANY_EMAIL,String(255),unique=True,nullable=False)
    uci=Column(COMPANY_UCI,String(14),unique=True)#unique company identifier
    type=Column(COMPANY_TYPE, String(255))
    addresses=relationship(Address.__name__)
    __mapper_args__ = {
        'polymorphic_identity': COMPANY,
        'polymorphic_on':type
    }
    #o enum ja trata sem precisar utilizar uma especialização
    #adicionar o relacionamento com endereço de empresa
    #utilizar  Query-Enabled Properties para os dois endereços,
    #pois desse modo daria para manter os enums?
    #adicionar o relacionamento com endereço(esse é pra multiplos endereços de entrega)
    def as_dict(self):
     return { COMPANY_ID: self.id,
              COMPANY_NAME: self.name_company,
              COMPANY_EMAIL: self.email,
              COMPANY_UCI: self.uci,
              COMPANY_TYPE: self.type,
              ADDRESSES: self.addresses}

    def __str__(self):
        dic = self.as_dict()
        string='{ '
        for i,j in dic.items():
            string+= str(i) + ' : ' + str(j) + ',\n'
        string=string[:len(string)-2]
        string+=' }'
        return string

class Deliveryman(Company):
    __tablename__=DELIVERYMAN
    id = Column(DELIVERYMAN_ID,Integer, ForeignKey(Company.id), primary_key=True)
    name_deliveryman=Column(DELIVERYMAN_NAME,String(255),nullable=False)
    dui=Column(DELIVERYMAN_DUI,String(255),unique=True,nullable=False)
    status=Column(DELIVERYMAN_STATUS,Boolean, default=False)
    ready=Column(DELIVERYMAN_READY,Boolean, default=False)
    lat=Column(LOCALIZATION_LAT,Float(), nullable=False)
    long=Column(LOCALIZATION_LONG,Float(), nullable=False)
    Id_veiculo=Column(DELIVERYMAN_ID_VEHICLE,Integer,ForeignKey(Vehicle.id))

    vehicle=relationship(Vehicle.__name__)
    __mapper_args__ = {
        'polymorphic_identity':DELIVERYMAN,
    }

    def as_dict(self):
     return { DELIVERYMAN_ID: self.id,
              DELIVERYMAN_NAME: self.name_deliveryman,
              DELIVERYMAN_DUI: self.email,
              DELIVERYMAN_STATUS: self.status,
              DELIVERYMAN_READY: self.ready,
              LOCALIZATION_LAT: self.lat,
              LOCALIZATION_LONG: self.long,
              COMPANY_NAME: self.name_company,
              COMPANY_EMAIL: self.email,
              COMPANY_UCI: self.uci,
              COMPANY_TYPE: self.type,
              DELIVERYMAN_ID_VEHICLE: self.Id_veiculo
              }

    def __str__(self):
        dic = self.as_dict()
        string='{ '
        for i,j in dic.items():
            string+= str(i) + ' : ' + str(j) + ',\n'
        string=string[:len(string)-2]
        string+=' }'
        return string


    #adicionar o relacionamento com entregas para que possa se realizar a lista de pacotes

class Package(Base):
    __tablename__=PACKAGE
    PackageStatus = enum.Enum('PackageStatus', ['em fila para coleta','em fila para entrega','em analise','entregue','em coleta','em entrega'])

    id=Column(PACKAGE_ID, Integer, primary_key=True)
    width=Column(PACKAGE_WIDTH,Integer,nullable=False)
    height=Column(PACKAGE_HEIGHT,Integer,nullable=False)
    length=Column(PACKAGE_LENGTH,Integer,nullable=False)
    weight=Column(PACKAGE_WEIGHT,Integer,nullable=False)
    shiped=Column(PACKAGE_SHIPPED,Boolean, default=False)
    received=Column(PACKAGE_RECEIVED,Boolean, default=False)
    volume=Column(PACKAGE_VOLUME,Integer,nullable=False)
    static_location=Column(PACKAGE_CURRENT_STATIC_LOCATION,String(255))
    status=Column(PACKAGE_STATUS, Enum(PackageStatus))
    id_address_start=Column(PACKAGE_ID_ADDRESS_START,Integer)#address company id
    id_address_destiny=Column(PACKAGE_ID_ADDRESS_DESTINY,Integer)#address client id


    #addresses=relationship(Address.__name__)
    #deliveries=relationship(Delivery.__name__, back_populates="package")
    #address posuira dois endereços a diferença estará no tipo, tentar especificar como o
    #join do relacionamento irá funcionar para que ele mantenha as duas keys estrangeiras
    #tentar manter o __name__ em Delivery no outro relacionamento, caso não consiga
    # por o nome direto

    def __str__(self):
        dic = self.as_dict()
        string='{ '
        for i,j in dic.items():
            string+= str(i) + ' : ' + str(j) + ',\n'
        string=string[:len(string)-2]
        string+=' }'
        return string

class Delivery(Base):
    __tablename__=DELIVERY

    id=Column(DELIVERY_ID, Integer, primary_key=True)
    code=Column(DELIVERY_IDENTIFIER_CODE, String(255))
    shipping_date=Column(DELIVERY_SHIPPING_DATE,DateTime, default=datetime.datetime.utcnow)
    finalization_date=Column(DELIVERY_FINALIZATION_DATE,DateTime, default=False)
    id_service_order=Column(DELIVERY_ID_SERVICE_ORDER,ForeignKey(SERVICE_ORDER+'.'+SERVICE_ORDER_ID))
    id_package=Column(DELIVERY_ID_PACKAGE,Integer,ForeignKey(PACKAGE+'.'+PACKAGE_ID))
    status=Column(DELIVERY_STATUS, Enum('entregador designado para a coleta','entregador a caminho para coleta',
    'saiu para entrega','a caminho da casa do cliente','entrega finalizada','coleta finalizada'))
    type=Column(DELIVERY_TYPE, Enum('entrega','coleta'))
    package=relationship(Package.__name__)

    def as_dict(self):
     return { DELIVERY_ID: self.id,
              DELIVERY_IDENTIFIER_CODE: self.code,
              DELIVERY_SHIPPING_DATE: self.shipping_date,
              DELIVERY_FINALIZATION_DATE: self.length,
              DELIVERY_ID_SERVICE_ORDER: self.weight,
              DELIVERY_STATUS: self.status,
              DELIVERY_TYPE: self.type,
              PACKAGE: self.package
              }

    def __str__(self):
        dic = self.as_dict()
        string='{ '
        for i,j in dic.items():
            string+= str(i) + ' : ' + str(j) + ',\n'
        string=string[:len(string)-2]
        string+=' }'
        return string

class Service_order(Base):
    __tablename__=SERVICE_ORDER

    id=Column(SERVICE_ORDER_ID, Integer, primary_key=True)
    code=Column(SERVICE_ORDER_IDENTIFIER_CODE,String(255),unique=True,nullable=False)
    shipping_date=Column(SERVICE_ORDER_SHIPPING_DATE,DateTime, default=datetime.datetime.utcnow)
    finalization_date=Column(SERVICE_ORDER_FINALIZATION_DATE,DateTime, default=False)
    status = Column(SERVICE_ORDER_STATUS, Enum('em analise','confirmado','finalizado'))
    deliveries=relationship(Delivery.__name__)
    #adionar o relacionamento com ordem de serviço e pacote
    def as_dict(self):
     return { SERVICE_ORDER_ID: self.id,
              SERVICE_ORDER_IDENTIFIER_CODE: self.code,
              SERVICE_ORDER_SHIPPING_DATE: self.shipping_date,
              SERVICE_ORDER_FINALIZATION_DATE: self.finalization_date,
              DELIVERIES: self.deliveries
              }

    def __str__(self):
        dic = self.as_dict()
        string='{ '
        for i,j in dic.items():
            string+= str(i) + ' : ' + str(j) + ',\n'
        string=string[:len(string)-2]
        string+=' }'
        return string

def getEngine():
    user ="root"
    password=""
    address="localhost"
    database_name="packDeliv"
    engine = create_engine('mysql+pymysql://%s:%s@%s/%s'%(user, password, address, database_name), echo=True)

    return engine

def INIT_API():
    engine = getEngine()
    if not database_exists(engine.url):
        create_database(engine.url)
    Base.metadata.create_all(bind=engine)
    return sessionmaker(bind=engine)

def getSession():
    engine = getEngine()
    Session=sessionmaker(bind=engine)
    return Session()

def attribute_to_column_dict(model_class):
    return inspect(model_class).columns

def column_name_to_attribute_dict(model_class):
    return {column.key: attribute_name for attribute_name, column in attribute_to_column_dict(model_class).items()}

def model_as_dict(model):
    dict = {}
    for attribute_name, column in attribute_to_column_dict(model.__class__).items():
        attribute_value = getattr(model, attribute_name)
        if isinstance(attribute_value, enum.Enum):
            attribute_value = attribute_value.value
        dict[column.key] = attribute_value

    return dict

def model_from_dict(model_class, dict):
    model = model_class()
    column_map = column_name_to_attribute_dict(model_class)

    for dict_key, dict_value in dict.items():
        attribute_name = column_map.get(dict_key, None)
        if attribute_name != None:
            setattr(model, attribute_name, dict_value)

    return model
