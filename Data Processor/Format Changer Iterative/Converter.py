f=open('dataTest.csv')
d={}
for l in f:
    l=l.strip().split(',')
    if len(l)!=2: continue
    src,dest=l
    if src in d.keys():
        d[src].append(dest)
    else:
        d[src]=[dest]
    if dest not in d.keys():
        d[dest]=[]
for key in d:
    if ' ' in key: continue
    z=d[key]
    adj=''
    if len(z)!=0:    
        for i in range(len(z)-1): adj+=z[i]+','
        adj+=z[-1]
    top='un'
    if 'nitrkl' in key: top='nitrkl'
    elif 'cet' in key: top='cet'
    elif 'iiit' in key: top='iiit'
    print "%s 1.0###%s$$$%s"%(key,adj,top)
    
