"""
main.py

Einstiegspunkt für das Fahrzeug management system.
Zuständig für Menü navigation und Benutzer interaktion.
"""

from fahrzeug import Auto, Motorrad, LKW
from manager import Fahrzeugmanager
from helper import get_text, get_positive_int, get_year


# ---------- Fahrzeug objekte erstellen ----------

def _auto_():
    return Auto(
        get_text("Marke: "),
        get_text("Modell: "),
        get_year("Baujahr: "),
        get_positive_int("Grundpreis: "),
        get_positive_int("Türen: ")
    )


def _motorrad_():
    return Motorrad(
        get_text("Marke: "),
        get_text("Modell: "),
        get_year("Baujahr: "),
        get_positive_int("Grundpreis: "),
        get_positive_int("Motor (cc): ")
    )


def _lkw_():
    return LKW(
        get_text("Marke: "),
        get_text("Modell: "),
        get_year("Baujahr: "),
        get_positive_int("Grundpreis: "),
        get_positive_int("Kapazität (Tonnen): ")
    )


# ---------- Fahrzeugauswahl ----------

def fahrzeug_auswaehlen(manager):

    fahrzeug_typ = {
        "1": _auto_,
        "2": _motorrad_,
        "3": _lkw_
    }

    print("\nFahrzeugtyp wählen:")
    print("1 → Auto")
    print("2 → Motorrad")
    print("3 → LKW")

    choice = input("Auswahl: ")

    typ_erstellen = fahrzeug_typ.get(choice)

    if typ_erstellen:
        manager.fahrzeug_hinzufügen(typ_erstellen())
    else:
        print("Ungültige Auswahl!")


# ---------- Main menu ----------

def main():

    manager = Fahrzeugmanager()

    while True:

        print("\n=== Fahrzeugverwaltung ===")
        print("1 → Fahrzeug hinzufügen")
        print("2 → Fahrzeuge anzeigen")
        print("3 → Sortieren")
        print("4 → Gesamtwert")
        print("5 → Fahrzeug suchen (ID)")
        print("6 → Fahrzeug löschen (ID)")
        print("7 → Beenden")

        choice = input("Auswahl: ")

        if choice == "1":
            fahrzeug_auswaehlen(manager)

        elif choice == "2":
            manager.fahrzeuge_anzeigen()

        elif choice == "3":
            manager.sort_nach_marke()

        elif choice == "4":
            manager.gesamtflottenwert()

        elif choice == "5":
            vid = get_positive_int("ID eingeben: ")
            manager.suche_nach_id(vid)

        elif choice == "6":
            vid = get_positive_int("ID eingeben: ")
            manager.fahrzeug_löschen(vid)

        elif choice == "7":
            print("Programm beendet.")
            break

        else:
            print("Ungültige Eingabe!")


if __name__ == "__main__":
    main()
