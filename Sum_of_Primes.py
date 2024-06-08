
import math
def top(a,mas,ar):   #asalları bulmak için
    i=2
    el=a*i
    while el<=mas:
        ar[el -1]=1
        i+=1
        el=a*i

def bul(mass):
    ar=[0]*mass
    nn=[False]*mass
    for i in range(1, mass-1):
        if ar[i]==0:
            top(i+1,mass-1,ar)
            nn[i+1]=True
    return nn

def dal(l,r, nn):
    return nn[r]-nn[l-1]


max=1000003
var=bul(max)
nn=[0]*max
for i in range(1,max):
    if var[i]:
        val=i
    else:
        val=0
    nn[i]=nn[i-1]+ val


n=int(input())
for w in range(n):
    l,r=map(int,input().split())
    m=dal(l, r, nn)
    print(m)