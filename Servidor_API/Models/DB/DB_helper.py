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
    __tablename__ = ADDRESS
    AddressType = enum.Enum('AddressType', ['MATRIZ', 'endereco_empresa', 'endereco_cliente'])

    id = Column(Integer, primary_key = True)
    street = Column(String(255), nullable = False)
    number = Column(String(255), nullable = False)
    complement = Column(String(255))
    district = Column(String(255), nullable = False)
    postal_code = Column(String(255), nullable = False)
    city = Column(String(255), nullable = False)
    state = Column(String(255),nullable = False)
    country = Column(String(255),nullable = False)
    lat = Column(Float(), nullable = True)
    long = Column(Float(), nullable = True)
    type = Column(Enum(AddressType))
    id_company = Column(Integer, ForeignKey(COMPANY + '.id'))
    id_client = Column(Integer, ForeignKey(CLIENT + '.id'))

    def as_dict(self):
        selfDic = model_as_dict(self)
        return selfDic

    def __str__(self):      
        return self.as_dict

class Client(Base):
    __tablename__=CLIENT

    id = Column(Integer, primary_key = True)
    upi=Column(String(11), unique = True)#unique company identifier
    name=Column(String(255), nullable = False)
    addresses=relationship(Address.__name__)

    def as_dict(self):
        selfDic = model_as_dict(self)
        if self.addresses != None:
            selfDic['addresses'] = [i.as_dict() for i in self.addresses]
        return selfDic
     #return {i for i in self.addresses}
    def __str__(self):      
        return self.as_dict

class Vehicle(Base):
    __tablename__= VEHICLE

    id = Column(Integer, primary_key = True)
    licence_plate = Column(String(255), unique = True, nullable = False)
    year = Column(Integer, nullable = False)
    model = Column(String(255), nullable = False)
    color = Column(String(255))
    ready = Column(Boolean, default = False)
    volume = Column(Integer, nullable = False)

    def as_dict(self):
        selfDic = model_as_dict(self)
        return selfDic

    def __str__(self):      
        return self.as_dict

class Company(Base):

    __tablename__=COMPANY

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable = False)
    password = Column(String(255), nullable = False)
    login = Column(String(255), unique = True,nullable = False)
    email = Column(String(255), unique = True,nullable = False)
    uci = Column(String(14), unique = True)#unique company identifier
    type = Column(String(255))
    addresses=relationship(Address.__name__)
    packages = relationship ('Package')
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
        selfDic = model_as_dict(self)
        selfDic.pop('password')
        selfDic['addresses'] = [i.as_dict() for i in self.addresses]
        if self.packages != None :
            selfDic['packages'] = [i.as_dict() for i in self.packages]
        return selfDic
     #return {i for i in self.addresses}
    def __str__(self):      
        return self.as_dict

class Deliveryman(Company):
    __tablename__ = DELIVERYMAN
    id = Column(Integer, ForeignKey(Company.id), primary_key = True)
    name_deliveryman = Column(String(255), nullable = False)
    dui = Column(String(255), unique = True, nullable = False)
    status = Column(Boolean, default = False)
    ready = Column(Boolean, default = False)
    lat = Column(Float(), nullable = False)
    long = Column(Float(), nullable = False)
    id_vehicle = Column(Integer, ForeignKey(Vehicle.id))

    vehicle = relationship(Vehicle.__name__)
    __mapper_args__ = {
        'polymorphic_identity':DELIVERYMAN,
    }

    def as_dict(self):
        selfDic = model_as_dict(self)
        if self.vehicle != None:
            selfDic['vehicle'] = self.vehicle.as_dict()
        if self.addresses != None:
            selfDic['addresses'] = [i.as_dict() for i in self.addresses]
        return selfDic
     #return {i for i in self.addresses}
    def __str__(self):      
        return self.as_dict


    #adicionar o relacionamento com entregas para que possa se realizar a lista de pacotes

