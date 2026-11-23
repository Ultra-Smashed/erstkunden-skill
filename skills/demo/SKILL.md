---
name: demo
description: >-
  Baut eine Demo, die zeigt, wie das Produkt das Problem löst, bevor es fertig ist: Klickdummy,
  Landingpage, kurzes Ablaufvideo als Animation oder ein Vorher-Nachher mit echten Zahlen des
  Kunden. Teil des Erstkunden-Skills. Nutze den Skill bei „bau mir eine Demo“, „Prototyp zum
  Zeigen“, „Mockup für Kunden“, „Klickdummy“, „wie zeige ich das Produkt, das es noch nicht gibt“.
---

# demo

Kunden kaufen kein Konzept. Sie kaufen, wenn sie sehen, wie ihr Problem verschwindet. Die Demo muss nicht funktionieren, sie muss überzeugen und ehrlich sein.

## Bevor du anfängst

Lies `erstkunden/produkt.md` im Projekt, sonst `~/.claude/erstkunden/produkt.md`. Darin stehen Zielkunde, Problem, Idee, Ziel für den Vorverkauf und wie die Person klingt. Fehlt die Datei, frag nur nach dem, was dieser Skill braucht, und leg sie nach der Vorlage `templates/produkt.md` an. Ergebnisse anderer Skills liegen in `erstkunden/`. Lies sie, statt neu zu fragen.

## Die richtige Demo

| Was | Wann |
|---|---|
| **Klickdummy** als Webseite mit zwei bis vier Ansichten | Software, App, Dashboard |
| **Vorher-Nachher** mit den Zahlen des Kunden | Zeitersparnis, Kosten, Fehler |
| **Ablauf als Animation** (30 bis 60 Sekunden) | Prozesse, Automatisierung |
| **Landingpage** mit Problem, Lösung, Preis, Knopf „Vorab sichern“ | breite Zielgruppe |

## So baust du sie

1. Nimm das Problem aus `erstkunden/marktforschung.md` und die Worte der Kunden.
2. Zeig genau **einen** Ablauf vom Problem zum Ergebnis. Nicht alle Funktionen.
3. Nutze Beispieldaten, die echt aussehen, und markier sie als Beispiel.
4. In der Claude-App als Artifact zum Teilen, in Claude Code als HTML-Datei im Ordner `erstkunden/demo/`.
5. Am Ende der Demo steht ehrlich: „In Entwicklung. Erstkunden gestalten mit.“

## Was du abgibst

Die Demo, einen Satz, was sie zeigt, und den Satz, mit dem die Person sie im Gespräch einleitet. Danach: Weiter mit /entscheider?

## Regeln für alle Skills

- **Nichts erfinden.** Keine Zahlen, Kunden, Zitate oder Referenzen, die du nicht belegen kannst. Fehlt etwas, lass eine Lücke `[einsetzen]` und sag es.
- **Ehrlich verkaufen.** Keine falsche Verknappung, keine Versprechen, die das Produkt noch nicht halten kann. Was noch in Arbeit ist, heißt so.
- **Rechnen mit Code.**
- **Keine Rechtsberatung.** Hinweise zu Recht und Datenschutz sind eine Einordnung. Im Zweifel prüfen lassen.
