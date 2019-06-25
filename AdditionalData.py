# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 10:05:29 2019

@author: Nate
"""

import pandas as pd
import quandl
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

api_key=open("api_key.txt", "r").read()

def state_list():
    fifty_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states', header=0)
    return fifty_states[0]['Abbreviation'][1:]
 
def grab_initial_state_data():
    main_df = pd.DataFrame()
    states = state_list()
    for abbv in states:
       query = 'FMAC/HPI_'+str(abbv)+'.2'
       df = quandl.get(query, authtoken=api_key).rename(columns={'SA Value':str(abbv)})
       df[abbv] = (df[abbv] - df[abbv][0]) / df[abbv][0] * 100
       
       if main_df.empty:
           main_df = df
       else:
           main_df = main_df.join(df)
           
    print(main_df.head())
   
    pickle_out = open('fifty_states.pickle','wb')
    pickle.dump(main_df, pickle_out)
    pickle_out.close()
    
def HPI_Benchmark():
    df = quandl.get('FMAC/HPI_USA.2', authtoken=api_key).rename(columns={'SA Value':'USA'})
    df['USA'] = (df['USA'] - df['USA'][0]) / df['USA'][0] * 100
    df.rename(columns={'USA':'US_HPI'}, inplace=True)
    return df

def mortgage30y():
    df = quandl.get('FMAC/MORTG', trim_start='1975-01-01', authtoken=api_key).rename(columns={'Value':'Mortgage30y'})
    df['Mortgage30y'] = (df['Mortgage30y'] - df['Mortgage30y'][0]) / df['Mortgage30y'][0] * 100
    df = df.resample('D').interpolate()
    df = df.resample('M').interpolate()
    return df

def sp500Data():
    df = pd.read_csv('sp500.csv', index_col='Date')
    df.index = pd.to_datetime(df.index)
    df['Adj Close'] = (df['Adj Close'] - df['Adj Close'][0]) / df['Adj Close'][0] * 100
    df = df.resample('M').interpolate()
    df.rename(columns={'Adj Close':'sp500'}, inplace=True)
    df = df['sp500']
    return df

def gdpData():
    df = quandl.get('FRED/GDP', trim_start='01-01-1975', authtoken=api_key).rename(columns={'Value':'GDP'})
    df['GDP'] = (df['GDP'] - df['GDP'][0]) / df['GDP'][0] * 100
    df = df.resample('D').interpolate()
    df = df.resample('M').interpolate()
    return df

def unemployment():
    df = quandl.get('USMISERY/INDEX.1', trim_start='01-01-1975', authtoken=api_key)
    return df

usUnemployment = unemployment()
US_GDP = gdpData()
sp500 = sp500Data()
m30 = mortgage30y()
HPI_data = pd.read_pickle('fifty_states_total_pct_change.pickle')
HPI_bench = HPI_Benchmark()

completeData = HPI_data.join([HPI_bench, m30, sp500, US_GDP, usUnemployment])
completeData.dropna(inplace = True)

completeData.to_pickle('completeData.pickle')
