# -*- coding: utf-8 -*-
"""
Created on Fri May 31 12:57:20 2019

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
    return df
    
#grab_initial_state_data()   
    
fig = plt.figure()
ax1 = plt.subplot2grid((2,1),(0,0))
# We create a new set of axes, with the grid now (2,1)
# 2 tall, 1 wide. A graph on top and a graph on bottom.
ax2 = plt.subplot2grid((2,1),(1,0), sharex=ax1)

HPI_data = pd.read_pickle('fifty_states_total_pct_change.pickle')

## This rolling method is super powerful! It will calculate
## rolling stats over (x) time increments. This means data will
## not populate before the xth row though, a problem for large x 
#HPI_data['MA12mean'] = HPI_data['MA'].rolling(12).mean()
#HPI_data['MA12std'] = HPI_data['MA'].rolling(12).std()
#
#print(HPI_data[['MA','MA12mean','MA12std']].head())
#
## dropna will cut off starting data until row x, but that may
## remove an excessive portion of data.
##HPI_data.dropna(how='all', inplace=True)
#
#HPI_data[['MA','MA12mean']].plot(ax = ax1)
#HPI_data['MA12std'].plot(ax = ax2)

# This is 12 month rolling correlation between MA and TX HPIs
MA_TX_12corr = HPI_data['MA'].rolling(12).corr(HPI_data['TX'])

HPI_data['MA'].plot(ax = ax1, label='MA HPI')
HPI_data['TX'].plot(ax = ax1, label='TX HPI')
ax1.legend(loc=2)

MA_TX_12corr.plot(ax = ax2, label='Corr')

plt.legend(loc=3)
plt.show()
