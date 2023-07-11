# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 09:41:55 2019

@author: Soheila
"""
#import libraries
import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
#%matplotlib inline

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#loading the data
bankdata = pd.read_csv("file:///C:/Users/Home/Desktop/bill_authentication.csv")
#show raws and columns of data
bankdata.head() 
 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#divide the data into attributes and lables
X = bankdata.drop('Class', axis=1)  #stored all data in X except Class
y = bankdata['Class']               #stored CLass attribute in Y 

#divide the data into train and test with model_selection library
from sklearn.model_selection import train_test_split  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#train the training set
from sklearn.svm import SVC  
svclassifier = SVC(kernel='linear', probability=True)  
svclassifier.fit(X_train, y_train)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#prediction
y_pred = svclassifier.predict(X_test) 

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Evaluation 
from sklearn.metrics import classification_report, confusion_matrix  
print(confusion_matrix(y_test,y_pred))  
print(classification_report(y_test,y_pred))  

plt.show(train_test_split(X,y))