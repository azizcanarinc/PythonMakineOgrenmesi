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

##eksik veriler
    
#sci kit leary
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
Yas = veriler.iloc[:,1:4].values
print(Yas)
imputer = imputer.fit(Yas[:,1:4])
Yas[:,1:4] = imputer.transform(Yas[:,1:4])
print(Yas)
ulke = veriler.iloc[:,0:1].values
print(ulke)

from sklearn import preprocessing

le = preprocessing.LabelEncoder()

ulke[:,0]=le.fit_transform(veriler.iloc[:,0])
print(ulke)

ohe = preprocessing.OneHotEncoder()
ulke = ohe.fit_transform(ulke).toarray()
print(ulke)

print(list(range(22)))
sonuc= pd.DataFrame(data=ulke, index=range(22),columns=["fr","tr","us"])
print(sonuc)
sonuc2= pd.DataFrame(data=Yas, index=range(22),columns=["boy","kilo","yas"])
print(sonuc2)
cinsiyet=veriler.iloc[:,-1].values
print(cinsiyet)

sonuc3=pd.DataFrame(data=cinsiyet,index=range(22),columns=["cinsiyet"])
print(sonuc3)

s=pd.concat([sonuc,sonuc2],axis=1)
print(s)
s2=pd.concat([sonuc3,s],axis=1)
print(s2)

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test = train_test_split(s,sonuc3,test_size=0.33,random_state=0)

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
Xx_train =sc.fit_transform(x_train)
X_test =sc.fit_transform(x_test)







    