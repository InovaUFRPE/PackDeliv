#!/usr/bin/python3.5
"""Library for utilities functions for the calc server."""

from random import randint


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

    def __init__(self, width, height, lenght, weight, address):
        """Initialization for Package object."""
        self.width = width
        self.height = height
        self.lenght = lenght
        self.weight = weight
        self.vol = self.width * self.height * self.lenght
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


def popular():
    """Popula o 'banco de dados'."""
    bairro1 = "areias"
    bairro2 = "marcos freire"
    bairro3 = "maraguape 2"

    rua1 = "rua quinze"
    rua2 = "avenida recife"
    rua3 = "avenida barreto de menezes"

    cep1 = "53421-081"
    cep2 = "54360-160"
    cep3 = "50860-000"

    cidade1 = "paulista"
    cidade2 = "recife"
    cidade3 = "jaboatao dos guararapes"

    address1 = Address(rua1, 182, "", bairro3, cep1, cidade1, "pe", "brasil")
    address2 = Address(rua2, 308, "", bairro1, cep2, cidade2, 'pe', 'brasil')
    address3 = Address(rua3, 100, "c", bairro2, cep3, cidade3, "pe", "brasil")
    address4 = Address(rua1, 174, "", bairro3, cep1, cidade1, "pe", "brasil")
    address5 = Address(rua2, 309, "", bairro1, cep2, cidade2, 'pe', 'brasil')
    address6 = Address(rua3, 101, "a", bairro2, cep3, cidade3, "pe", "brasil")

    list_address = [address1, address2, address3, address4, address5, address6]
    list_bairro1 = []
    list_bairro2 = []
    list_bairro3 = []
    list_package = {}

    for i in range(12):
        p = Package(width=randint(1, 10), height=randint(1, 10), lenght=randint(1, 10), weight=randint(10, 25), address=list_address[i % 6].get())
        if p.address['district'] == bairro1:
            list_bairro1.append(p)
        elif p.address['district'] == bairro2:
            list_bairro2.append(p)
        else:
            list_bairro3.append(p)

    list_package['bairro1'] = list_bairro1
    list_package['bairro2'] = list_bairro2
    list_package['bairro3'] = list_bairro3

    return list_package
