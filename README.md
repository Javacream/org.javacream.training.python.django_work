# Django-Seminar – Agenda (12 Blöcke)

Ziel des Seminars ist es, eine vollständige Django-Webanwendung zu entwickeln und dabei die wichtigsten Konzepte, Best Practices und typischen Workflows kennenzulernen.

## Block 1 – Einführung & Überblick
- Was ist Django?
- Philosophie: „batteries included“
- Typische Einsatzgebiete
- Architektur: MTV (Model–Template–View)
- Überblick über den Seminarablauf und das Beispielprojekt

## Block 2 – Entwicklungsumgebung & Projektstart
- Virtuelle Umgebungen (venv)
- Installation von Django
- Projekt vs. App
- `django-admin` und `manage.py`
- Start des Entwicklungsservers

## Block 3 – URL Routing & Views
- URL-Dispatcher
- Funktionsbasierte Views
- Klassenbasierte Views (Überblick)
- Request- und Response-Objekte
- GET- und POST-Requests

## Block 4 – Templates & statische Dateien
- Django Template Language (DTL)
- Template-Vererbung
- Kontextdaten
- Template-Tags und Filter
- Einbindung von CSS und statischen Assets


## Block 5 – Models & ORM Grundlagen
- Models definieren
- Felder und Datentypen
- Migrationen verstehen
- Einführung in das Django ORM
- Erste Datenbankabfragen

## Block 6 – Beziehungen & Datenmodellierung
- One-to-Many-Beziehungen
- Many-to-Many-Beziehungen
- Foreign Keys
- QuerySets und Filter
- Performance-Grundlagen (Überblick)

## Block 7 – Django Admin
- Aktivieren des Admin-Bereichs
- Models registrieren
- Listen- und Formularansichten anpassen
- Such- und Filterfunktionen
- Admin als produktives Werkzeug

## Block 8 – Forms & User Input
- Django Forms
- ModelForms
- Validierung von Eingaben
- CSRF-Schutz
- Verarbeitung von POST-Daten

## Block 9 – Authentifizierung & Benutzer
- Django Auth-System
- Login und Logout
- Permissions und Groups
- Zugriffsbeschränkungen für Views
- Überblick: Custom User Model

## Block 10 – APIs & JSON
- JSON-Responses mit Django
- Aufbau einfacher API-Endpunkte
- Serialisierung von Daten
- Fehlerbehandlung (404, 400)
- Ausblick: Django REST Framework

## Block 11 – Testing, Debugging & Best Practices
- Tests für Models und Views
- Django Test Client
- Debugging-Strategien
- Logging-Grundlagen
- Typische Anfängerfehler vermeiden

## Block 12 – Deployment & Ausblick
- Development vs. Production
- WSGI / ASGI Überblick
- Umgang mit Settings in Produktion
- Security-Grundlagen
- Nächste Schritte (APIs, Async, Skalierung)

## Start
```bash
python -m venv venv
source venv/bin/activate
pip install django
python manage.py migrate
python manage.py runserver
```
