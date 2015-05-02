from urlparse import urlparse,urlunparse
def parse_url(Url):
    scheme, netloc, path, params, query, fragment = urlparse(Url)
    Blank=''
    if not netloc:
        netloc,path=path,''
    return urlunparse((scheme, netloc, Blank,Blank,Blank,Blank))

reader=open('data2.csv')
writer=open('data2_proc.csv','w')
flag=False
for line in reader:
    line=line.strip().split(',')
    if len(line)!=2 : continue
    if not flag: 
        flag=True
        continue
    url1=parse_url(line[0])
    url2=parse_url(line[1])
    newLine=url1+','+url2+'\n'
    writer.write(newLine)
reader.close()
writer.close()
