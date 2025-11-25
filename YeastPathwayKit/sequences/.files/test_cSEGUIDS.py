#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pydna.readers import read
from pathlib import Path

new = list(Path(".").glob("*.gb"))
old = list(Path("old").glob("*.gb"))

newset = set(n.name for n in new)
oldset = set(n.name for n in old)

for n in new:
    ns = read(n)
    op = Path("old")/Path(n)
    if op.exists():
        os = read(op)
        print(n.name, ns.cseguid()==os.cseguid())
    else:
        print(n.name, "<<<<<<<<<<<<<<<<<<<<<<")