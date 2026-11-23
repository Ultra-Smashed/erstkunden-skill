# erstkunden-skill

Elf Claude-Skills, die dir zahlende Kunden bringen, bevor dein Produkt fertig ist. Auf Deutsch, kostenlos, MIT-Lizenz, ohne Anmeldung, ohne API-Schlüssel.

Die meisten Gründer bauen monatelang und suchen dann Kunden. Dieser Skill dreht das um: Problem finden, für das Firmen schon zahlen, Demo zeigen, Entscheider ansprechen, Vorverkauf. Gebaut wird erst, wenn Kunden bezahlt haben, und dann genau das, was sie brauchen.

## Installation

Füg das in Claude ein:

```
https://github.com/Ultra-Smashed/erstkunden-skill

Installiere den Skill.
```

Die Code-Ausführung muss an sein (Settings → Capabilities), für die Marktforschung auch die Websuche.

Oder als Plugin in Claude Code:

```
/plugin marketplace add Ultra-Smashed/erstkunden-skill
/plugin install erstkunden-skill@erstkunden-skill
```

Als Plugin heißen die Skills dann `/erstkunden-skill:vorverkauf` und so weiter. Für die kurzen Namen die Ordner kopieren:

```bash
git clone https://github.com/Ultra-Smashed/erstkunden-skill.git
cp -r erstkunden-skill/skills/* ~/.claude/skills/
```

## Zuerst: dein Vorhaben

Leg [`templates/produkt.md`](templates/produkt.md) als `erstkunden/produkt.md` in dein Projekt oder als `~/.claude/erstkunden/produkt.md` und füll aus, was du schon weißt. Oder sag Claude: „Interview mich zu meinem Vorhaben und schreib meine produkt.md.“ Jeder Skill liest sie.

## Die elf Skills

| Befehl | Was er tut |
| --- | --- |
| `/marktforschung` | Findet Probleme, für deren Lösung Firmen schon heute Tausende zahlen, mit Problemkosten pro Jahr und Quellen. |
| `/demo` | Baut eine Demo, die zeigt, wie dein Produkt das Problem löst: Klickdummy, Vorher-Nachher, Ablauf oder Landingpage. |
| `/entscheider` | Findet die Menschen mit dem Budget und schreibt die erste Nachricht. Verschickt nichts. |
| `/pitch` | Gesprächsleitfaden, kurze Präsentation und Kurzfassung für ein Produkt in Entwicklung. |
| `/vorverkauf` | Das Erstkunden-Angebot mit ehrlichen Bedingungen und die Auswertung mit `validierung.py`: bauen, weitermachen oder umdenken. |
| `/anforderungen` | Macht aus Gesprächen mit zahlenden Kunden den kleinsten sinnvollen Umfang. |
| `/angebot` | Ein Angebot auf einer Seite mit drei Paketen. |
| `/preise` | Preis aus dem Wert für den Kunden, Untergrenze aus deinen Kosten, gerechnet mit `preise.py`. |
| `/nachfassen` | Drei Nachrichten mit Abstand, jede mit neuem Grund, auch für Zusagen ohne Zahlung. |
| `/einwaende` | Antworten auf „zu teuer“ und „gibt es noch nicht“, dazu ein Rollenspiel mit Feedback. |
| `/launch-plan` | Vom Vorverkauf zur Lieferung, mit Updates an die Erstkunden. |

## So arbeitest du damit

```
/marktforschung  ->  /preise  ->  /demo  ->  /entscheider  ->  /pitch  ->  /vorverkauf
                                              /nachfassen, /einwaende, /angebot   (laufend)
/vorverkauf sagt „bauen“  ->  /anforderungen  ->  /launch-plan
```

## Die Tools

Reines Python aus der Standardbibliothek, ab Python 3.8.

```bash
python3 skills/preise/preise.py --problemkosten 24000 --anteil 0.15 --kosten 3000 --stunden 40 --stundensatz 90
python3 skills/vorverkauf/validierung.py erstkunden/vorverkauf.csv --ziel-kunden 3 --ziel-umsatz 4000
```

`validierung.py` liest eine Liste deiner Kontakte mit Status (angesprochen, gespraech, demo, zusage, bezahlt, abgesagt) und sagt dir, ob du bauen kannst. Nur „bezahlt“ zählt als Beweis.

## Kleingedrucktes

**Nichts wird verschickt und nichts wird kassiert.** Die Skills schreiben Nachrichten, Angebote und Pläne. Du verschickst, du stellst Rechnungen.

**Ehrlich verkaufen.** Vorverkauf heißt: klar sagen, dass das Produkt in Entwicklung ist, ein ehrliches Lieferdatum und Geld zurück, wenn nicht geliefert wird. Keine falsche Verknappung.

**Kaltakquise.** In Deutschland ist Werbung per E-Mail ohne Einwilligung auch an Firmen unzulässig. `/entscheider` schlägt deshalb andere Wege für den ersten Kontakt vor.

**Keine Rechts- oder Steuerberatung.** Hinweise zu Widerrufsrecht, Datenschutz und Wettbewerbsrecht sind eine Einordnung.

## Tests

```bash
cd tests && python3 -m unittest -v
```
