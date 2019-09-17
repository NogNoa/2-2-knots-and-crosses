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
       win=win or L[Size*i]==L[Size*i+1] or L[Size*i]==L[Size*i+Size] or L[Size*i]==L[Size*i+Size+1]