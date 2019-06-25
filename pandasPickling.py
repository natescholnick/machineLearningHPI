# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import quandl
import pickle

api_key=open("api_key.txt", "r").read()

def state_list():
    fifty_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states', header=0)
    return fifty_states[0]['Abbreviation'][1:]

# With bulky objects, such as this quandl query, pickling is how
# we save them for faster future referencing. 
def grab_initial_state_data():
    main_df = pd.DataFrame()
    states = state_list()
    for abbv in states:
       query = "FMAC/HPI_"+str(abbv)
       df = (quandl.get(query, authtoken=api_key)).rename(columns={'NSA Value':'NSA_'+str(abbv),'SA Value':'SA_'+str(abbv)})
       
       if main_df.empty:
           main_df = df
       else:
           main_df = main_df.join(df)
   
    pickle_out = open('fifty_states.pickle','wb') # wb = write bytes
    pickle.dump(main_df, pickle_out)
    pickle_out.close()
  
# After run once the pickle file is generated  
# grab_initial_state_data() 
    
pickle_in = open('fifty_states.pickle','rb') # rb = read bytes
HPI_data = pickle.load(pickle_in)
print(HPI_data)

# In pandas, this pickling process has sleeker syntax, as well
# as being marginally faster for very large data sets:
# HPI_data.to_pickle('example.pickle')
# HPI_data2 = pd.read_pickle('example.pickle')