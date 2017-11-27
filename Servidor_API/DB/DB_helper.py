from sqlalchemy import create_engine, Column, Integer, String,Boolean, ForeignKey,Date
from geoalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
#from DB_Names import *  (dont work in RestApi.py -->fix it)



DATABASE_NAME="packDeliv_DB"

TABLE_COMPANY= 'Empresa'
TABLE_DELIVERYMAN= 'Entregador'
TABLE_ADRESS= 'Endereco'
TABLE_VEHICLE='Veiculo'
TABLE_SERVICE_ORDER='Ordem_de_servico'
TABLE_DELIVERY='Entrega'
TABLE_PACKAGE='Pacote'


TABLE_COMPANY_ID = 'id'        
TABLE_COMPANY_ID_ADRESS ='Id_endereco'
TABLE_COMPANY_NAME='Nome_fantasia'
TABLE_COMPANY_PASSWORD ='Senha'
TABLE_COMPANY_LOGIN ='Login'
TABLE_COMPANY_EMAIL ='Email' 
TABLE_COMPANY_UCI= 'CNPJ' # unique identifier of company

TABLE_DELIVERYMAN_ID= 'id'
TABLE_DELIVERYMAN_ID_VEHICLE= 'Id_veiculo'
TABLE_DELIVERYMAN_ID_COMPANY = 'id_empresa'
TABLE_DELIVERYMAN_DUI= 'cnh' #driver unique identifier
TABLE_DELIVERYMAN_AVAILABILITY= 'Disponibilidade'
TABLE_DELIVERYMAN_READY= 'apto'
TABLE_DELIVERYMAN_LOCALIZATION= 'localizacao'

TABLE_ADRESS_ID= 'Id'
TABLE_ADRESS_STREET= 'Logradouro'
TABLE_ADRESS_NUMBER= 'Numero'
TABLE_ADRESS_COMPLEMENT= 'Complemento'
TABLE_ADRESS_DISTRICT= 'Bairro'
TABLE_ADRESS_POSTAL_CODE = 'CEP'
TABLE_ADRESS_CITY= 'Cidade'
TABLE_ADRESS_STATE= 'Estado'
TABLE_ADRESS_COUNTRY= 'Pais'

TABLE_VEHICLE_ID= 'id'
TABLE_VEHICLE_LICENSE_PLATE= 'placa'
TABLE_VEHICLE_YEAR = 'ano'
TABLE_VEHICLE_MODEL = 'modelo'
TABLE_VEHICLE_COLOR = 'cor'
TABLE_VEHICLE_READY= 'apto'

TABLE_SERVICE_ORDER_ID='Id'
TABLE_SERVICE_ORDER_IDENTIFIER_CODE='Codigo'
TABLE_SERVICE_ORDER_SHIPPING_DATE= 'Data_expedicao'
TABLE_SERVICE_ORDER_FINALIZATION_DATE='Data_finalizacao'

TABLE_DELIVERY_ID='Id'
TABLE_DELIVERY_IDENTIFIER_CODE='codigo'
TABLE_DELIVERY_SHIPPING_DATE='Data_expedicao'
TABLE_DELIVERY_FINALIZATION_DATE='Data_finalizacao'
TABLE_DELIVERY_ID_SERVICE_ORDER='Id_ordem_de_servico'
TABLE_DELIVERY_ID_PACKAGE='Id_pacote Varchar'
TABLE_DELIVERY_ID_SUCESS='Sucesso'

TABLE_PACKAGE_ID='Id'
TABLE_PACKAGE_WIDTH='Largura'
TABLE_PACKAGE_HEIGHT='Altura'
TABLE_PACKAGE_LENGTH='Comprimento'
TABLE_PACKAGE_WEIGHT='Peso'
TABLE_PACKAGE_SHIPPED='Expedido'
TABLE_PACKAGE_RECEIVED='Recebido'
TABLE_PACKAGE_LOCAL_DESTINY='Destino'
TABLE_PACKAGE_ID_ADRESS ='Id_endereco'
TABLE_PACKAGE_CURRENT_STATIC_LOCATION='Local_atual_estatico'


