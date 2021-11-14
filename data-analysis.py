from numpy.core.fromnumeric import mean
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

alumni = pd.read_csv('alumni.csv')
#print(alumni.describe())
def clean_currency(curr):
    return float(curr.replace(',', '').replace('$', ''))

alumni['Savings'] = alumni['Savings ($)'].agg(clean_currency)
#print(alumni['Gender'].value_counts())

#Replace "M" with "Male"
alumni['Gender'] = alumni['Gender'].str.replace(r'^M$', 'Male', regex=True)

#print(alumni['Gender'].value_counts())
#Find the mean, median and stardard deviation
salary = alumni['Salary'].agg([np.mean, np.median, np.std])
#print(salary)
#print(alumni['Fee'].value_counts())
over_15000 = alumni[alumni['Fee'] >=15000]
print(over_15000)