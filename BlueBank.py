# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 22:42:41 2022

@author: Mahi
"""
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#method 1 to read json file 
json_file = open(' loan_data_json.json')
data = json.load(json_file)

#method 2 to read json file
# =============================================================================
# with open(' loan_data_json.json') as json_file:
#     data = json.load(json_file)
#     print(data)
# =============================================================================
#working with dictionaries


#transform to dataframe
loanData = pd.DataFrame(data)


loanData['purpose'].unique()
loanData.describe()
#describe a data for specific column
loanData['int.rate'].describe()
loanData['fico'].describe()
loanData['dti'].describe()

income = np.exp(loanData['log.annual.inc'])

loanData['annualIncome'] = income

# fico >= 300 and < 400: 'Very Poor'
# fico >= 400 and ficoscore < 600: 'Poor'
# fico >= 601 and ficoscore < 660: 'Fair'
# fico >= 660 and ficoscore < 780: 'Good'
# fico >=780: 'Excellent'

# fico = loanData['fico'][192]

# if fico >= 300 and fico < 400:
#     cat = 'Very Poor'
# elif fico >=400 and fico < 600:
#     cat = 'Poor'
# elif fico >=601 and fico < 660:
#     cat = 'Fair'
# elif fico >= 660 and fico < 780:
#     cat = 'Good'
# elif fico >=780:
#     cat = ' Excellent'
# else:
#     cat ='unknown'
    
# print(cat)


# fruits =['apples', 'oranges', 'bananas']

# for x in fruits:
#     print(x)
#     y= x+' fruit'
#     print(y)
 
print(loanData['fico'][0])

length =len(loanData)
ficocat = []
for x in range(0, length):
    category =loanData['fico'][x]
    try:
        
        if category >= 300 and category < 400:
            cat = 'Very Poor'
        elif category >=400 and category < 600:
            cat = 'Poor'
        elif category >=601 and category < 660:
            cat = 'Fair'
        elif category >= 660 and category < 780:
            cat = 'Good'
        elif category >=780:
            cat = ' Excellent'
        else:
            cat ='unknown'
    except:
        cat = 'unknown'
    ficocat.append(cat)
    
ficocat = pd.Series(ficocat)
loanData['fico.category'] = ficocat


#df.loc as conditional statements
#df.loc[df['column name'] condition , 'newcolumn name'] = value

#for inteest rate new colukmn is wanted if  rate >0.12 then high else low

loanData.loc[loanData['int.rate'] > 0.12, 'int.rate.type'] ='high'
loanData.loc[loanData['int.rate'] <= 0.12, 'int.rate.type'] ='low'

#number of rows by fico category
catPlot = loanData.groupby(['fico.category']).size()
catPlot.plot.bar(color = 'green')
plt.show()

purposePlot = loanData.groupby(['purpose']).size()
purposePlot.plot.bar(color = 'red', width = 0.2)
plt.show()

#scatter plots
ypoint = loanData['annualIncome']
xpoint = loanData['dti']
plt.scatter(xpoint, ypoint)
plt.show()

#writing to csv
loanData.to_csv('loanData_cleaned.csv', index = True)







