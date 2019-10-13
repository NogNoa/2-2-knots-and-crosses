# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 15:51:46 2019

@author: omer
"""

def TangenceMult(n):
    T=[]
    p,q=[0],[0]
    a,b=[0],[0]
    for i in range(n):
        for j in range(len(a)):
            a[j]=a[j]-q[j]
        a[0]+=1
        #print('a',a)
        for j in range(len(b)):
            print (b[j],p[j])
            b[j]=b[j]+p[j]
        #print ('b',q)
        p+=a
        q+=b
        T.append('('+str(p)+','+str(q)+')')
        a=p[1:]
        b=q[1:]
        print(p,q,a,b)
    return T
print(TangenceMult(3))