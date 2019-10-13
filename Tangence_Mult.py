# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 15:51:46 2019

@author: omer
"""

def TangenceMult(n):
    T=[]
    p,q=[0],[0]
    for i in range(n):
        p.append(0)
        q.append(0)
        for j in range(len(p)-1,0,-1):
            p[j]=p[j]-q[j-1]
            q[j]=q[j]+p[j-1] 
        p[1]+=1        
        #print('a',a)
        #print ('b',q)
        T.append('('+str(p)+','+str(q)+')')
    return T
print(TangenceMult(10))