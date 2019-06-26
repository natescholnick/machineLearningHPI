# machineLearningHPI
This was is a first project in exploring features of the ScyPy library. It is based upon an online tutorial by sendex.
Gather economic data and run it through a machine learning classifier.
Then see how well it can predict if the national HPI will go up or down each month.

The code can be built as follows:
**make sure you have pip installed

For SciPy:
**pip install scipy-stack

For quandl (enjoy my api_key lol):
**pip install quandl

### Download completeData.pickle and run economicIndicatorsMachineLearning.py

**or

### Download api_key.txt and sp500.csv
The S&P500 data is available free on Yahoo Finance.

### Run percentagePickles.py 
This will generate fifty_states.pickle, fifty_states_step_pct_change.pickle, fifty_states_total_pct_change.pickle, and respective png files for their data.

### Run additionalData.py
completeData.pickle is now generated and economicIndicatorsMachineLearning.py should run.

### Run economicIndicatorsMachineLearning.py

*As time goes on, the most likely culprit for hiccups, should you encounter any, will be pulling the data from Quandl and elsewhere. URLs change, column names change, data may be put behind a paywall, etc. Luckily, this will usually be an easy tweak.




