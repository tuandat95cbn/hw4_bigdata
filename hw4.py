def hash(a,b,p,ee,x):
    y= x%p
    hash_val=(a*y+b) %p
    return hash_val % ee
a=[]
b=[]
import math
f=open('hash_params.txt','r')
tmp=f.read()
v=tmp.split('\n')
v.pop(len(v)-1)
for i in v:
    z=i.split('\t')
    a.append(int(z[0]))
    b.append(int(z[1]))
print a,b
f.close()
f=open('words_stream.txt','r')
x=f.readline()
t=0;
ee=10000
import numpy as np
c=np.zeros((5,10000),dtype=int)
while True:
    t+=1;
    z=x.split('\n')
    for i in range(0,5):
        xx=hash(a[i],b[i],123457,ee,int(z[0]))
        c[i][xx]+=1;
    x=f.readline()
    if x=='': 
        break
    if (t % 100000 ==0):
    	print t
f.close
print c
f=open('counts.txt','r')
E=[];
T=[]
count=0
belowone=[]
while True:
    count +=1
    x=f.readline()
    if x=='': 
		break
    z=x.split('\n')
    zz=z[0].split('\t')

    min=100000000000;
    for i in range(0,5):
        xx=hash(a[i],b[i],123457,ee,int(zz[0]))
        if c[i][xx]<min : min=c[i][xx]
    if (min-float(zz[1]))/float(zz[1]) <1 :
        belowone.append(zz[0])
    E.append((min-float(zz[1]))/float(zz[1]))
    T.append(float(zz[1])/t)
    if count % 100000==0:
        print count 
   
print E[0:10],T[0:10] 
f.close()
f=open('belowone.txt','w')
for i in belowone:
    print >> f, i 
f.close()
for i in range(len(E)):
    E[i]=math.log10(E[i])
for i in range(len(T)):
    T[i]=math.log10(T[i])

import matplotlib.pyplot as plt
plt.plot(T,E,'ro')
plt.show()
