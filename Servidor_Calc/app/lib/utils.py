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

# def popular():
#     """Popula o 'banco de dados'."""

#     # Bairros
#     bairro1 = "Maranguape 2"
#     bairro2 = "Areias"
#     bairro3 = "Marcos Freire"
#     bairro4 = "Espinheiro"
#     bairro5 = "Torre"
#     bairro6 = "Bairro Novo"
#     bairro7 = "Piedade"
#     bairro8 = "Graças"
#     bairro9 = "Candeias"
#     bairro10 = "Boa Vista"

#     # Ruas
#     """Maranguape 2"""
#     rua1 = "Rua Quinze"
#     rua2 = "Rua Doze"
#     rua3 = "Rua Catorze"

#     """Areias"""
#     rua4 = "Avenida Recife"
#     rua5 = "Rua Ipojuca"
#     rua6 = "Rua Barros Sobrinho"

#     """Marcos Freire"""
#     rua7 = "Avenida Barreto de Menezes"
#     rua8 = "Rua Rio Nilo"
#     rua9 = "Rua Rio Madeira"

#     """Espinheiro"""
#     rua10 = "Rua Quarenta e Oito"
#     rua11 = "Rua Santo Elias"
#     rua12 = "Rua Alfredo de Medeiros"

#     """Torre"""
#     rua13 = "Rua João de Deus"
#     rua14 = "Rua José de Holanda"
#     rua15 = "Rua Real da Torre"

#     """Bairro Novo"""
#     rua16 = "Rua Alberto Lundgren"
#     rua17 = "Rua Luís de Carvalho"
#     rua18 = "Rua Maria Ramos"

#     """Piedade"""
#     rua19 = "Rua Pernambuco"
#     rua20 = "Rua Garanhuns"
#     rua21 = "Rua Aracatu"

#     """Graças"""
#     rua22 = "Rua Amélia"
#     rua23 = "Rua da Amizade"
#     rua24 = "Rua das Graças"

#     """Candeias"""
#     rua25 = "Rua do Jangadeiro"
#     rua26 = "Rua Buriti"
#     rua27 = "Rua Caratinga"

#     """Boa Vista"""
#     rua28 = "Rua da Conceição"
#     rua29 = "Rua do Aragão"
#     rua30 = "Rua do Riachuelo"

#     # Ceps
#     cep1 = "54431-100"
#     cep2 = "54232-501"
#     cep3 = "50438-052"
#     cep4 = "54433-703"
#     cep5 = "54430-004"
#     cep6 = "54632-905"
#     cep7 = "52336-806"
#     cep8 = "51937-707"
#     cep9 = "56730-708"
#     cep10 = "55632-709"
#     cep11 = "54789-710"
#     cep12 = "55637-611"
#     cep13 = "57431-612"
#     cep14 = "58960-313"
#     cep15 = "54356-614"
#     cep16 = "52456-315"
#     cep17 = "57483-516"
#     cep18 = "56563-500"
#     cep19 = "55939-315"
#     cep20 = "59851-436"
#     cep21 = "54432-323"
#     cep22 = "51230-221"
#     cep23 = "52330-110"
#     cep24 = "59230-323"
#     cep25 = "58430-324"
#     cep26 = "58631-325"
#     cep27 = "54733-326"
#     cep28 = "56234-327"
#     cep29 = "59327-328"
#     cep30 = "54033-329"

#     # Cidades
#     cidade1 = "Paulista"
#     cidade2 = "Recife"
#     cidade3 = "Jaboatão dos Guararapes"
#     cidade4 = "Olinda"

