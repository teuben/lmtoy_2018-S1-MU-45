#! /usr/bin/env python
#
#   script generator for project="2018-S1-MU-45"
#
#

import os
import sys

from lmtoy import runs

project="2018-S1-MU-45"

#        obsnums per source (make it negative if not added to the final combination)
on = {}

#   84752 looks bad
on['L1157-B1'] = [              
                  84475, 84683, 84744, 84748,-84752, 84756, 84760,           # 30-may-2019
                  85984, 85988, 85992, 86082, 86086, 86231, 86235,           # through 8-nov-2019 
                 ]

#        common parameters per source on the first dryrun (run1, run2)
pars1 = {}
pars1['L1157-B1'] = "dv=450 dw=750 extent=180"

#        common parameters per source on subsequent runs (run1a, run2a)
pars2 = {}
pars2['L1157-B1'] = "pix_list=0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15"

runs.mk_runs(project, on, pars1, pars2)

