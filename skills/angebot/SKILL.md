---
name: angebot
description: >-
  Schreibt ein Angebot für ein Produkt in Entwicklung: drei Pakete, was drin ist, was der Kunde
  davon hat, Lieferdatum, Bedingungen und der nächste Schritt, auf einer Seite. Teil des
  Erstkunden-Skills. Nutze den Skill bei „schreib das Angebot“, „Angebot nach dem Gespräch“,
  „Pakete schnüren“, „Proposal“, „was biete ich an“.
---

# angebot

Ein Angebot, das man in zwei Minuten versteht, wird unterschrieben. Eins mit zwölf Seiten wird weitergeleitet.

## Bevor du anfängst

Lies `erstkunden/produkt.md` im Projekt, sonst `~/.claude/erstkunden/produkt.md`. Darin stehen Zielkunde, Problem, Idee, Ziel für den Vorverkauf und wie die Person klingt. Fehlt die Datei, frag nur nach dem, was dieser Skill braucht, und leg sie nach der Vorlage `templates/produkt.md` an. Ergebnisse anderer Skills liegen in `erstkunden/`. Lies sie, statt neu zu fragen.

## Aufbau, eine Seite

1. **Ihr Ziel** in den Worten des Kunden aus dem Gespräch.
2. **Drei Pakete** mit Preisen aus /preise. Das mittlere ist das empfohlene und so markiert.
3. **Was Sie davon haben**, pro Paket in Ergebnissen, nicht in Funktionen.
4. **Stand und Lieferung:** was fertig ist, was nicht, Lieferdatum.
5. **Bedingungen:** Zahlungsweise, Laufzeit, Kündigung, Geld-zurück-Zusage beim Vorverkauf.
6. **Nächster Schritt** mit Datum und einem einzigen Knopf oder Satz zum Zusagen.

Die Preise und Summen mit Code rechnen. Netto und Brutto klar trennen.

## Was du abgibst

Das Angebot als Dokument zum Herunterladen und die kurze Mail dazu in der Stimme der Person. Danach den Kontakt in `erstkunden/vorverkauf.csv` auf `demo` oder `zusage` setzen.

## Regeln für alle Skills

- **Nichts erfinden.** Keine Zahlen, Kunden, Zitate oder Referenzen, die du nicht belegen kannst. Fehlt etwas, lass eine Lücke `[einsetzen]` und sag es.
- **Ehrlich verkaufen.** Keine falsche Verknappung, keine Versprechen, die das Produkt noch nicht halten kann. Was noch in Arbeit ist, heißt so.
- **Rechnen mit Code.**
- **Keine Rechtsberatung.** Hinweise zu Recht und Datenschutz sind eine Einordnung. Im Zweifel prüfen lassen.
