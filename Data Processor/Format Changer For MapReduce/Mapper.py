#!/usr/bin/env python
import sys
for line in sys.stdin:
    line=line.strip()
    links = line.split(',')
    if len(links)!=2: continue
    print '%s\t%s' % (links[0], links[1])
    print '%s\t%s' % (links[1],'')