#     # Endereços
#     address1 = Address(rua1, 182, "", bairro1, cep1, cidade1, "pe", "brasil")
#     address2 = Address(rua2, 308, "", bairro2, cep2, cidade2, 'pe', 'brasil')
#     address3 = Address(rua3, 100, "c", bairro3, cep3, cidade3, "pe", "brasil")
#     address4 = Address(rua1, 174, "", bairro1, cep1, cidade1, "pe", "brasil")
#     address5 = Address(rua2, 309, "", bairro2, cep2, cidade2, 'pe', 'brasil')
#     address6 = Address(rua3, 101, "a", bairro3, cep3, cidade3, "pe", "brasil")
#     address7 = Address(rua1, 123, "", bairro1, cep1, cidade1, "pe", "brasil")
#     address8 = Address(rua2, 456, "", bairro1, cep2, cidade1, "pe", "brasil")
#     address9 = Address(rua3, 789, "", bairro1, cep3, cidade1, "pe", "brasil")
#     address10 = Address(rua4, 908, "", bairro2, cep4, cidade2, "pe", "brasil")
#     address11 = Address(rua5, 765, "", bairro2, cep5, cidade2, "pe", "brasil")
#     address12 = Address(rua6, 432, "", bairro2, cep6, cidade2, "pe", "brasil")
#     address13 = Address(rua7, 213, "", bairro3, cep7, cidade3, "pe", "brasil")
#     address14 = Address(rua8, 526, "", bairro3, cep8, cidade3, "pe", "brasil")
#     address15 = Address(rua9, 662, "", bairro3, cep9, cidade3, "pe", "brasil")
#     address16 = Address(rua10, 721, "", bairro4, cep10, cidade2, "pe", "brasil")
#     address17 = Address(rua11, 922, "", bairro4, cep11, cidade2, "pe", "brasil")
#     address18 = Address(rua12, 833, "", bairro4, cep12, cidade2, "pe", "brasil")
#     address19 = Address(rua13, 129, "", bairro5, cep13, cidade2, "pe", "brasil")
#     address20 = Address(rua14, 222, "", bairro5, cep14, cidade2, "pe", "brasil")
#     address21 = Address(rua15, 113, "", bairro5, cep15, cidade2, "pe", "brasil")
#     address22 = Address(rua16, 114, "", bairro6, cep16, cidade4, "pe", "brasil")
#     address23 = Address(rua17, 115, "", bairro6, cep17, cidade4, "pe", "brasil")
#     address24 = Address(rua18, 116, "", bairro6, cep18, cidade4, "pe", "brasil")
#     address25 = Address(rua19, 117, "", bairro7, cep19, cidade3, "pe", "brasil")
#     address26 = Address(rua20, 118, "", bairro7, cep20, cidade3, "pe", "brasil")
#     address27 = Address(rua21, 119, "", bairro7, cep21, cidade3, "pe", "brasil")
#     address28 = Address(rua22, 110, "", bairro8, cep22, cidade2, "pe", "brasil")
#     address29 = Address(rua23, 111, "", bairro8, cep23, cidade2, "pe", "brasil")
#     address30 = Address(rua24, 129, "", bairro8, cep24, cidade2, "pe", "brasil")


#     list_address = [address1, address2, address3, address4, address5, address6, address7, address8, address9, address10, address11, address12, address13, address14, address15, address16, address17, address18, address19, address20, address21, address22,address23, address24, address25, address26, address27, address28, address29, address30]
#     list_bairro1 = []
#     list_bairro2 = []
#     list_bairro3 = []
#     list_bairro4 = []
#     list_bairro5 = []
#     list_bairro6 = []
#     list_bairro7 = []
#     list_bairro8 = []
#     list_bairro9 = []
#     list_bairro10 = []
#     list_package = {}

#     for i in range(12):
#         p = Package(width=randint(1, 10), height=randint(1, 10), lenght=randint(1, 10), weight=randint(10, 25), address=list_address[i % 6].get())
#         if p.address['district'] == bairro1:
#             list_bairro1.append(p)
#         elif p.address['district'] == bairro2:
#             list_bairro2.append(p)
#         elif p.address['district'] == bairro3:
#             list_bairro3.append(p)
#         elif p.address['district'] == bairro4:
#             list_bairro4.append(p)
#         elif p.address['district'] == bairro5:
#             list_bairro5.append(p)
#         elif p.address['district'] == bairro6:
#             list_bairro6.append(p)
#         elif p.address['district'] == bairro7:
#             list_bairro7.append(p)
#         elif p.address['district'] == bairro8:
#             list_bairro8.append(p)
#         elif p.address['district'] == bairro9:
#             list_bairro9.append(p)
#         else:
#             list_bairro10.append(p)

#     list_package['bairro1'] = list_bairro1
#     list_package['bairro2'] = list_bairro2
#     list_package['bairro3'] = list_bairro3
#     list_package['bairro4'] = list_bairro4
#     list_package['bairro5'] = list_bairro5
#     list_package['bairro6'] = list_bairro6
#     list_package['bairro7'] = list_bairro7
#     list_package['bairro8'] = list_bairro8
#     list_package['bairro9'] = list_bairro9
#     list_package['bairro10'] = list_bairro10

#     return list_package


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
