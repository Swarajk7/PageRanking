#!/usr/bin/env python
import sys
for line in sys.stdin:
    line=line.strip()
    a=line
    line = line.split()
    src = line[0]
    try:
        rank,adjandtopic=line[1].split("###")
        adj,topic=adjandtopic.split('$$$')
        adj1=adj.strip().split(",")
        for node in adj1:
            if node: print "%s\t%s\t%s\t%f"%(node,"","",float(rank)/len(adj1))
        print "%s\t%s\t%s\t%f"%(src,adj,topic,0.0)
    except:
        pass
