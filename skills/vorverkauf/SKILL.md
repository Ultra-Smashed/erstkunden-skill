---
name: vorverkauf
description: >-
  Bringt Kunden dazu, vor dem Start zu bezahlen, und nutzt ihre Anforderungen, um genau das passende
  Produkt zu bauen: Erstkunden-Angebot mit Rabatt und Mitsprache, ehrliche Bedingungen mit
  Lieferdatum und Geld-zurück-Zusage, Zahlungslink, Auswertung mit validierung.py. Teil des
  Erstkunden-Skills. Nutze den Skill bei „Vorverkauf“, „Presale“, „Kunden vorab zahlen lassen“,
  „Nachfrage testen“, „Founding Customer“, „bauen oder nicht“, „validieren“.
---

# vorverkauf

Eine Zusage kostet nichts. Eine Zahlung beweist Nachfrage. Darum endet jedes gute Gespräch im Vorverkauf mit der Bitte um Geld, ehrlich und mit klaren Bedingungen.

```bash
python3 validierung.py erstkunden/vorverkauf.csv --ziel-kunden 3 --ziel-umsatz 4000
```

## Bevor du anfängst

Lies `erstkunden/produkt.md` im Projekt, sonst `~/.claude/erstkunden/produkt.md`. Darin stehen Zielkunde, Problem, Idee, Ziel für den Vorverkauf und wie die Person klingt. Fehlt die Datei, frag nur nach dem, was dieser Skill braucht, und leg sie nach der Vorlage `templates/produkt.md` an. Ergebnisse anderer Skills liegen in `erstkunden/`. Lies sie, statt neu zu fragen.

## Das Erstkunden-Angebot

- **Preis:** aus /preise, mit Vorverkaufs-Rabatt (Standard 30 %), für eine begrenzte Zahl Erstkunden. Die Begrenzung muss stimmen.
- **Mitsprache:** Erstkunden bestimmen mit, was zuerst gebaut wird. Daraus kommen die Anforderungen.
- **Lieferdatum:** ein ehrliches Datum, mit Puffer.
- **Geld zurück:** Wird nicht geliefert oder nicht gebaut, gibt es den vollen Betrag zurück. Das senkt das Risiko für den Kunden und gehört dazu.
- **Bei Verbrauchern:** Widerrufsrecht und Angaben zum Liefertermin beachten.

## So läuft es

1. Angebot als kurzes Dokument (eine Seite) schreiben, in der Stimme der Person.
2. Zahlungsweg vorschlagen, den die Person schon hat (Rechnung, Zahlungslink ihres Zahlungsanbieters). Claude legt nichts an und zieht kein Geld ein.
3. Jeden Kontakt in `erstkunden/vorverkauf.csv` führen: kontakt, firma, status, betrag, datum, notiz. Status: angesprochen, gespraech, demo, zusage, bezahlt, abgesagt.
4. Wöchentlich `validierung.py` laufen lassen und das Urteil ehrlich sagen: **bauen**, **weitermachen** oder **umdenken**.
5. Bei „bauen“: sofort /anforderungen mit den zahlenden Kunden.

## Was du abgibst

Das Angebot, die Mail mit der Bitte um Zahlung und das aktuelle Urteil mit Zahlen. Nur „bezahlt“ zählt als Beweis.

## Regeln für alle Skills

- **Nichts erfinden.** Keine Zahlen, Kunden, Zitate oder Referenzen, die du nicht belegen kannst. Fehlt etwas, lass eine Lücke `[einsetzen]` und sag es.
- **Ehrlich verkaufen.** Keine falsche Verknappung, keine Versprechen, die das Produkt noch nicht halten kann. Was noch in Arbeit ist, heißt so.
- **Rechnen mit Code.**
- **Keine Rechtsberatung.** Hinweise zu Recht und Datenschutz sind eine Einordnung. Im Zweifel prüfen lassen.
