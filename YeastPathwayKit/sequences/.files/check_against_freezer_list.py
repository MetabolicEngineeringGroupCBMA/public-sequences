#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""docstring."""

import re
import csv

with open("LGM - MEC_freezer_list.tsv") as f:
    txt = f.read()

matches = re.findall(r"(pYPKa_Z_[^\s]+)", txt)
result = sorted(set(matches))
tps = []
for ins in result:
    tps.append(ins.removeprefix("pYPKa_Z_"))
matches = re.findall(r"(pYPKa_E_[^\s]+)", txt)
result = sorted(set(matches))
for ins in result:
    tps.append(ins.removeprefix("pYPKa_E_"))
tps_minus80 = sorted(set(tps))

tps = []
with open("promoter_list_002.csv") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        ins, letter, pf, pr, template, comment = row
        tps.append(ins)
tps_list = sorted(set(tps))

print(set(tps_list).difference(set(tps_minus80)))
print(set(tps_minus80).difference(set(tps_list)))
print(set(tps_minus80) == set(tps_list))