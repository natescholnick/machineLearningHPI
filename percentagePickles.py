# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 11:32:09 2019

@author: Nate
"""

import pandas as pd
import quandl
import matplotlib.pyplot as plt

api_key=open("api_key.txt", "r").read()

def state_list():
    states_df = pd.read_html('https://en.wikipedia.org/wiki/List_of_U.S._state_abbreviations', header=0)[0]
    fifty_states = states_df.iloc[:,5][11:62]
    fifty_states.drop([19], inplace=True)
    return fifty_states

# With bulky objects, such as this quandl query, pickling is how
# we save them for faster future referencing. 
def grab_initial_state_data():
    main_df = pd.DataFrame()
    states = state_list()
    for abbv in states:
       query = "FMAC/HPI_"+str(abbv)+'.2'
       df = (quandl.get(query, authtoken=api_key)).rename(columns={'SA Value':str(abbv)})
       if main_df.empty:
           main_df = df
       else:
           main_df = main_df.join(df)
   
    main_df.to_pickle('fifty_states.pickle')
  
# After run once the pickle file is generated  
#grab_initial_state_data() 
    
HPI_data = pd.read_pickle('fifty_states.pickle')
#print(HPI_data)

HPI_data.plot()
plt.legend().remove()
plt.savefig('fifty_states_original.png', bbox_inches='tight')

HPI_data.pct_change().to_pickle('fifty_states_step_pct_change.pickle')

HPI_data.pct_change().plot()
plt.legend().remove()
plt.savefig('fifty_states_step_pct_change.png', bbox_inches='tight')


for column in HPI_data:
    HPI_data[column] = HPI_data[column] = (HPI_data[column] - HPI_data[column][0]) / HPI_data[column][0] * 100

HPI_data.to_pickle('fifty_states_total_pct_change.pickle')

HPI_data.plot()
plt.legend().remove()
plt.savefig('fifty_states_total_pct_change.png', bbox_inches='tight')
plt.show()