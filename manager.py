"""
manager.py

Speichert, sucht, löscht und meldet Fahrzeugdaten.
Verwendet eine wörterbuchbasierte ID-Speicherung.
"""


class Fahrzeugmanager:
    """Verwaltet Fahrzeuge, die anhand einer eindeutigen ID gespeichert sind."""

    def __init__(self):
        self.vehicles = {}
        self.next_id = 1

    # ---------- speichern ----------

    def fahrzeug_hinzufügen(self, vehicle):
        vid = self.next_id
        self.vehicles[vid] = vehicle
        self.next_id += 1
        print(f"Fahrzeug gespeichert mit ID: {vid}")

    # ---------- anzeigen ----------

    def fahrzeuge_anzeigen(self):
        if not self.vehicles:
            print("\nKeine Fahrzeuge vorhanden.")
            return

        print("\n=== Fahrzeugliste ===")

        for vid, vehicle in self.vehicles.items():
            print(f"\nID: {vid}")
            vehicle.display_info()
            print("-------------------")

    # ---------- suchen ----------

    def suche_nach_id(self, vid):
        vehicle = self.vehicles.get(vid)

        if vehicle:
            print("Fahrzeug gefunden:")
            vehicle.display_info()
        else:
            print("Fahrzeug aktuell nicht verfügbar.")

    # ---------- löschen ----------

    def fahrzeug_löschen(self, vid):
        if vid in self.vehicles:
            del self.vehicles[vid]
            print("Fahrzeug gelöscht.")
        else:
            print("Fahrzeug aktuell nicht verfügbar.")

    # ---------- Sortierung ----------

    def sort_nach_marke(self):

        def get_marke(item):
            return item[1].marke

        items = list(self.vehicles.items())
        items.sort(key=get_marke)

        self.vehicles = dict(items)
        print("Nach Marke sortiert")

    # ---------- flotten wert ----------

    def gesamtflottenwert(self):
        total = sum(v.kosten_berechnen() for v in self.vehicles.values())
        print(f"Gesamtwert: {total} €")
