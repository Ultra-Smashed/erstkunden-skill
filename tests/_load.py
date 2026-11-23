"""Lädt ein Tool aus einem Skill-Ordner (die Ordnernamen enthalten Bindestriche)."""

import importlib.util
import io
import os
from contextlib import redirect_stdout, redirect_stderr

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS = os.path.join(ROOT, "skills")
FIX = os.path.join(ROOT, "tests", "fixtures")


def load(folder, name):
    pfad = os.path.join(SKILLS, folder, name + ".py")
    spec = importlib.util.spec_from_file_location("%s_%s" % (folder.replace("-", "_"), name), pfad)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def fix(name):
    return os.path.join(FIX, name)


def run(mod, *args):
    out, err = io.StringIO(), io.StringIO()
    code = 0
    with redirect_stdout(out), redirect_stderr(err):
        try:
            code = mod.main(list(args))
        except SystemExit as e:
            code = e.code
    return code, out.getvalue(), err.getvalue()
