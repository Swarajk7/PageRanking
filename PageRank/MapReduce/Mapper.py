#!/usr/bin/env python
import sys
for line in sys.stdin:
    line=line.strip()
    line = line.split()
    src = line[0]
    rank,adj=line[1].split("#")
    adj1=adj.strip().split(",")
    for node in adj1:
        print "%s\t%s\t%f"%(node,"",float(rank)/len(adj1))
    print "%s\t%s\t%f"%(src,adj,0.0)
