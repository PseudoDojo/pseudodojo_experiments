#!/usr/bin/env python

import sys
import os
from abipy.ppcodes.oncv_parser import OncvParser
from abipy.core.atom import l2char # NlkState, RadialFunction, RadialWaveFunction,

filepath = sys.argv[1]
parser = OncvParser(filepath)
parser.scan()

if not parser.run_completed or parser.errors:
    raise RuntimeError()
print(parser)

ae, ps = parser.atan_logders.ae, parser.atan_logders.ps
data = {}

for l, ae_alog in ae.items():
    ps_alog = ps[l]
    if "energies_Ha" not in data:
        data["energies_Ha"] = list(ae_alog.energies)

    #print("l", l)
    #print("AE energies", ae_alog.energies)
    #print("AE values", ae_alog.values)
    #print("PS values", ps_alog.values)
    lchar = l2char[l]
    data[lchar] = {"ae_arctan_logder": list(ae_alog.values),
                   "ps_arctan_logder": list(ps_alog.values)}


#import pprint
#pprint.pprint(data)

import json
#s = json.dumps(data, indent=4)
#print(s)

#out_json = os.path.basename(filepath) + ".json"
#print("Writing json file to", out_json)
#with open(out_json, 'w', encoding='utf-8') as f:
#    json.dump(data, f, ensure_ascii=False) #, indent=4)


# To read the data:
#with open(out_json, 'r', encoding='utf-8') as f:
#    data = json.load(f)
energies = data["energies_Ha"]
for l in ["s", "p", "d", "f"]:
    ae_values = data[l]["ae_arctan_logder"]
    ps_values = data[l]["ps_arctan_logder"]


# To plot data with matplotlib.
#plotter = parser.get_plotter()

#plotter.plot_atan_logders()
#plotter.plot_atanlogder_econv()
