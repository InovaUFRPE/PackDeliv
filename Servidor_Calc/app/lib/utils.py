#!/usr/bin/python3.5
"""Library for utilities functions for the calc server."""

from random import randint
from datetime import datetime, timedelta


class LatLng:
    """Class for use with coordinates."""

    def __init__(self, coordinates):
        """Init the LatLng object."""
        splited_coords = coordinates.split(';')
        self.__lat = int(splited_coords[0])
        self.__lng = int(splited_coords[1])

    def get_lat(self):
        """Get latitude value."""
        return self.__lat

    def get_lng(self):
        """Get longitude value."""
        return self.__lng


class Package:
    """Package model class."""

    __ID = 0

    def __init__(self, width, height, lenght, weight, address, final_date):
        """Initialization for Package object."""
        self.width = width
        self.height = height
        self.lenght = lenght
        self.weight = weight
        self.vol = self.width * self.height * self.lenght
        self.start_date = datetime.now()
        self.final_date = final_date
        self.address = address
        self.id = Package.__ID + 1
        Package.__ID += 1

    def get(self):
        """Representation method for Package."""
        return vars(self)


class Address:
    """Adress model class."""

    def __init__(self, street, number, complement, district, postal_code, city, state, country):
        """Initialization for Address object."""
        self.street = street
        self.number = number
        self.complement = complement
        self.district = district
        self.postal_code = postal_code
        self.city = city
        self.state = state
        self.country = country

    def get(self):
        """Representation method for Package."""
        return vars(self)


class ServiceOrder:
    """ServiceOrder model class"""

    __ID = 0
    __CODE = 100000

    def __init__(self, deliveries, shipping_date, finalization_date):
        """Initialization for ServiceOrder object."""
        self.deliveries = deliveries
        self.id = ServiceOrder.__ID + 1
        ServiceOrder.__ID += 1
        self.code = ServiceOrder.__CODE + 1
        ServiceOrder.__CODE += 1
        self.shipping_date = shipping_date
        self.finalization_date = finalization_date

    def get(self):
        """Representation method for Package."""
        return vars(self)


def popular():
    """Popula o 'banco de dados'."""

    # Bairros
    bairros = ["Maranguape 2", "Areias", "Marcos Freire", "Espinheiro", "Torre", "Bairro Novo", "Piedade", "Graças", "Candeias", "Boa Vista"]

    # Ruas
    ruas = ["Rua Quinze", "Rua Catorze", "Rua Doze", "Avenida Recife", "Rua Ipojuca", "Rua Barros Sobrinho", "Avenida Barreto de Menezes", "Rua Rio Nilo", "Rua Rio Madeira", "Rua Quarenta e Oito"]
    ruas2 = ["Rua Santo Elias", "Rua Alfredo de Medeiros", "Rua João de Deus", "Rua José de Holanda", "Rua Real da Torre", "Rua Alberto Lundgren", "Rua Luís de Carvalho", "Rua Maria de Ramos", "Rua Pernambuco", "Rua Garanhuns"]
    ruas3 = ["Rua Aracatu", "Rua Amélia", "Rua da Amizade", "Rua das Graças", "Rua do Jangadeiro", "Rua Buriti", "Rua Caratinga", "Rua da Conceição", "Rua do Aragão", "Rua do Riachuelo"]
    ruas.extend(ruas2)
    ruas.extend(ruas3)

    # Ceps
    ceps = ["54431-100", "54232-501", "50438-052", "54433-703", "54430-004", "54632-905", "52336-806", "51937-707", "56730-708", "55632-709"]
    ceps2 = ["54789-710", "55637-611", "57431-612", "58960-313", "54356-614", "52456-315", "57483-516", "56563-500", "55939-315", "59851-436"]
    ceps3 = ["54432-323", "51230-221", "52330-110", "59230-323", "58430-324", "58631-325", "54733-326", "56234-327", "59327-328", "54033-329"]
    ceps.extend(ceps2)
    ceps.extend(ceps3)

    # Cidades
    cidades = ["Paulista", "Recife", "Jaboatão dos Guararapes", "Olinda"]

    # Endereços
    list_address = []
    for i in range(30):
        new_address = Address(ruas[i], randint(1, 3000), '', bairros[i % 10], ceps[i], cidades[i % 4], 'pe', 'brasil')
        list_address.append(new_address)

    # Lista de pacotes separados por bairro (índice)
    # list_bairros = [[]] * 10 <- não declarar assim senão todas as listas serão modificadas ao mesmo tempo
    list_bairros = [ [], [], [], [], [], [], [], [], [], []]
    for i in range(30):
        final_date = datetime.now() + timedelta(days=randint(1, 5))
        p = Package(width=randint(1, 10), height=randint(1, 10), lenght=randint(1, 10), weight=randint(10, 25), address=list_address[i].get(), final_date=final_date)
        list_bairros[i % 10].append(p)

    # Dicionário de pacotes por bairro (string)
    list_package = {}
    for i in range(10):
        list_package[bairros[i]] = list_bairros[i]

    return list_package
