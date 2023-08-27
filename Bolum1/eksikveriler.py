# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 22:29:23 2023

@author: AzizCan
"""

#ders 6
#imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#kodlar
#veri yükleme
veriler=pd.read_csv("eksikveriler.txt")
print(veriler)
"""
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
"""
##eksik veriler
    
#sci kit leary
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
Yas = veriler.iloc[:,1:4].values
print(Yas)
imputer = imputer.fit(Yas[:,1:4])
Yas[:,1:4] = imputer.transform(Yas[:,1:4])
print(Yas)










    