from pydoc import replace
from ydata_quality import DataQuality
import pandas as pd
from ydata_quality.erroneous_data import ErroneousDataIdentifier

#Load in the data
df = pd.read_csv("disney_plus_shows.csv")

# create a DataQuality object from the main class that holds all quality modules
dq = DataQuality(df=df) 

# run the tests and outputs a summary of the quality tests
results = dq.evaluate()

#statistics report
import pandas as pd
df = pd.read_csv("disney_plus_shows.csv")

df.describe(include='all')

from pandas_profiling import ProfileReport

profile = ProfileReport(df)
profile

#Dqrules
import numpy as np
import pandas as pd

# Import and read dataset
df = pd.read_csv("disney_plus_shows.csv")
df.head(17)

df['AMOUNT'].mask(df['AMOUNT'] == '', 0, inplace=True)

profile.to_file('PATH TO SAVE THE PDF REPORT')

