#  Fahrzeugverwaltungssystem

##  Projektübersicht

Das **Fahrzeugverwaltungssystem** ist eine konsolenbasierte Python-Anwendung, die ermöglicht verschiedene features wie Hinzufügen, Speichen, Anzeigen, Sortieren, Suchen und Löschen verschiedener Fahrzeugtypen wie Autos, Motorräder und LKWs. Jeder Fahrzeugtyp besitzt eigene Eigenschaften und eine individuelle Kostenberechnung.

Das Projekt simuliert grundlegende Funktionen eines Fahrzeug- oder Flottenverwaltungssystems.

##  Funktionen

### Fahrzeugverwaltung

* Fahrzeuge mit eindeutiger ID hinzufügen
* Mehrere Fahrzeugtypen unterstützen:

  * Auto (Anzahl Türen)
  * Motorrad (Hubraum)
  * LKW (Ladekapazität)

### Kostenberechnung

* Dynamische Berechnung über konfigurierbare Regeln

### Suche

* Suche nach Fahrzeug-ID
* Suche nach Marke/Modell

### Sortierung

* Sortieren nach Marke oder Modell

### Anzeige

* Übersicht aller Fahrzeuge mit Details
* Anzeige berechneter Kosten

### Löschen

* Fahrzeug nach ID entfernen
* Meldung bei nicht vorhandenem Fahrzeug

### Statistik

* Fahrzeuganzahl nach Typ (Dictionary-Auswertung)

### Fehlerbehandlung

* Sichere Benutzereingabe mit try/except

---

##  Demonstrierte Konzepte

* Klassen & Vererbung
* Polymorphie
* Konstruktoren (**init**)
* Listen und Dictionaries
* Kapselung
* Modularer Programmaufbau
* Ausnahmebehandlung
* Menübasierte Benutzerführung

---

##  Projektstruktur

```
fahrzeug.py   → Fahrzeugklassen & Preisregeln
manager.py    → Verwaltung & Operationen
utils.py      → Eingabeprüfung
main.py       → Hauptprogramm & Menü
README.md     → Dokumentation
```

---

## ▶ Programm starten

Python 3 installieren und ausführen:

```
python main.py
```

Dann den Menüanweisungen folgen.

---

##  Erweiterungsmöglichkeiten

* JSON Speicherung/Laden
* Datenbankintegration
* Erweiterte Preislogik
* Berichtssystem

---

##  Autor

Jay Oza
## Software version
Version 1.0

---

