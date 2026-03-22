import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
#from stata_python import *

def calc_taxamt(income, rate, bracket):
    """
    Compute tax amount given the specified taxable income
    and the specified progressive tax rate structure.
    """ 
    tax_amount = (
        rate[1] * min(income, bracket[1]) +
        rate[2] * min(bracket[2] - bracket[1], max(0, income - bracket[1])) +
        rate[3] * min(bracket[3] - bracket[2], max(0, income - bracket[2])) +
        rate[4] * min(bracket[4] - bracket[3], max(0, income - bracket[3])) +
        rate[5] * min(bracket[5] - bracket[4], max(0, income - bracket[4])) +
        rate[6] * min(bracket[6] - bracket[5], max(0, income - bracket[5])) +
        rate[7] * min(bracket[7] - bracket[6], max(0, income - bracket[6]))        
    )
    return tax_amount

def marg_rate(income_list, rate, bracket):
    marginal_rate=np.zeros(len(income_list))
    for i in range(len(df)):
        if income_list[i]< bracket[1]:
            marginal_rate[i]=rate[1]
        elif income_list[i]< bracket[2]:
            marginal_rate[i]=rate[2]
        elif income_list[i]< bracket[3]:
            marginal_rate[i]=rate[3]
        elif income_list[i]< bracket[4]:
            marginal_rate[i]=rate[4]
        elif income_list[i]< bracket[5]:
            marginal_rate[i]=rate[5]        
        elif income_list[i]< bracket[6]:
            marginal_rate[i]=rate[6]
        else:
            marginal_rate[i]=rate[7]
    
    return marginal_rate

df = pd.read_csv("taxcalc/pit_kenya.csv")
df = df.sort_values(['emp_income'])
pitax=np.zeros(len(df))
rate = [0, 0.1, 0.25, 0.30, 0.325, 0.35, 0.35, 0.35]
bracket = [0, 288000, 388000, 6000000, 9600000, 1e+99, 2e+99, 9e+99]

personal_relief = 28800
for i in range(len(df)):
    pitax[i]=calc_taxamt(df['emp_income'].values[i], rate, bracket)
    pitax[i] = max(pitax[i]-personal_relief,0)

df['tax1'] = pitax

df['weighted_tax1'] = df['tax1']*df['weight']

df['atr1']=df['tax1']/df['emp_income']

marginal_rate1 = marg_rate(df['emp_income'].values, rate, bracket)
df['marginal_rate1'] = marginal_rate1

print("Revenue First Schedule (bill): ", df['weighted_tax1'].sum()/1e9)

#### Second Reform Option
pitax=np.zeros(len(df))
rate = [0, 0.1, 0.25, 0.30, 0.325, 0.40, 0.40, 0.40]
bracket = [0, 288000, 388000, 6000000, 9600000, 1e+99, 2e+99, 9e+99]

personal_relief = 28800
for i in range(len(df)):
    pitax[i]=calc_taxamt(df['emp_income'].values[i], rate, bracket)
    pitax[i] = max(pitax[i]-personal_relief,0)

df['tax2'] = pitax

df['weighted_tax2'] = df['tax2']*df['weight']

df['atr2']=df['tax2']/df['emp_income']

marginal_rate2 = marg_rate(df['emp_income'].values, rate, bracket)
df['marginal_rate2'] = marginal_rate2

print("Revenue Second Schedule (bill): ", df['weighted_tax2'].sum()/1e9)

df['net_of_marginal_rate1'] = 1-df['marginal_rate1']
df['net_of_marginal_rate2'] = 1-df['marginal_rate2']

df['pct_change_net_marginal_rate']=(df['net_of_marginal_rate2']-df['net_of_marginal_rate1'])/df['net_of_marginal_rate1']

elasticity = 0.2 
df['pct_change_income'] = elasticity*df['pct_change_net_marginal_rate']
df['change_income'] = df['pct_change_income']*df['emp_income']
df['emp_income_behavior']=df['emp_income']+df['change_income']

### With Behavior Adjustment
pitax=np.zeros(len(df))
rate = [0, 0.1, 0.25, 0.30, 0.325, 0.40, 0.40, 0.40]
bracket = [0, 288000, 388000, 6000000, 9600000, 1e+99, 2e+99, 9e+99]

personal_relief = 28800
for i in range(len(df)):
    pitax[i]=calc_taxamt(df['emp_income_behavior'].values[i], rate, bracket)
    pitax[i] = max(pitax[i]-personal_relief,0)

df['tax3'] = pitax

df['weighted_tax3'] = df['tax3']*df['weight']

print("Revenue Second Schedule with Behavior Adjustment (bill): ", df['weighted_tax3'].sum()/1e9)


