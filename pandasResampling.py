# -*- coding: utf-8 -*-
"""
Created on Tue May 28 16:09:28 2019

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
ax1 = plt.subplot2grid((1,1),(0,0))

HPI_data = pd.read_pickle('fifty_states_total_pct_change.pickle')

# =============================================================================
# Here is the resampling function!
# =============================================================================
MA1yr = HPI_data['MA'].resample('A', how='mean') # mean is default, ohlc = open, high, low, close
print(MA1yr.head())

HPI_data['MA'].plot(ax = ax1, label='Monthly')
MA1yr.plot(ax = ax1, label='Yearly')

plt.legend(loc=2)
plt.show()



