# machineLearningHPI
This is a first project in exploring features of the ScyPy library. It is based upon an [online tutorial](https://pythonprogramming.net/data-analysis-python-pandas-tutorial-introduction/) by sentdex/PythonProgramming.
Gather economic data and run it through a machine learning classifier.
Then see how well it can predict if the national HPI will go up or down each month.

The code can be built as follows:
**make sure you have pip installed**

For SciPy:
```
pip install scipy-stack
```

For quandl (enjoy my api_key lol):
```
pip install quandl
```

## Download completeData.pickle and run economicIndicatorsMachineLearning.py

**or**

## Download api_key.txt and sp500.csv
The S&P500 data is available free on Yahoo Finance.

## Run percentagePickles.py 
This will generate fifty_states.pickle, fifty_states_step_pct_change.pickle, fifty_states_total_pct_change.pickle, and respective png files for their data.

Total percentage change in state HPI over time
![Total Change](https://raw.githubusercontent.com/natescholnick/machineLearningHPI/master/fifty_states_total_pct_change.png)

Stepwise percentage change in state HPI over time
![Step Change](https://raw.githubusercontent.com/natescholnick/machineLearningHPI/master/fifty_states_step_pct_change.png)


## Run additionalData.py
completeData.pickle is now generated and economicIndicatorsMachineLearning.py should run.

## Run economicIndicatorsMachineLearning.py

Right now, the program only outputs a number between 0 and 1, the accuracy of its guesses after training on only the total percentage data. I plan to expand upon this, both with data visualization for what the classifier is doing, and by comparing results when feeding in step precentage change data.

**As time goes on, the most likely culprit for hiccups, should you encounter any, will be pulling the data from Quandl and elsewhere. URLs change, column names change, data may be put behind a paywall, etc. Luckily, this will usually be an easy tweak.**




