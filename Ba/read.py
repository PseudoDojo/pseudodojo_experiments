#!/usr/bin/env python

import sys
import json

# To read the data:
filepath = sys.argv[1]
with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Energy mesh in Hartree
energies = data["energies_Ha"]

for l in ("s", "p", "d", "f"):
    # AE and Pseudo logder for each l as a function of l
    ae_values = data[l]["ae_arctan_logder"]
    ps_values = data[l]["ps_arctan_logder"]
