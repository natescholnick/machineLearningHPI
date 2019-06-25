# -*- coding: utf-8 -*-
"""
Created on Wed May 29 13:41:26 2019

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

HPI_data['MA1yr'] = HPI_data['MA'].resample('A').mean()

# MA1yr will not plot because of NaN values
print(HPI_data[['MA','MA1yr']].head())

# This will delete all rows with NaN values
# Problem is, now monthly MA only gets 1 data point per year
#HPI_data.dropna(how='all', inplace=True)

# This will fill NaN values. There is method= ffill, bfill
# A value= can be chosen, any number or string
# limit= will regulate how many NaN are filled, depends on method vs value
HPI_data.fillna(method='ffill', inplace=True)

print(HPI_data[['MA','MA1yr']])

# Count and print the remaining # of NaN entries
print(HPI_data.isnull().values.sum())

HPI_data[['MA','MA1yr']].plot(ax = ax1)

plt.legend(loc=2)
plt.show()
