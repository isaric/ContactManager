# all domain classes should be defined here
import random

class Address:
    
    def __init__(self, city, street, country, postal_code):
        self.city = city
        self.street = street
        self.contry = country
        self.postal_code = postal_code

    def __repr__(self):
        d = self.__dict__
        line = ""
        for value in d.values():
            line += f"{value}\t"
        return line


class Person:

    def __init__(self, oib, address):
        self.oib = oib
        self.address = address

class NaturalPerson(Person):

    def __init__(self, oib, address, f_name, l_name, dob):
        super().__init__(oib, address)
        self.f_name = f_name
        self.l_name = l_name
        self.dob = dob


class Employee(NaturalPerson):

    def __init__(self, f_name, l_name, dob, address, oib, position):
        super().__init__(oib, address, f_name, l_name, dob)
        self.position = position

class Customer(NaturalPerson):
    
    def __init__(self, f_name, l_name, dob, address, oib):
        super().__init__(oib, address, f_name, l_name, dob)

class Company(Person):

    def __init__(self, name, oib, address, iban, tax_nr):
        super().__init__(oib, address)
        self.name = name
        self.iban = iban
        self.tax_code = tax_nr
        self.employees = []
        self.customer = []
        self.products = []
        

class Product:
    
    def __init__(self, code, name, description, price):
        self.code = code
        self.name = name
        self.description = description
        self.price = price

#this is our composite class that will
#hold all other objects
class ContactManager:
    
    def __init__(self):
        self.companies = []
        self.oibs = []

    def create_company(self, name, iban, address):
        oib = self._generate_oib_()
        cmpny = Company(name, oib , address, iban, "HR" + oib)
        self.companies.append(cmpny)

    def _generate_oib_(self):
        result = ""
        for i in range(11):
            digit = random.randint(0, 9)
            result += str(digit)
        if result in self.oibs:
            result = self.generate_oib()
            self.oibs.append(result)
        return result
    
