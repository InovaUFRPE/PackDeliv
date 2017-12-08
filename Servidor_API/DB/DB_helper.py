from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from Rest_utils.entities_atributes_Names import *  #(dont work in RestApi.py -->fix it)


def getEngine():
    user ="root"
    password="admin"
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


Base = declarative_base()
Session = getSession()

'''class Vehicle(Base):
    __tablename__= VEHICLE

    id= Column(VEHICLE_ID,Integer,primary_key=True)
    licence_plate = Column(VEHICLE_LICENSE_PLATE, String(255),unique=True, nullable=False)
    year=Column(VEHICLE_YEAR, Integer,nullable=False)
    model = Column(VEHICLE_MODEL,String(255),nullable=False)
    color =Column(VEHICLE_COLOR,String(255),nullable=False)
    ready=Column(VEHICLE_READY, Boolean, default=False)


class Deliveryman(Company):
    __tablename__=DELIVERYMAN
    id = Column(DELIVERYMAN_ID,Integer, ForeignKey(Company.id), primary_key=True)
    Id_veiculo=Column(DELIVERYMAN_ID_VEHICLE,Integer,ForeignKey(Vehicle.id,onupdate="CASCADE", ondelete="CASCADE"))
    #id_company=Column(DELIVERYMAN_ID_COMPANY,Integer,ForeignKey(Company.id,onupdate="CASCADE", ondelete="CASCADE"))
    dui=Column(DELIVERYMAN_DUI,Integer,unique=True,nullable=False)
    availability=Column(DELIVERYMAN_AVAILABILITY,Boolean, default=False)
    ready=Column(DELIVERYMAN_READY,Boolean, default=False)
    #localization = GeometryColumn(DELIVERYMAN_LOCALIZATION,Point(2))

    __mapper_args__ = {
        'polymorphic_identity':DELIVERYMAN,
    }

class Service_order(Base):
    __tablename__=SERVICE_ORDER
    
    id=Column(SERVICE_ORDER_ID, Integer, primary_key=True)
    code=Column(SERVICE_ORDER_IDENTIFIER_CODE,String(255),unique=True,nullable=False)
    shipping_date=Column(SERVICE_ORDER_SHIPPING_DATE,Date)
    finalization_date=Column(SERVICE_ORDER_FINALIZATION_DATE,Date)


class Package(Base):
    __tablename__=PACKAGE
    id=Column(PACKAGE_ID, Integer, primary_key=True)
    width=Column(PACKAGE_WIDTH,Integer,nullable=False)
    height=Column(PACKAGE_HEIGHT,Integer,nullable=False)
    length=Column(PACKAGE_LENGTH,Integer,nullable=False)
    weight=Column(PACKAGE_WEIGHT,Integer,nullable=False)
    shiped=Column(PACKAGE_SHIPPED,Boolean, default=False)
    receiveid=Column(PACKAGE_RECEIVED,Boolean, default=False)
    #local_destiny=GeometryColumn(PACKAGE_LOCAL_DESTINY,Point(2))
    #id_adress_destiny=Column(PACKAGE_ID_ADRESS,Integer)
    static_location=Column(PACKAGE_CURRENT_STATIC_LOCATION,String(255),nullable=False)

class Delivery(Base):
    __tablename__=DELIVERY

    id=Column(DELIVERY_ID, Integer, primary_key=True)
    code=Column(DELIVERY_IDENTIFIER_CODE, String(255))
    shipping_date=Column(DELIVERY_SHIPPING_DATE,Date)
    finalization_date=Column(DELIVERY_FINALIZATION_DATE,Date)
    id_service_order=Column(DELIVERY_ID_SERVICE_ORDER,Integer,ForeignKey(Service_order.id,onupdate="CASCADE", ondelete="CASCADE"))
    id_package=Column(DELIVERY_ID_PACKAGE,Integer,ForeignKey(Package.id,onupdate="CASCADE", ondelete="CASCADE"))


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

def saveDeliveryman(json_deliveryman):
    id_adress=saveAdress(json_deliveryman[ADRESS])

    Session=getSession()
    session=Session()
    deliveryman=Deliveryman()

    deliveryman.dui=json_deliveryman[DELIVERYMAN_DUI]

    deliveryman.id_adress=id_adress
    deliveryman.name_company=json_deliveryman[COMPANY_NAME]
    deliveryman.password=json_deliveryman[COMPANY_PASSWORD]
    deliveryman.login=json_deliveryman[COMPANY_LOGIN]
    deliveryman.email=json_deliveryman[COMPANY_EMAIL]
    #deliveryman.uci=json_deliveryman[COMPANY_UCI]
    session.add(deliveryman)
    response = False
    try:
        session.commit()
        session.refresh(deliveryman)
        response = deliveryman.id
    except:
        deleteAdress(id_adress)

    session.close()
    return response

def savePackage(json_package):
    Session=getSession()
    session=Session()
    package=Package()
    package.width=json_package[PACKAGE_WIDTH]
    package.height=json_package[PACKAGE_HEIGHT]
    package.length=json_package[PACKAGE_LENGTH]
    package.weight=json_package[PACKAGE_WEIGHT]
    package.shiped=json_package[PACKAGE_SHIPPED]
    package.receiveid=json_package[PACKAGE_RECEIVED]
    #package.local_destiny=json_package[PACKAGE_LOCAL_DESTINY]
    #package.id_adress_destiny=json_package[PACKAGE_ID_ADRESS]
    package.static_location=json_package[PACKAGE_CURRENT_STATIC_LOCATION]
    session.add(package)
    response=False
    try:
        session.commit()
        session.refresh(package)
        response = package.id
    except:
        deleteAdress(id_adress)    
    session.close()
    return response '''
  
