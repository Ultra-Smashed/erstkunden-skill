import json
import os
import re
import unittest

from _load import ROOT, SKILLS as SKILLS_DIR

SKILLS = ["marktforschung", "demo", "entscheider", "pitch", "vorverkauf", "anforderungen", "angebot", "preise",
          "nachfassen", "einwaende", "launch-plan"]


def read(*parts):
    with open(os.path.join(*parts), encoding="utf-8") as fh:
        return fh.read()


class Repo(unittest.TestCase):
    def test_elf_skills(self):
        gefunden = sorted(d for d in os.listdir(SKILLS_DIR) if os.path.isfile(os.path.join(SKILLS_DIR, d, "SKILL.md")))
        self.assertEqual(gefunden, sorted(SKILLS))

    def test_frontmatter(self):
        for s in SKILLS:
            text = read(SKILLS_DIR, s, "SKILL.md")
            m = re.match(r"^---\nname: (.+)\ndescription: >-\n((?:  .+\n)+)---\n", text)
            self.assertTrue(m, s)
            self.assertEqual(m.group(1), s)
            self.assertLess(len(" ".join(m.group(2).split())), 1024, s)
            self.assertIn("Nichts erfinden", text, s)

    def test_plugin_json(self):
        p = json.loads(read(ROOT, ".claude-plugin", "plugin.json"))
        mp = json.loads(read(ROOT, ".claude-plugin", "marketplace.json"))
        self.assertEqual(p["name"], mp["plugins"][0]["name"])
        self.assertIn("Ultra-Smashed/erstkunden-skill", p["repository"])


if __name__ == "__main__":
    unittest.main()
