# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import quandl

api_key=open("api_key.txt", "r").read()

df=quandl.get('FMAC/HPI_AK', authtoken=api_key)
#print(df.head())

# =============================================================================
# This will read in every table on the page and generate a list
# of data frames. We are lucky that the page only has 1 table.
# Still, we will include index [0] as consistent syntax.
# =============================================================================
fifty_states=pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states', header=0)

# The index will make it a single data frame
# print(fifty_states[0])

# This is a column
# Selecting the column by name will work, but it can only be iterated
# over if it is identified as a header within the data frame
# print(fifty_states[0]['Abbreviation'])
    
for abbv in fifty_states[0]['Abbreviation']:
   print("FMAC/HPI_"+str(abbv))
  
#This can also be accomplished by numerically selecting the column as follows    
#for abbv in fifty_states[0][fifty_states[0].columns[1]]:
#   print("FMAC/HPI_"+str(abbv))