#!/usr/bin/env python
import sys
BETA=0.85
NodeSize = 2354 #find a way to do this dynamically
def get(val):
    return BETA*val + (1-BETA)/NodeSize
last_key=None
total_rank = 0.0
overall_adj=''
for line in sys.stdin:
    src,adj,rank = line.strip().split("\t")
    if last_key == src:
        if adj=='': total_rank += float(rank)
        else: overall_adj=adj
    else:
        if last_key: print "%s %f#%s"%(last_key,get(total_rank),overall_adj)
        last_key=src
        if adj=='': 
            total_rank=float(rank)
            overall_adj = ''
        else: 
            total_rank = 0.0
            overall_adj = adj     
if last_key: print "%s %f#%s"%(last_key,get(total_rank),overall_adj)    
