#!/usr/bin/env python3
"""Zählt deinen Vorverkauf und sagt: bauen, weitermachen oder umdenken. Nur Standardbibliothek.

Liste als CSV mit Kopfzeile (Komma oder Semikolon):

  kontakt,firma,status,betrag,datum,notiz
  Anna Berg,Kanzlei Berg,bezahlt,1400,2026-11-20,
  Tom Ries,Ries GmbH,zusage,1400,2026-11-21,zahlt nach Rechnung

Status: angesprochen, gespraech, demo, zusage, bezahlt, abgesagt

  python3 validierung.py vorverkauf.csv --ziel-kunden 3 --ziel-umsatz 4000
  python3 validierung.py vorverkauf.csv --json

Nur „bezahlt“ zählt als Beweis. Eine Zusage ohne Zahlung ist ein gutes Zeichen, kein Beleg.
"""

import argparse
import csv
import io
import json
import sys

STUFEN = ["angesprochen", "gespraech", "demo", "zusage", "bezahlt"]
ALIAS = {"gespräch": "gespraech", "call": "gespraech", "bezahlt ": "bezahlt", "gezahlt": "bezahlt",
         "zugesagt": "zusage", "abgelehnt": "abgesagt", "nein": "abgesagt"}


def lesen(text):
    probe = text.split("\n", 1)[0]
    trenner = ";" if probe.count(";") > probe.count(",") else ","
    zeilen = []
    for z in csv.DictReader(io.StringIO(text), delimiter=trenner):
        z = {k.strip().lower(): (v or "").strip() for k, v in z.items() if k}
        status = ALIAS.get(z.get("status", "").lower(), z.get("status", "").lower())
        betrag = z.get("betrag", "").replace("€", "").replace(" ", "").strip()
        if "," in betrag:  # deutsches Format: 1.400,50
            betrag = betrag.replace(".", "").replace(",", ".")
        try:
            betrag = float(betrag) if betrag else 0.0
        except ValueError:
            betrag = 0.0
        zeilen.append({"kontakt": z.get("kontakt", ""), "firma": z.get("firma", ""), "status": status, "betrag": betrag})
    return zeilen


def auswerten(zeilen, ziel_kunden=3, ziel_umsatz=0.0):
    zaehler = {s: 0 for s in STUFEN + ["abgesagt"]}
    unbekannt = []
    for z in zeilen:
        if z["status"] in zaehler:
            zaehler[z["status"]] += 1
        else:
            unbekannt.append(z["status"])
    # Wer weiter ist, war auch auf den Stufen davor
    erreicht = {}
    for i, s in enumerate(STUFEN):
        erreicht[s] = sum(zaehler[t] for t in STUFEN[i:])
    bezahlt = [z for z in zeilen if z["status"] == "bezahlt"]
    umsatz = sum(z["betrag"] for z in bezahlt)
    zusagen = zaehler["zusage"]
    gespraeche = erreicht["gespraech"] + zaehler["abgesagt"]
    quote = round(len(bezahlt) / gespraeche, 2) if gespraeche else 0.0

    ziel_erreicht = len(bezahlt) >= ziel_kunden and umsatz >= ziel_umsatz
    if ziel_erreicht:
        urteil = "bauen"
        grund = "Genug Kunden haben bezahlt. Bau genau das, was sie in /anforderungen gesagt haben, nicht mehr."
    elif gespraeche >= 20 and quote < 0.05:
        urteil = "umdenken"
        grund = "Viele Gespräche, kaum Zahlungen. Problem, Zielgruppe oder Preis passen nicht. Zurück zu /marktforschung."
    else:
        urteil = "weitermachen"
        fehlen = max(0, ziel_kunden - len(bezahlt))
        grund = f"Es fehlen noch {fehlen} zahlende Kunden" + (f" und {max(0, ziel_umsatz - umsatz):.0f} € Umsatz" if ziel_umsatz else "") + "."
        if zusagen:
            grund += f" {zusagen} Zusagen ohne Zahlung: jetzt mit /nachfassen um die Zahlung bitten."
    return {"stufen": erreicht, "abgesagt": zaehler["abgesagt"], "bezahlt": len(bezahlt), "umsatz": round(umsatz, 2),
            "quote_gespraech_zu_zahlung": quote, "urteil": urteil, "grund": grund, "unbekannter_status": sorted(set(unbekannt))}


def main(argv=None):
    p = argparse.ArgumentParser(description="Vorverkauf auswerten")
    p.add_argument("datei")
    p.add_argument("--ziel-kunden", type=int, default=3)
    p.add_argument("--ziel-umsatz", type=float, default=0.0)
    p.add_argument("--json", action="store_true")
    a = p.parse_args(argv)
    with open(a.datei, encoding="utf-8-sig") as fh:
        e = auswerten(lesen(fh.read()), a.ziel_kunden, a.ziel_umsatz)
    if a.json:
        print(json.dumps(e, ensure_ascii=False, indent=2))
        return 0
    s = e["stufen"]
    print(f"Angesprochen {s['angesprochen']} → Gespräch {s['gespraech']} → Demo {s['demo']} → Zusage {s['zusage']} → bezahlt {s['bezahlt']}"
          + (f" (abgesagt {e['abgesagt']})" if e["abgesagt"] else ""))
    print(f"Umsatz aus dem Vorverkauf: {e['umsatz']:.0f} €")
    print(f"Urteil: {e['urteil'].upper()}. {e['grund']}")
    if e["unbekannter_status"]:
        print("Unbekannter Status, nicht gezählt: " + ", ".join(e["unbekannter_status"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
