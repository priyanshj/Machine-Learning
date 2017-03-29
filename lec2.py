# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 14:58:14 2016

@author: priyansh
"""

import pandas as pd
import quandl
import math

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
print(df.head())