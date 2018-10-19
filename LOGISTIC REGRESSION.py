# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 20:08:46 2018

@author: CAPTAIN
"""

import numpy as np
import pandas as pd

np.set_printoptions(suppress=True)
data=pd.read_csv("Iris.csv")
data.dropna()
x=np.array(data.iloc[:,:-1])
label=[]
def data_preprocessing(data):
    temp=data["Species"]
    k=np.array(temp)
    for i in k:
        if(i=="Iris-setosa"):
            label.append([1,0,0])
        elif(i=="Iris-versicolor"):
            label.append([0,1,0])
        else:
            label.append([0,0,1])
            
one=np.ones((x.shape[0],1))
#x=np.concatenate((one,x),axis=1)
data_preprocessing(data) 
y=np.array(label)   
shuf=np.arange(y.shape[0]) 
np.random.shuffle(shuf)
x=x[shuf]
y=y[shuf]


#y=np.array(data["Species"],dtype="U5").reshape(-1,1)

alpha=0.0001

theta=np.random.randn(x.shape[1],3)*0.01
def cost(x,y,theta):
    h1=np.matmul(x,theta)
    sig=1/(1+np.exp(-h1))
    c1= (-1/x.shape[0])*np.sum(y*np.log(sig)+(1-y)*(np.log(1-sig)))
    return h1,c1

def gradient_descent(x,y):
    global theta
    iter=10900
    
    for i in range(iter):
        h2,c2=cost(x,y,theta)
        theta=theta- (alpha/x.shape[0])*(np.matmul(x.T,(h2-y)))
        
        if (i%100)==0:
            print(c2)
            

gradient_descent(x,y)
pred=x@theta
correct=0
for i in range(x.shape[0]):
    k1=np.argmax(y[i])
    k2=np.argmax(pred[i])
    if(k1==k2):
        correct+=1
print(correct/x.shape[0])
