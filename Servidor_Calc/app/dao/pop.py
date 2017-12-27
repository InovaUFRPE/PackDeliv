#!/usr/bin/python3.5
"""Populator module."""

from random import randint


class Package:
    """Package model class."""

    def __init__(self, width, height, lenght, weight, adress):
        """Initialization for Package object."""
        self.width = width
        self.height = height
        self.lenght = lenght
        self.weight = weight
        self.adress = adress


class Adress:
    """Adress model class."""

    def __init__(self, street, number, complement, district, postal_code, city, state, country):
        """Initialization for Adress object."""
        self.street = street
        self.number = number
        self.complement = complement
        self.district = district
        self.postal_code = postal_code
        self.city = city
        self.state = state
        self.country = country

def popular():
    """Popula o 'banco de dados'."""
    bairro1 = "areias"
    bairro2 = "marcos freire"
    bairro3 = "maraguape 2"

    adress1 = Adress("rua quinze", 182, "", bairro3, "53421-081", "paulista", "pe", "brasil")
    adress2 = Adress('avenida recife', 308, '', bairro1, '54360-160', 'recife', 'pe', 'brasil')
    adress3 = Adress("avenida barreto de menezes", 100, "c", bairro2, "50860-000", "jaboatao dos guararapes", "pe", "brasil")
    adress4 = Adress("rua quinze", 174, "", bairro3, "53421-081", "paulista", "pe", "brasil")
    adress5 = Adress('avenida recife', 309, '', bairro1, '54360-160', 'recife', 'pe', 'brasil')
    adress6 = Adress("avenida barreto de menezes", 101, "a", bairro2, "50860-000", "jaboatao dos guararapes", "pe", "brasil")

    list_adress = [adress1, adress2, adress3, adress4, adress5, adress6]
    list_bairro1 = []
    list_bairro2 = []
    list_bairro3 = []
    list_package = {}

    for i in range(12):
        p = Package()
        p.adress = list_adress[i % 6]
        p.height = randint(1, 10)
        p.lenght = randint(1, 10)
        p.width = randint(1, 10)
        p.weight = randint(10, 50)
        if p.adress.district == bairro1:
            list_bairro1.append(p)
        elif p.adress.district == bairro2:
            list_bairro2.append(p)
        else:
            list_bairro3.append(p)

    list_package['bairro1'] = list_bairro1
    list_package['bairro2'] = list_bairro2
    list_package['bairro3'] = list_bairro3

    return list_package
