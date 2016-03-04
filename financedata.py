# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 18:55:23 2016

@author: rlobel
"""
import pandas as pd
import pandas.io.data as web
import datetime as dt # Standard Python date / time library
start, end = dt.datetime(2006, 1, 1), dt.datetime(2012, 12, 31)
ticker_list = {'INTC': 'Intel',
'MSFT': 'Microsoft',
'IBM': 'IBM',
'BHP': 'BHP',
'RSH': 'RadioShack',
'TM': 'Toyota',
'AAPL': 'Apple',
'AMZN': 'Amazon',
'BA': 'Boeing',
'QCOM': 'Qualcomm',
'KO': 'Coca-Cola',
'GOOG': 'Google',
'SNE': 'Sony',
'PTR': 'PetroChina'}
returns=pd.DataFrame({'cos':ticker_list.values()},index=ticker_list.keys())
temp = pd.Series(0.0,ticker_list.keys())
#data = web.DataReader('UNRATE', 'fred', start, end)
for key in ticker_list.keys():
 prices = web.DataReader(key, 'google', start,end)
 temp[key] = (prices.ix[end,3]-prices.ix[0,0])/prices.ix[0,0]

returns['Returns']=temp
returns.plot(kind='bar')
#add comment here
#import matplotlib.pyplot as plt
#plt.show()
