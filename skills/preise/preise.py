#!/usr/bin/env python3
"""Preise aus dem Wert für den Kunden, mit Untergrenze aus deinen Kosten. Nur Standardbibliothek.

  python3 preise.py --problemkosten 24000 --anteil 0.2 --kosten 3000 --stunden 40 --stundensatz 90
  python3 preise.py --problemkosten 24000 --vorverkauf-rabatt 0.3 --json

--problemkosten   was das Problem den Kunden pro Jahr kostet (Euro), aus der Marktforschung
--anteil          welchen Teil davon der Kunde für die Lösung zahlen würde (Standard 0,15 = 15 %)
--kosten          deine festen Kosten pro Kunde und Jahr (Software, Lizenzen, Material)
--stunden         deine Arbeitsstunden pro Kunde und Jahr
--stundensatz     dein Mindest-Stundensatz
--vorverkauf-rabatt  Rabatt für Erstkunden, die vor dem Start zahlen (Standard 0,3)

Ergebnis: drei Pakete (Basis, Empfohlen, Premium), der Vorverkaufspreis und eine Warnung,
wenn der Preis aus dem Wert unter deinen Kosten liegt.
"""

import argparse
import json
import sys


def runden(betrag):
    """Auf einen glatten Preis runden: unter 100 auf 9, unter 1000 auf 10, sonst auf 50 (−1 für ...9)."""
    if betrag < 100:
        return max(9, int(round(betrag / 10.0)) * 10 - 1)
    if betrag < 1000:
        return int(round(betrag / 10.0)) * 10
    return int(round(betrag / 50.0)) * 50


def rechnen(problemkosten, anteil=0.15, kosten=0.0, stunden=0.0, stundensatz=0.0, vorverkauf_rabatt=0.3):
    if problemkosten <= 0:
        raise ValueError("Problemkosten müssen größer als 0 sein")
    if not 0 < anteil < 1:
        raise ValueError("Anteil muss zwischen 0 und 1 liegen")
    if not 0 <= vorverkauf_rabatt < 1:
        raise ValueError("Vorverkaufs-Rabatt muss zwischen 0 und 1 liegen")
    untergrenze = kosten + stunden * stundensatz
    wert = problemkosten * anteil
    empfohlen = max(wert, untergrenze * 1.3 if untergrenze else 0)
    pakete = {
        "Basis": runden(empfohlen * 0.6),
        "Empfohlen": runden(empfohlen),
        "Premium": runden(empfohlen * 1.8),
    }
    ergebnis = {
        "wert_pro_jahr": round(wert),
        "untergrenze_pro_jahr": round(untergrenze),
        "pakete_pro_jahr": pakete,
        "pakete_pro_monat": {k: runden(v / 12.0) for k, v in pakete.items()},
        "vorverkauf_pro_jahr": runden(pakete["Empfohlen"] * (1 - vorverkauf_rabatt)),
        "rendite_fuer_kunden": round(problemkosten / pakete["Empfohlen"], 1),
        "warnungen": [],
    }
    if untergrenze and wert < untergrenze:
        ergebnis["warnungen"].append(
            "Der Preis aus dem Wert liegt unter deinen Kosten. Entweder ist das Problem zu klein für diese Lösung, "
            "oder die Lösung zu teuer gebaut. Erst klären, dann verkaufen.")
    if untergrenze and ergebnis["vorverkauf_pro_jahr"] < untergrenze:
        ergebnis["warnungen"].append(
            "Der Vorverkaufspreis deckt deine Kosten nicht. Rabatt kleiner machen oder auf wenige Erstkunden begrenzen.")
    if ergebnis["rendite_fuer_kunden"] < 3:
        ergebnis["warnungen"].append(
            "Der Kunde bekommt weniger als das Dreifache seines Preises zurück. Für einen schnellen Kauf ist das knapp.")
    return ergebnis


def main(argv=None):
    p = argparse.ArgumentParser(description="Preise aus dem Wert für den Kunden")
    p.add_argument("--problemkosten", type=float, required=True)
    p.add_argument("--anteil", type=float, default=0.15)
    p.add_argument("--kosten", type=float, default=0.0)
    p.add_argument("--stunden", type=float, default=0.0)
    p.add_argument("--stundensatz", type=float, default=0.0)
    p.add_argument("--vorverkauf-rabatt", type=float, default=0.3)
    p.add_argument("--json", action="store_true")
    a = p.parse_args(argv)
    try:
        e = rechnen(a.problemkosten, a.anteil, a.kosten, a.stunden, a.stundensatz, a.vorverkauf_rabatt)
    except ValueError as fehler:
        print(fehler, file=sys.stderr)
        return 2
    if a.json:
        print(json.dumps(e, ensure_ascii=False, indent=2))
        return 0
    print(f"Wert für den Kunden: {e['wert_pro_jahr']} € pro Jahr ({int(a.anteil * 100)} % von {int(a.problemkosten)} € Problemkosten)")
    if e["untergrenze_pro_jahr"]:
        print(f"Deine Untergrenze: {e['untergrenze_pro_jahr']} € pro Jahr")
    for name, preis in e["pakete_pro_jahr"].items():
        print(f"- {name}: {preis} € pro Jahr (rund {e['pakete_pro_monat'][name]} € im Monat)")
    print(f"Vorverkauf für Erstkunden: {e['vorverkauf_pro_jahr']} € im ersten Jahr")
    print(f"Der Kunde bekommt das {e['rendite_fuer_kunden']}-Fache seines Preises zurück.")
    for w in e["warnungen"]:
        print("Achtung: " + w)
    return 0


if __name__ == "__main__":
    sys.exit(main())
