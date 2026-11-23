---
name: preise
description: >-
  Findet den Preis aus dem Wert für den Kunden statt aus dem Bauchgefühl: Problemkosten, ein fairer
  Anteil davon, Untergrenze aus den eigenen Kosten, drei Pakete und ein Vorverkaufspreis, gerechnet
  mit preise.py. Teil des Erstkunden-Skills. Nutze den Skill bei „was soll ich verlangen“,
  „Preis festlegen“, „Pakete“, „zu billig“, „Preismodell“, „pricing“.
---

# preise

Neue Gründer sind fast immer zu billig. Der Preis kommt aus dem, was das Problem den Kunden kostet, nicht aus dem, was die Arbeit dich kostet. Die eigenen Kosten sind nur die Untergrenze.

```bash
python3 preise.py --problemkosten 24000 --anteil 0.15 --kosten 3000 --stunden 40 --stundensatz 90
```

## Bevor du anfängst

Lies `erstkunden/produkt.md` im Projekt, sonst `~/.claude/erstkunden/produkt.md`. Darin stehen Zielkunde, Problem, Idee, Ziel für den Vorverkauf und wie die Person klingt. Fehlt die Datei, frag nur nach dem, was dieser Skill braucht, und leg sie nach der Vorlage `templates/produkt.md` an. Ergebnisse anderer Skills liegen in `erstkunden/`. Lies sie, statt neu zu fragen.

## So gehst du vor

1. **Problemkosten pro Kunde und Jahr** aus /marktforschung, mit Rechenweg. Fehlen sie, gemeinsam rechnen: Stunden pro Woche × Stundensatz × Wochen, plus Fehlerkosten.
2. **Anteil:** Wie viel davon zahlt ein Kunde für die Lösung? Standard 15 %, bei hohem Risiko oder großem Wechselaufwand weniger.
3. **Untergrenze:** feste Kosten pro Kunde plus deine Stunden mal Mindest-Stundensatz.
4. `preise.py` rechnen lassen. Warnungen nie verschweigen.
5. **Prüfen:** Was zahlen Kunden heute für die nächstbeste Lösung? Liegt der Preis weit darüber, braucht es einen sehr klaren Grund.

## Was du abgibst

Drei Pakete mit Jahres- und Monatspreis, den Vorverkaufspreis, den Satz, mit dem die Person den Preis im Gespräch begründet („Das Problem kostet Sie rund … im Jahr, die Lösung …“), und alle Warnungen des Tools.

## Regeln für alle Skills

- **Nichts erfinden.** Keine Zahlen, Kunden, Zitate oder Referenzen, die du nicht belegen kannst. Fehlt etwas, lass eine Lücke `[einsetzen]` und sag es.
- **Ehrlich verkaufen.** Keine falsche Verknappung, keine Versprechen, die das Produkt noch nicht halten kann. Was noch in Arbeit ist, heißt so.
- **Rechnen mit Code.**
- **Keine Rechtsberatung.** Hinweise zu Recht und Datenschutz sind eine Einordnung. Im Zweifel prüfen lassen.
