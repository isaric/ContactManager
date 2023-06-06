# implement all auxiliary and input functions here

from models import Address, ContactManager


menu_1 = """
#########################################

    Contact Manager Aplikacija

        Glavni Izbornik

    1 - Stvori novu tvrtku

    2 - Odaberi tvrtku

    3 - Izlaz

    Napišite broj ispred vašeg izbora

#########################################
"""

company_menu = """
#########################################
            {tvrka.naziv}

    1 - Rad s zaposlenicima

    2 - Rad s strankama

    3 - Rad s proizvodima

    4 - Povratak

    Napišite broj ispred vašeg izbora

#########################################
"""

hashtag_line = "#################################"

employee_menu = """
    1 - Unesi novog zaposlenika

    2 - Obriši postojećeg zaposlenika

    3 - Izmjeni postojećeg zaposlenika

    4 - Povratak
"""

customer_menu = """
    1 - Unesi novu stranku

    2 - Obriši postojeću stranku

    3 - Izmjeni postojeću stranku

    4 - Povratak
"""

product_menu = """
    1 - Unesi novi proizvod

    2 - Obriši postojeći proizvod

    3 - Izmjeni postojeći proizvod

    4 - Povratak
"""

employee_header = """
    OIB\tIme\tPrezime\tDatum_Rodnjena\tPozicija\tUlica\tGrad\tDržava\tPoštanski Broj
"""

customer_header = """
    OIB\tIme\tPrezime\tDatum_Rodnjena\tUlica\tGrad\tDržava\tPoštanski Broj
"""

company_header = """OIB\tIme\tIBAN\tUlica\tGrad\tDržava\tPoštanski Broj
"""

product_header = """\tKod\tIme\tOpis\t\tCijena"""


def main_menu():
    cm = ContactManager()
    while True:
        print(menu_1)
        choice=input("\n")
        if choice == "1":
            create_company(cm)
        elif choice == "2":
            choose_company(cm)
        elif choice == "3":
            exit()

def create_address():

    street = input("Unesite ulicu i broj:\n")
    city = input("Unesite grad:\n")
    pc = input("Unesite poštanski broj:\n")
    country = input("Unesite naziv države:\n")

    return Address(city, street, country, pc)


def create_company(cmgr):
    name = input("Unesite ime tvrtke:\n")
    iban = input("Unesite iban tvrtke:\n")
    address = create_address()
    cmgr.create_company(name, iban, address)

def choose_company(cmgr):
    print()
    print()
    print(company_header)
    for company in cmgr.companies:
        cd = company.__dict__
        c_line = ""
        for value in cd.values():
            c_line += f"{value}\t"
        print(c_line)

    print()
    print()