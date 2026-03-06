"""
fahrzeug.py
Fahrzeugklassen und Preisgestaltung.
"""


# Wörterbuch für zusätzliche Kosten für customization.
pricing_rules = {
    "extra_door_cost": 500,
    "engine_rate": 2,
    "capacity_rate": 3
}

class Fahrzeug:
    """Basisklasse, die ein generisches Fahrzeug repräsentiert."""

    def __init__(self, marke, modell, baujahr, grundpreis):
        self.marke = marke
        self.modell = modell
        self.baujahr = baujahr
        self.grundpreis = grundpreis

    def kosten_berechnen(self):
        """Rückgabe der gesamten Fahrzeugkosten."""
        return self.grundpreis

    def display_info(self):
        """Fahrzeug informationen ausdrucken."""
        print("Marke:", self.marke)
        print("Modell:", self.modell)
        print("Baujahr:", self.baujahr)
        print("Preis:", self.kosten_berechnen(), "€")


class Auto(Fahrzeug):
    """Auto klasse mit Angabe der Türanzahl und Kostenberechnung."""

    def __init__(self, marke, modell, baujahr, grundpreis, tueren):
        super().__init__(marke, modell, baujahr, grundpreis)
        self.tueren = tueren

    def kosten_berechnen(self):
        if self.tueren > 2:
            return self.grundpreis + self.tueren * pricing_rules["extra_door_cost"]

    def display_info(self):
        super().display_info()
        print("Türen:", self.tueren)


class Motorrad(Fahrzeug):
    """Motorradklasse mit Kostenberechnung nach Motorgröße."""

    def __init__(self, marke, modell, baujahr, grundpreis, engine_cc):
        super().__init__(marke, modell, baujahr, grundpreis)
        self.engine_cc = engine_cc

    def kosten_berechnen(self):
        if self.engine_cc > 500:
            return self.grundpreis + self.engine_cc * pricing_rules["engine_rate"]

    def display_info(self):
        super().display_info()
        print("Motor:", self.engine_cc, "cc")


class LKW(Fahrzeug):
    """LKW-Klasse mit Ladekapazität und Kostenberechnung."""

    def __init__(self, marke, modell, baujahr, grundpreis, capacity):
        super().__init__(marke, modell, baujahr, grundpreis)
        self.capacity = capacity

    def kosten_berechnen(self):
        if self.capacity > 15:
            return self.grundpreis + self.capacity * pricing_rules["capacity_rate"]

    def display_info(self):
        super().display_info()
        print("Kapazität:", self.capacity, "Tonnen")
