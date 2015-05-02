#!/usr/bin/env python
from __future__ import print_function
import sys
current_key=None
for line in sys.stdin:
    splitted=line.strip().split('\t')
    if len(splitted) ==2: source,dest = splitted
    else: source,dest = splitted[0],''
    if source != current_key:
        if current_key: print ('')
        print("%s 1.0#%s"%(source,dest),end="")
        current_key=source
    else:
        print (",%s"%(dest),end="")