Base = declarative_base()

class Adress(Base):
    __tablename__= TABLE_ADRESS
    
    id= Column(TABLE_ADRESS_ID,Integer,primary_key=True)
    street = Column(TABLE_ADRESS_STREET, String(255))
    number = Column(TABLE_ADRESS_NUMBER,Integer, nullable=False)
    complement = Column(TABLE_ADRESS_COMPLEMENT,String(255))
    district = Column(TABLE_ADRESS_DISTRICT,String(255), nullable=False)
    postal_code= Column(TABLE_ADRESS_POSTAL_CODE, String(255), nullable= False)
    city = Column(TABLE_ADRESS_CITY, String(255), nullable=False)
    state = Column(TABLE_ADRESS_STATE, String(255),nullable=False)
    country = Column(TABLE_ADRESS_COUNTRY,String(255),nullable=False)



class Vehicle(Base):
    __tablename__= TABLE_VEHICLE

    id= Column(TABLE_VEHICLE_ID,Integer,primary_key=True)
    licence_plate = Column(TABLE_VEHICLE_LICENSE_PLATE, String(255),unique=True, nullable=False)
    year=Column(TABLE_VEHICLE_YEAR, Integer,nullable=False)
    model = Column(TABLE_VEHICLE_MODEL,String(255),nullable=False)
    color =Column(TABLE_VEHICLE_COLOR,String(255),nullable=False)
    ready=Column(TABLE_VEHICLE_READY, Boolean, default=False)

class Company(Base):
    __tablename__=TABLE_COMPANY

    id=Column(TABLE_COMPANY_ID, Integer, primary_key=True)
    id_adress=Column(TABLE_COMPANY_ID_ADRESS,Integer,ForeignKey(Adress.id),nullable=False)
    name_company=Column(TABLE_COMPANY_NAME,String(255),nullable=False)
    password = Column(TABLE_COMPANY_PASSWORD,String(255),nullable=False)
    login=Column(TABLE_COMPANY_LOGIN,String(255),unique=True,nullable=False)
    email=Column(TABLE_COMPANY_EMAIL,String(255),unique=True,nullable=False)
    uci=Column(TABLE_COMPANY_UCI,Integer,unique=True,nullable=False)#unique company identifier

class Deliveryman(Base):
    __tablename__=TABLE_DELIVERYMAN
    id=Column(TABLE_DELIVERYMAN_ID, Integer, primary_key=True)
    Id_veiculo=Column(TABLE_DELIVERYMAN_ID_VEHICLE,Integer,ForeignKey(Vehicle.id,onupdate="CASCADE", ondelete="CASCADE"))
    id_company=Column(TABLE_DELIVERYMAN_ID_COMPANY,Integer,ForeignKey(Vehicle.id,onupdate="CASCADE", ondelete="CASCADE"))
    dui=Column(TABLE_DELIVERYMAN_DUI,Integer,unique=True,nullable=False)
    availability=Column(TABLE_DELIVERYMAN_AVAILABILITY,Boolean, default=False)
    ready=Column(TABLE_DELIVERYMAN_READY,Boolean, default=False)
    localization = GeometryColumn(TABLE_DELIVERYMAN_LOCALIZATION,Point(2))

class Service_order(Base):
    __tablename__=TABLE_SERVICE_ORDER
    
    id=Column(TABLE_SERVICE_ORDER_ID, Integer, primary_key=True)
    code=Column(TABLE_SERVICE_ORDER_IDENTIFIER_CODE,String(255),unique=True,nullable=False)
    shipping_date=Column(TABLE_SERVICE_ORDER_SHIPPING_DATE,Date)
    finalization_date=Column(TABLE_SERVICE_ORDER_FINALIZATION_DATE,Date)


