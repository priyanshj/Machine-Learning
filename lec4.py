# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 10:04:15 2016

@author: priyansh
"""

import pandas as pd
import quandl, math, time
import numpy as np
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style
import datetime

style.use('ggplot')

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


#print(df.head())

X = np.array(df.drop(['label'],1))
X = preprocessing.scale(X)

X = X[:-forecast_out]
X_lately = X[-forecast_out:]

df.dropna(inplace = True)
#y = np.array(df['label'])
y = np.array(df['label'])

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y,test_size = 0.2)
clf = LinearRegression()
clf.fit(X_train, y_train)
accuracy = clf.score(X_test,y_test)

#print(accuracy)

forecast_set = clf.predict(X_lately)
print(forecast_set,accuracy,forecast_out)

df['Forecast'] = np.nan

last_date = df.iloc[-1].name
last_unix = time.mktime(last_date.timetuple()) #valid for python 2.7
#last_unix = last_date.timestamp()    #it is valid only in python 3
one_day = 86400
next_unix = last_unix + one_day

for i in forecast_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += one_day
    df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)] + [i]
    
print(df.tail())
    
df['Adj. Close'].plot()
df['Forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()