class Package(Base):
    __tablename__ = PACKAGE
    PackageStatus = enum.Enum('PackageStatus', ['em fila para coleta','em fila para entrega','em analise','entregue','em coleta','em entrega'])

    id = Column(Integer, primary_key = True)
    width = Column(Integer, nullable = False)
    height = Column(Integer, nullable = False)
    length = Column(Integer, nullable = False)
    weight = Column(Integer, nullable = False)
    shiped = Column(Boolean, default = False)
    received = Column(Boolean, default = False)
    volume = Column(Integer, nullable = False)
    static_location = Column(String(255))
    status = Column(Enum(PackageStatus))
    send_date = Column(DateTime, default = datetime.datetime.utcnow)
    delivery_date = Column(DateTime, default = False)
    id_address_start = Column(Integer, ForeignKey(ADDRESS + '.id'))#address company id
    id_address_destiny = Column(Integer, ForeignKey(ADDRESS + '.id'))#address client id
    id_company = Column(Integer, ForeignKey(COMPANY + '.id'))
    id_client = Column(Integer, ForeignKey(CLIENT + '.id'))
    address_destiny = relationship("Address", foreign_keys=[id_address_destiny])
    address_start = relationship("Address", foreign_keys=[id_address_start])

    def as_dict(self):
        selfDic = model_as_dict(self)
        selfDic['address_destiny'] = self.address_destiny.as_dict()
        selfDic['address_start'] = self.address_start.as_dict()
        
        return selfDic
     #return {i for i in self.addresses}
    def __str__(self):      
        return self.as_dict
    #addresses=relationship(Address.__name__)
    #deliveries=relationship(Delivery.__name__, back_populates="package")
    #address posuira dois endereços a diferença estará no tipo, tentar especificar como o
    #join do relacionamento irá funcionar para que ele mantenha as duas keys estrangeiras
    #tentar manter o __name__ em Delivery no outro relacionamento, caso não consiga
    # por o nome direto

class Delivery(Base):
    __tablename__ = DELIVERY
    DeliveryStatus = enum.Enum('DeliveryStatus', ['entregador designado para a coleta','entregador a caminho para coleta', 'saiu para entrega','a caminho da casa do cliente','entrega finalizada','coleta finalizada'])
    DeliveryType = enum.Enum('DeliveryType', ['entrega','coleta'])

    id = Column(Integer, primary_key = True)
    code = Column(String(255))
    shipping_date = Column(DateTime, default = datetime.datetime.utcnow)
    finalization_date = Column(DateTime, default = False)
    status = Column( Enum(DeliveryStatus), nullable = False)
    type = Column(Enum(DeliveryType), nullable = False)
    id_service_order = Column(ForeignKey(SERVICE_ORDER+'.id'))
    id_package = Column(Integer, ForeignKey(PACKAGE+'.id'))
    package = relationship(Package.__name__)

    def as_dict(self):
        selfDic = model_as_dict(self)
        if self.package != None:
            selfDic['package'] = [i.as_dict() for i in self.package]
        return selfDic
     #return {i for i in self.addresses}
    def __str__(self):      
        return self.as_dict

class ServiceOrder(Base):
    __tablename__ = SERVICE_ORDER
    ServiceOrderStatus = enum.Enum('ServiceOrderStatus', ['em analise','confirmado','finalizado'])

    id = Column( Integer, primary_key = True)
    code = Column( String(255), unique = True, nullable = False)
    shipping_date = Column(DateTime, default = datetime.datetime.utcnow)
    finalization_date = Column( DateTime, default = False)
    status = Column( Enum(ServiceOrderStatus), nullable = False)
    deliveries = relationship( Delivery.__name__)
    def as_dict(self):
        selfDic = model_as_dict(self)
        if self.deliveries != None:
            selfDic['deliveries'] = [i.as_dict() for i in self.deliveries]
        return selfDic
     #return {i for i in self.addresses}
     
    def __str__(self):      
        return self.as_dict
    #adionar o relacionamento com ordem de serviço e pacote

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
    modelInspected = inspect(model_class)
    return modelInspected.columns

def column_name_to_attribute_dict(model_class):
    return {column.key: attribute_name for attribute_name, column in attribute_to_column_dict(model_class).items()}

def model_as_dict(model):
    dict = {}
    for attribute_name, column in inspect(model.__class__).columns.items():
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
