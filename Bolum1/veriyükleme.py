# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 22:29:23 2023

@author: AzizCan
"""

#ders 6
#imports
import pandas as pd
import numba as pn
import matplotlib.pyplot as plt

#kodlar
#veri yükleme
veriler=pd.read_csv("veriler.txt")
print(veriler)

#veri ön isleme
boy=veriler[["boy"]]
print(boy)

boykilo=veriler[["boy","kilo"]]
print(boykilo)

x=10

class insan:
    boy= 180
    def kosmak(self,b):
        return b + 10
        
    
aziz=insan()
print(aziz.boy)
print(aziz.kosmak(30))
    
    
    
    