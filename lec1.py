# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 10:20:21 2016

@author: priyansh
"""

import pandas as pd
import quandl

df = quandl.get("WIKI/GOOGL")
#print(df.head())

df = df[['Adj. Open','Adj. Low','Adj. High','Adj. Close','Adj. Volume']]
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0
df['PCT_Change'] = (df['Adj. Open'] - df['Adj. Close']) / df['Adj. Open'] * 100.0
df = df[['Adj. Close','HL_PCT','PCT_Change','Adj. Volume']]

print(df.head())