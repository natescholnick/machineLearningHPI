# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 20:36:32 2019

@author: Nate
"""

import pandas as pd
import quandl
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
from sklearn import svm, preprocessing, model_selection

style.use('ggplot')

api_key=open("api_key.txt", "r").read()

def create_labels(curHPI, futHPI):
    if futHPI > curHPI:
        return 1
    else:
        return 0

housing_data = pd.read_pickle('completeData.pickle')

housing_data = housing_data.pct_change()
housing_data.replace([np.inf, -np.inf], np.nan, inplace=True)
housing_data['US_HPI_future'] = housing_data['US_HPI'].shift(-1)
housing_data.dropna(inplace=True)

housing_data['label'] = list(map(create_labels, housing_data['US_HPI'], housing_data['US_HPI_future']))

X = np.array(housing_data.drop(['label','US_HPI_future'], 1))
X = preprocessing.scale(X)
y = np.array(housing_data['label'])

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.15)

clf = svm.SVC(kernel='linear')
clf.fit(X_train, y_train)

print(clf.score(X_test, y_test))