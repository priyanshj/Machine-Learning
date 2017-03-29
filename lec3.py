# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 18:04:46 2016

@author: priyansh
"""

import pandas as pd
import quandl, math
import numpy as np
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression

df = quandl.get("WIKI/GOOGL")
#print(df.head())

df = df[['Adj. Open','Adj. Low','Adj. High','Adj. Close','Adj. Volume']]
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0
df['PCT_Change'] = (df['Adj. Open'] - df['Adj. Close']) / df['Adj. Open'] * 100.0
df = df[['Adj. Close','HL_PCT','PCT_Change','Adj. Volume']]

#print(df.head())

forecast_col = 'Adj. Close'
df.fillna(-99999, inplace=True)

forecast_out = int(math.ceil(0.01*len(df)))

df['label'] = df[forecast_col].shift(-forecast_out)
df.dropna(inplace = True)

#print(df.head())

X = np.array(df.drop(['label'],1))
y = np.array(df['label'])
X = preprocessing.scale(X)
y = np.array(df['label'])

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y,test_size = 0.2)
clf = LinearRegression()
clf.fit(X_train, y_train)
accuracy = clf.score(X_test,y_test)

print(accuracy)