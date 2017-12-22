from sqlalchemy import create_engine, Column, Integer, String,Boolean, ForeignKey,Date,DateTime
#from geoalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
import datetime
from Rest_utils.entities_atributes_Names import *  #(dont work in RestApi.py -->fix it)

Base = declarative_base()

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
    #add coluna de localização



class Vehicle(Base):
    __tablename__= VEHICLE

    id= Column(VEHICLE_ID,Integer,primary_key=True)
    licence_plate = Column(VEHICLE_LICENSE_PLATE, String(255),unique=True, nullable=False)
    year=Column(VEHICLE_YEAR, Integer,nullable=False)
    model = Column(VEHICLE_MODEL,String(255),nullable=False)
    color =Column(VEHICLE_COLOR,String(255))
    ready=Column(VEHICLE_READY, Boolean, default=False)

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

class Deliveryman(Company):
    __tablename__=DELIVERYMAN
    id = Column(DELIVERYMAN_ID,Integer, ForeignKey(Company.id), primary_key=True)
    name_deliveryman=Column(DELIVERYMAN_NAME,String(255),nullable=False)
    Id_veiculo=Column(DELIVERYMAN_ID_VEHICLE,Integer,ForeignKey(Vehicle.id,onupdate="CASCADE", ondelete="CASCADE"))
    #id_company=Column(DELIVERYMAN_ID_COMPANY,Integer,ForeignKey(Company.id,onupdate="CASCADE", ondelete="CASCADE"))
    dui=Column(DELIVERYMAN_DUI,String(255),unique=True,nullable=False)
    status=Column(DELIVERYMAN_STATUS,Boolean, default=False)
    ready=Column(DELIVERYMAN_READY,Boolean, default=False)
    #localization = GeometryColumn(DELIVERYMAN_LOCALIZATION,Point(2))

    __mapper_args__ = {
        'polymorphic_identity':DELIVERYMAN,
    }

class Service_order(Base):
    __tablename__=SERVICE_ORDER

    id=Column(SERVICE_ORDER_ID, Integer, primary_key=True)
    #code=Column(SERVICE_ORDER_IDENTIFIER_CODE,String(255),unique=True,nullable=False)
    shipping_date=Column(SERVICE_ORDER_SHIPPING_DATE,Date)
    finalization_date=Column(SERVICE_ORDER_FINALIZATION_DATE,Date)
    #list_package = relationship('Package')

class Package(Base):
    __tablename__ = PACKAGE
    id=Column(PACKAGE_ID, Integer, primary_key=True)
    width=Column(PACKAGE_WIDTH,Integer,nullable=False)
    height=Column(PACKAGE_HEIGHT,Integer,nullable=False)
    length=Column(PACKAGE_LENGTH,Integer,nullable=False)
    weight=Column(PACKAGE_WEIGHT,Integer,nullable=False)
    shiped=Column(PACKAGE_SHIPPED,Boolean, default=False)
    received=Column(PACKAGE_RECEIVED,Boolean, default=False)
    id_adress_start=Column(PACKAGE_ID_START_ADRESS,Integer)
    id_adress_destiny=Column(PACKAGE_ID_ADRESS,Integer)
    static_location=Column(PACKAGE_CURRENT_STATIC_LOCATION,String(255))
    started_date = Column(DateTime, default=datetime.datetime.utcnow)
    Service_order_id = Column(Integer , ForeignKey('Service_order.id'))

class Delivery(Base):
    __tablename__=DELIVERY

    id=Column(DELIVERY_ID, Integer, primary_key=True)
    code=Column(DELIVERY_IDENTIFIER_CODE, String(255))
    shipping_date=Column(DELIVERY_SHIPPING_DATE,Date)
    finalization_date=Column(DELIVERY_FINALIZATION_DATE,Date)
    id_service_order=Column(DELIVERY_ID_SERVICE_ORDER,Integer,ForeignKey(Service_order.id,onupdate="CASCADE", ondelete="CASCADE"))
    id_package=Column(DELIVERY_ID_PACKAGE,Integer,ForeignKey(Package.id,onupdate="CASCADE", ondelete="CASCADE"))


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
    adress.street=json_adress[ADRESS_STREET]
    adress.number=json_adress[ADRESS_NUMBER]
    adress.complement=json_adress[ADRESS_COMPLEMENT]
    adress.district=json_adress[ADRESS_DISTRICT]
    adress.postal_code=json_adress[ADRESS_POSTAL_CODE]
    adress.city=json_adress[ADRESS_CITY]
    adress.state=json_adress[ADRESS_STATE]
    adress.country=json_adress[ADRESS_COUNTRY]
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

def getAdress(id):
    Session = getSession()
    session=Session()
    response=session.query(Adress).filter(Adress.id == id).all()
    if len(response)==1:
        r=response[0]
        adress={ADRESS_ID : r.id, ADRESS_STREET : r.street,ADRESS_NUMBER : r.number, ADRESS_COMPLEMENT : r.complement, ADRESS_DISTRICT : r.district, ADRESS_POSTAL_CODE :r.postal_code,ADRESS_CITY :  r.city, ADRESS_STATE : r.state, ADRESS_COUNTRY : r.country}
        return {"response" : adress }
    else:
        return {"response" : "invalid adress"}

