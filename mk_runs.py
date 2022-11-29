#! /usr/bin/env python
#
#   script generator for project="2018-S1-MU-45"
#
#

import os
import sys

# in prep of the new lmtoy module
try:
    lmtoy = os.environ['LMTOY']
    sys.path.append(lmtoy + '/lmtoy')
    import runs
except:
    print("No LMTOY with runs.py")
    sys.exit(0)

project="2018-S1-MU-45"

#        obsnums per source (make it negative if not added to the final combination)
on = {}

on['L1157-B1'] = [              
                  84475,-84683, 84744, 84748, 84752, 84756, 84760,           # 30-may-2019
                  85984, 85988, 85992, 86082, 86086, 86231, 86235,           # through 8-nov-2019 
                 ]

#        common parameters per source on the first dryrun (run1, run2)
pars1 = {}
pars1['L1157-B1'] = "dv=250 dw=250 extent=150"

#        common parameters per source on subsequent runs (run1a, run2a)
pars2 = {}
pars2['L1157-B1'] = "pix_list=0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15"

runs.mk_runs(project, on, pars1, pars2)

