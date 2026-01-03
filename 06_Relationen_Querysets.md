# Block 06 – Übungen

## Ziele
- Projektziel: Du modellierst Beziehungen und nutzt Related Queries.

## Aufgaben
- Aufgabe A: Erstelle ein Model `Author` (Name, Email) und verknüpfe `Post` mit `Author` (ForeignKey).
- Aufgabe B: Migriere und erstelle 2 Autoren + mehrere Posts pro Autor.
- Aufgabe C: Query: alle Posts eines Autors; alle Autoren mit mindestens 1 Post.
- Aufgabe D: Erstelle ein Tagging (ManyToMany) für `Post` mit Model `Tag` (Name).

## Bonus
- Erkläre `select_related` vs. `prefetch_related` in eigenen Worten (kurz).

## Abgabe/Check
- Code läuft lokal (`python manage.py runserver`).
- Relevante Änderungen sind committet.
- Kurze Notizen zu Learnings (2–5 Stichpunkte).
