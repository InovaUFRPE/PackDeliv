#!/usr/bin/python3.5
"""ORM integration module."""

from sqlalchemy import Column, String, Integer, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

import datetime

Base = declarative_base()


PACKAGE = 'Pacote'
PACKAGE_ID = 'Id'
PACKAGE_WIDTH = 'Largura'
PACKAGE_HEIGHT = 'Altura'
PACKAGE_LENGTH = 'Comprimento'
PACKAGE_WEIGHT = 'Peso'
PACKAGE_SHIPPED = 'Expedido'
PACKAGE_RECEIVED = 'Recebido'
PACKAGE_ID_START_ADRESS = 'Id_endereco_inicio'
PACKAGE_ID_ADRESS = 'Id_endereco_final'
PACKAGE_LOCAL_DESTINY = 'Endereco_Destino'
PACKAGE_LOCAL_START = 'Endereco_Inicio'
PACKAGE_CURRENT_STATIC_LOCATION = 'Local_atual_estatico'

SERVICE_ORDER = 'Ordem_de_servico'
SERVICE_ORDER_ID = 'Id'
SERVICE_ORDER_IDENTIFIER_CODE = 'Codigo'
SERVICE_ORDER_SHIPPING_DATE = 'Data_expedicao'
SERVICE_ORDER_FINALIZATION_DATE = 'Data_finalizacao'


class Service_order(Base):
    """Service order table."""

    __tablename__ = SERVICE_ORDER
    id = Column(SERVICE_ORDER_ID, Integer, primary_key=True)
    shipping_date = Column(SERVICE_ORDER_SHIPPING_DATE, DateTime)
    finalization_date = Column(SERVICE_ORDER_FINALIZATION_DATE, DateTime)
    list_package = relationship(PACKAGE)


class Package(Base):
    """Package table."""

    __tablename__ = PACKAGE
    id = Column(PACKAGE_ID, Integer, primary_key=True)
    width = Column(PACKAGE_WIDTH, Integer, nullable=False)
    height = Column(PACKAGE_HEIGHT, Integer, nullable=False)
    length = Column(PACKAGE_LENGTH, Integer, nullable=False)
    weight = Column(PACKAGE_WEIGHT, Integer, nullable=False)
    shiped = Column(PACKAGE_SHIPPED, Boolean, default=False)
    received = Column(PACKAGE_RECEIVED, Boolean, default=False)
    id_adress_start = Column(PACKAGE_ID_START_ADRESS, Integer)
    id_adress_destiny = Column(PACKAGE_ID_ADRESS, Integer)
    static_location = Column(PACKAGE_CURRENT_STATIC_LOCATION, String(255))
    started_date = Column(DateTime, default=datetime.datetime.utcnow)
