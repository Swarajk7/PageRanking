f=open('rank0')
n=4
M1=[[0]*n for i in range(n)]
M=[[0]*n for i in range(n)]
v=[0]*n

'''take Input'''

for i in f:
    line=i.strip()
    z=line.split(' ')
    #print z
    _id=int(z[0])
    vv=z[1].split('#')
    v[_id]=float(vv[0])
    zz=vv[1].split(',')
    for z in zz:
        if len(z)>0:
            M1[_id][int(z)]=1.0/len(zz)

for i in range(n):
    for j in range(n): M[i][j]=M1[i][j]
    

beta = 0.85
'''for i in range(n):
    for j in range(n):
        M[i][j]=beta*M[i][j]+(1-beta)*(1.0/n)'''

def mul(v):
    V=[0]*n
    for i in range(n):
        s=0.0
        for j in range(n):
            #print v[j],M[i][j],v[j]*M[i][j]
            s=s+v[j]*M[j][i]
        V[i]=s
    #print V
    return V
    
def diff(v1,v2):
    val=0
    for (a,b) in zip(v1,v2):
        val=max(val,(b-a)**2)
    return val

count=0

while True:
    v_new=mul(v)
    for i in range(len(v_new)): v_new[i]=beta*v_new[i]+(1-beta)*(1.0/n)
    #break
    if count>=100 or diff(v,v_new) <= 0.00001:
        v=v_new
        break
    v=v_new
    count+=1
print count
for i in range(len(v)):
    print i,v[i]*1000
