import pandas as pd
import numpy as np

alumni = pd.read_csv('alumni.csv')
#print(alumni.describe())
def clean_currency(curr):
    return float(curr.replace(',', '').replace('$', ''))

alumni['Savings'] = alumni['Savings ($)'].agg(clean_currency)
print(alumni['Gender'].value_counts())

#Replace "M" with "Male"


#print(alumni['Savings'])