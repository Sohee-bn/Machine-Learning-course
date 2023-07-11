#################################################
##  course:    Machine learning                ##
##  Prof:      Dr Razzaghi                     ##
##  HomeWork:  1                               ##
##      Soheila Behrooznia & Mahkameh Salehi   ##
##                winter 2019                  ##
#################################################

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets,linear_model
from sklearn.metrics import mean_squared_error,r2_score
from sklearn import linear_model


#read data
features = pd.read_csv('file:///C:/Users/Mahkameh/Desktop/features.csv')
labels = pd.read_csv('file:///C:/Users/Mahkameh/Desktop/labels.csv')

# Split train and test sets
train_features = features[30:]
train_labels = labels[30:]

test_features =  features[0:30]
test_labels =  labels[0:30]

#model(w)
ols = linear_model.LinearRegression()
model = ols.fit(train_features, train_labels)


list(model.predict(test_features))
list(model.predict(test_labels))

#part 1
plt.scatter(features, labels ,color='g')
plt.plot(train_features, model.predict(train_features),color='r')
plt.show()