def editAdress(json_adress):
    Session = getSession()
    session=Session()
    id=json_adress[ADRESS_ID]
    response=session.query(Adress).filter(Adress.id == id).all()

    if len(response)==1:
        adress=response[0]
        adress.street=json_adress[ADRESS_STREET]
        adress.number=json_adress[ADRESS_NUMBER]
        adress.complement=json_adress[ADRESS_COMPLEMENT]
        adress.district=json_adress[ADRESS_DISTRICT]
        adress.postal_code=json_adress[ADRESS_POSTAL_CODE]
        adress.city=json_adress[ADRESS_CITY]
        adress.state=json_adress[ADRESS_STATE]
        adress.country=json_adress[ADRESS_COUNTRY]
        session.add(adress)
        session.commit()
        session.refresh(adress)
        session.close()
        return {"response" : adress }
    else:
        return {"response" : "invalid adress"}

def saveVehicle(json_vehicle):
    Session= getSession()
    session=Session()
    vehicle=Vehicle()
    vehicle.licence_plate=json_vehicle[VEHICLE_LICENSE_PLATE]
    vehicle.model=json_vehicle[VEHICLE_MODEL]
    vehicle.year=json_vehicle[VEHICLE_YEAR]
    #vehicle.ready=json_vehicle['']
    #vehicle.color=json_vehicle['']
    session.add(vehicle)
    session.commit()
    session.refresh(vehicle)
    id=vehicle.id
    session.close()
    return id



def saveDeliveryman(json_deliveryman):
    id_adress=saveAdress(json_deliveryman[ADRESS])
    id_vehicle=saveVehicle(json_deliveryman[VEHICLE])
    Session=getSession()
    session=Session()
    deliveryman=Deliveryman()

    deliveryman.dui=json_deliveryman[DELIVERYMAN_DUI]
    deliveryman.Id_veiculo=id_vehicle
    deliveryman.id_adress=id_adress
    deliveryman.name_company=json_deliveryman[COMPANY_NAME]
    deliveryman.name_deliveryman=json_deliveryman[DELIVERYMAN_NAME]
    deliveryman.password=json_deliveryman[COMPANY_PASSWORD]
    deliveryman.login=json_deliveryman[COMPANY_LOGIN]
    deliveryman.email=json_deliveryman[COMPANY_EMAIL]
    deliveryman.uci=json_deliveryman[COMPANY_UCI]

    session.add(deliveryman)
    response = False
    session.commit()
    session.refresh(deliveryman)
    response = deliveryman.id
    #deleteAdress(id_adress)

    session.close()
    return response

def savePackage(json_package):
    print(json_package)
    Session=getSession()
    session=Session()
    package=Package()

    package.width=json_package[PACKAGE_WIDTH]
    package.height=json_package[PACKAGE_HEIGHT]
    package.length=json_package[PACKAGE_LENGTH]
    package.weight=json_package[PACKAGE_WEIGHT]
    package.local_destiny=json_package[PACKAGE_LOCAL_DESTINY]
    package.local_start=json_package[PACKAGE_LOCAL_START]
    package.id_adress_start=json_package[PACKAGE_ID_START_ADRESS]

    #package.id_adress_destiny=json_package[PACKAGE_ID_ADRESS]
    #package.static_location=json_package[PACKAGE_CURRENT_STATIC_LOCATION]

    session.add(package)
    response=False

    session.commit()
    session.refresh(package)
    response = package.id
    session.close()
    return response

def getPackages(id):
    Session=getSession()
    session=Session()
    response= session.query(Package).filter(Package.id_adress_start==id).all()
    listPackage=[{PACKAGE_ID : p.id,PACKAGE_WIDTH:p.width,PACKAGE_HEIGHT:p.height,PACKAGE_LENGTH:p.length,PACKAGE_WEIGHT:p.weight,PACKAGE_RECEIVED:p.received,PACKAGE_LOCAL_DESTINY: getAdress(p.id_adress_destiny) ,PACKAGE_LOCAL_START:getAdress(p.id_adress_destiny)} for p in response]
    return listPackage




def saveCompany(json_company):
    id_adress=saveAdress(json_company[ADRESS])
    Session=getSession()
    session=Session()
    company=Company()
    company.id_adress=id_adress
    company.name_company=json_company[COMPANY_NAME]
    company.password=json_company[COMPANY_PASSWORD]
    company.login=json_company[COMPANY_LOGIN]
    company.email=json_company[COMPANY_EMAIL]
    company.uci=json_company[COMPANY_UCI]
    session.add(company)
    response = False
    try:
        session.commit()
        session.refresh(company)
        response = company.id
    except:
        deleteAdress(id_adress)

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

def editCompany(json_company):
    Session=getSession()
    session=Session()
    id=json_company[COMPANY_ID]
    response= session.query(Company).filter(Company.id == id).all()
    company=response[0]
    json_adress=json_company[ADRESS]
    editAdress(json_adress)
    company.email=json_company[COMPANY_EMAIL]

    session.add(company)
    session.commit()
    session.close()
    return True

#Criando Endereço para a Combinação

#endereço 1 = {"Id":"" , "Logradouro":"adm123" }
