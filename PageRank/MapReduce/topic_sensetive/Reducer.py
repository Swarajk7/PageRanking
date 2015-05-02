#!/usr/bin/env python
import sys
BETA=0.85
TOPIC = 'nitrkl'
LEN = 1473
def get(val,flag):
    global BETA,LEN
    return BETA*val + (flag*(1-BETA))/LEN
def printReducer(last_key,total_rank,overall_adj,top):
    flag = 0
    global TOPIC
    if TOPIC == top : flag=1
    print "%s %f###%s$$$%s"%(last_key,get(total_rank,flag),overall_adj,top)

last_key=None
total_rank = 0.0
overall_adj=''
topic = ''
for line in sys.stdin:
    try:
        src,adj,top,rank = line.strip().split("\t")
        if last_key == src:
            if adj=='': total_rank += float(rank)
            else: overall_adj=adj
            if top!='': topic = top
        else:
            if last_key: printReducer(last_key,total_rank,overall_adj,topic)
            last_key=src
            if adj=='': 
                total_rank=float(rank)
                overall_adj = ''
                topic = ''
            else: 
                total_rank = 0.0
                overall_adj = adj  
                topic = top   
    except:
        #print line
        pass
if last_key: printReducer(last_key,total_rank,overall_adj,topic) 