class Package(Base):
    __tablename__=TABLE_PACKAGE
    id=Column(TABLE_PACKAGE_ID, Integer, primary_key=True)
    width=Column(TABLE_PACKAGE_WIDTH,Integer,nullable=False)
    height=Column(TABLE_PACKAGE_HEIGHT,Integer,nullable=False)
    length=Column(TABLE_PACKAGE_LENGTH,Integer,nullable=False)
    weight=Column(TABLE_PACKAGE_WEIGHT,Integer,nullable=False)
    shiped=Column(TABLE_PACKAGE_SHIPPED,Boolean, default=False)
    receiveid=Column(TABLE_PACKAGE_RECEIVED,Boolean, default=False)
    local_destiny=GeometryColumn(TABLE_PACKAGE_LOCAL_DESTINY,Point(2))
    id_adress_destiny=Column(TABLE_PACKAGE_ID_ADRESS,Integer)
    static_location=Column(TABLE_PACKAGE_CURRENT_STATIC_LOCATION,String(255),nullable=False)

class Delivery(Base):
    __tablename__=TABLE_DELIVERY

    id=Column(TABLE_DELIVERY_ID, Integer, primary_key=True)
    code=Column(TABLE_DELIVERY_IDENTIFIER_CODE, String(255))
    shipping_date=Column(TABLE_DELIVERY_SHIPPING_DATE,Date)
    finalization_date=Column(TABLE_DELIVERY_FINALIZATION_DATE,Date)
    id_service_order=Column(TABLE_DELIVERY_ID_SERVICE_ORDER,Integer,ForeignKey(Service_order.id,onupdate="CASCADE", ondelete="CASCADE"))
    id_package=Column(TABLE_DELIVERY_ID_PACKAGE,Integer,ForeignKey(Package.id,onupdate="CASCADE", ondelete="CASCADE"))


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


def saveAdress(json_adress):

    Session = getSession()
    session=Session()
    adress = Adress()
    adress.street=json_adress[TABLE_ADRESS_STREET]
    adress.number=json_adress[TABLE_ADRESS_NUMBER]
    adress.complement=json_adress[TABLE_ADRESS_COMPLEMENT]
    adress.district=json_adress[TABLE_ADRESS_DISTRICT]
    adress.postal_code=json_adress[TABLE_ADRESS_POSTAL_CODE]
    adress.city=json_adress[TABLE_ADRESS_CITY]
    adress.state=json_adress[TABLE_ADRESS_STATE]
    adress.country=json_adress[TABLE_ADRESS_COUNTRY]
    session.add(adress)
    session.commit()
    session.refresh(adress)
    id=adress.id
    session.close()
    return id

def deleteAdress(id):
    Session = getSession()
    session=Session()
    session.query(Adress).filter(Adress.id == id).\
    delete()
    session.commit()
    session.close()

def saveVehicle(json_vehicle0):
    Session= getSession()
    session=Session()
    vehicle=Vehicle()
    vehicle.licence_plate=json_vehicle['']
    vehicle.model=json_vehicle['']
    vehicle.year=json_vehicle['']
    vehicle.ready=json_vehicle['']
    vehicle.color=json_vehicle['']
    session.add(vehicle)
    session.commit()
    session.refresh(vehicle)
    id=adress.id
    session.close()
    return id

def saveCompany(json_company):
    id_adress=saveAdress(json_company[TABLE_ADRESS])
    Session=getSession()
    session=Session()
    company=Company()
    company.id_adress=id_adress
    company.name_company=json_company[TABLE_COMPANY_NAME]
    company.password=json_company[TABLE_COMPANY_PASSWORD]
    company.login=json_company[TABLE_COMPANY_LOGIN]
    company.email=json_company[TABLE_COMPANY_EMAIL]
    company.uci=json_company[TABLE_COMPANY_UCI]
    session.add(company)
    try:
        session.commit()
    except:
        deleteAdress(id_adress)
        return False
    session.refresh(company)
    id = company.id
    session.close()
    return id


