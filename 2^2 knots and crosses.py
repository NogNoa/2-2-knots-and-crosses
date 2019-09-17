# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 11:00:59 2019

@author: omer
"""
def Check_win(L,Size):
    if type(L)!=list:
        print('This isn\'t a list mate')
        return
    L=L[:Size**2]
    win=False
    for i in range(Size):
        print('i=',i)
        for j in [1,Size,Size+1]:
            print('j=',j)
            win= win or L[Size*i]==L[Size*i+j]
            print('win=',win)
    return win
print(Check_win([1,2,0,4],2))