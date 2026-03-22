import pandas as pd
import numpy as np

PATH = "C:/Users/ssj34/Documents/OneDrive/python_latest/Microsimulation/Kenya-PIT-Microsimulation/"
df = pd.read_csv(PATH+"taxcalc/pit_kenya.csv")
n = len(df)
numerator = 0
for i in range(n):
    numerator = numerator + (i+1)*df['emp_income'].values[i]

denominator = n*df['emp_income'].values.sum()

gini = (2*numerator/denominator)-((n+1)/n)

def calc_gini(data):
    n = len(data)
    numerator = 0
    for i in range(n):
        numerator = numerator + (i+1)*data[i]
    
    denominator = n*data.sum()
    
    gini = (2*numerator/denominator)-((n+1)/n)
    return gini

gini1 = calc_gini(df['emp_income'].values)

gini2 = calc_gini(df['total_tax_payable_less_relief_old'].values)

print("Kakwani Index: ", gini2-gini1)