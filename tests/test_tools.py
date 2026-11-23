import json
import os
import tempfile
import unittest

from _load import load, fix, run

pr = load("preise", "preise")
va = load("vorverkauf", "validierung")


class Preise(unittest.TestCase):
    def test_pakete_steigen(self):
        e = pr.rechnen(24000, 0.15)
        p = e["pakete_pro_jahr"]
        self.assertLess(p["Basis"], p["Empfohlen"])
        self.assertLess(p["Empfohlen"], p["Premium"])
        self.assertEqual(e["wert_pro_jahr"], 3600)
        self.assertLess(e["vorverkauf_pro_jahr"], p["Empfohlen"])

    def test_warnung_unter_kosten(self):
        e = pr.rechnen(5000, 0.1, kosten=1000, stunden=20, stundensatz=80)
        self.assertTrue(any("unter deinen Kosten" in w for w in e["warnungen"]))
        self.assertGreaterEqual(e["pakete_pro_jahr"]["Empfohlen"], 2600 * 1.3 - 50)

    def test_runden(self):
        self.assertEqual(pr.runden(3612), 3600)
        self.assertEqual(pr.runden(412), 410)
        self.assertEqual(pr.runden(47), 49)

    def test_falsche_eingabe(self):
        code, _, err = run(pr, "--problemkosten", "0")
        self.assertEqual(code, 2)


class Validierung(unittest.TestCase):
    def test_stufen_und_urteil(self):
        code, out, _ = run(va, fix("vorverkauf.csv"), "--ziel-kunden", "3", "--json")
        e = json.loads(out)
        self.assertEqual(e["bezahlt"], 1)
        self.assertEqual(e["umsatz"], 1400.0)
        self.assertEqual(e["stufen"]["angesprochen"], 5)
        self.assertEqual(e["stufen"]["gespraech"], 4)
        self.assertEqual(e["urteil"], "weitermachen")
        self.assertIn("Zusagen ohne Zahlung", e["grund"])

    def test_bauen(self):
        code, out, _ = run(va, fix("vorverkauf.csv"), "--ziel-kunden", "1", "--json")
        self.assertEqual(json.loads(out)["urteil"], "bauen")

    def test_umdenken(self):
        zeilen = "kontakt,firma,status,betrag\n" + "".join(f"K{i},F{i},abgesagt,\n" for i in range(25))
        with tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False, encoding="utf-8") as fh:
            fh.write(zeilen)
        try:
            code, out, _ = run(va, fh.name, "--json")
            self.assertEqual(json.loads(out)["urteil"], "umdenken")
        finally:
            os.unlink(fh.name)


if __name__ == "__main__":
    unittest.main()
