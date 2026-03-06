"""
helper.py

Wiederverwendbare Eingabe validierungs funktionen.
"""


def get_text(txt):
    while True:
        value = input(txt)
        if value:
            return value
        print("Eingabe darf nicht leer sein!")


def get_positive_int(prompt):
    while True:
        user_input = input(prompt)

        if user_input.isdigit():     # checks if only digits
            num = int(user_input)

            if num > 0:
                return num

            print("Zahl muss positiv sein!")

        else:
            print("Ungültige Zahl!")


def get_year(yr):
    while True:
        year = get_positive_int(yr)
        if 1900 <= year <= 2100:
            return year
        print("Ungültiges Baujahr!")
