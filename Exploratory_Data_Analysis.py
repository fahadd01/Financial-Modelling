'''Fahad Hassan
   2020-10-0149
Financial Modelling and Analysis: Math 242
Assignment 3: Exploratory Data Analysis'''

#Importing LIbraries

import numpy as np
import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt
import statsmodels.api as sm
import datetime
from scipy.stats import norm

#Question 1

dat  = pd.read_csv('MCD_PriceDaily.csv', delimiter =',')
AC_Price = dat['Adj Close']

n = len(AC_Price)
x = np.linspace(0, n - 1, n)

plt.plot(x,AC_Price)
plt.title('1.1: Plot of Adjusted Closing Price')
plt.xlabel('Index')
plt.ylabel('Adjusted Closing Prices')
plt.show()

print('\n1.1.\nRefer to plot 1.1\n')

LogRet = np.log(AC_Price/AC_Price.shift(1))
date = dat['Date']
dat['Date'] = pd.to_datetime(dat['Date'])
Date = dat['Date']

plt.plot(Date, LogRet)
plt.title('1.3: Time Series Plot of Log Returns')
plt.xlabel('Time')
plt.ylabel('Log Returns')
plt.show()

print('1.3.\nRefer to plot 1.3\n(Following error message occurs due to missing value in .csv file)\n')

plt.hist(LogRet, bins = 80)
plt.title('1.4.A: 80 bins')
plt.xlabel('Log Returns')
plt.ylabel('Frequency')
plt.show()

plt.hist(LogRet, bins = 10)
plt.title('1.4.B: 10 bins')
plt.xlabel('Log Returns')
plt.ylabel('Frequency')
plt.show()

print('\n1.4.\nRefer to plot 1.4.A and 1.4.B\n')

LogRet[0] = LogRet[1]
sm.qqplot(LogRet, line = 'r')
plt.title('1.5: QQ Plot for Log Returns')
plt.show()

print('1.5.\nRefer to plot 1.5\n')

#Question 2

print('2.1.\nAssociated Z value = ',round(norm.ppf(0.975), 2),'\n')

N = 1000000 #sufficiently large
RandomNormal = np.random.normal(-1, np.sqrt(2), N)

print('2.2.\nAssociated Z value = ',np.quantile(RandomNormal, 0.975),'(~ actual z = ',round(-1 + 1.96*np.sqrt(2), 2),')\n')

#Question 3

start = datetime.datetime(2019, 1, 1)
end = datetime.datetime(2020, 1, 1)

Get1 = web.DataReader(['AAPL', 'IBM', 'SBUX', 'MCD'], 'yahoo', start, end)['Adj Close']
Matrix = [('Apple', Get1['AAPL']), ('IBM', Get1['IBM']), ('Starbucks', Get1['SBUX']), ("Mcdonalds", Get1['MCD'])]

n = len(Matrix)
Get1 = list()

x= np.linspace(0,1, len(Matrix[0][1]))         
figure_1, axes_1 = plt.subplots(nrows = int(n/2), ncols = int(n/2))

for i in range(n):
    Price_3 = Get1.append(Matrix[i][1])
    
for i in range (int(n/2)):
    for j in range (int(n/2)):
        a= 0 + j
        if i == 1:
            a = 1 + j
        axes_1[i,j].set_title(Matrix[i+a][0])
        axes_1[i,j].set_ylabel('Prices')
        axes_1[i,j].set_xlabel('Time')
        axes_1[i,j].plot(x, Get1[i+a])
           
figure_1.tight_layout()
plt.show()

print('3.1.\nRefer to plots 3.1\n')

Get2 = web.DataReader(['AAPL', 'IBM', 'SBUX', 'MCD'], 'yahoo', start, end)['Adj Close']
Matrix2 = [('Apple', Get2['AAPL']), ('IBM', Get2['IBM']), ('Starbucks', Get2['SBUX']), ("Mcdonalds", Get2['MCD'])]

Get2 = list()

figure_2, axes_2 = plt.subplots(nrows = int(n/2), ncols = int(n/2))

for i in range(n):
    log_returns = Get2.append(np.log(Matrix2[i][1]/Matrix2[i][1].shift(1)))

for i in range (int(n/2)):
    for j in range (int(n/2)):
        a= 0 + j
        if i == 1:
            a = 1 + j
        axes_2[i,j].set_title(Matrix2[i+a][0])
        axes_2[i,j].set_ylabel('Log Returns')
        axes_2[i,j].set_xlabel('Time')
        axes_2[i,j].plot(x, Get2[i+a])
           
figure_2.tight_layout()
plt.show()

print('3.2.\nRefer to plots 3.2\n')

for i in range (n):  
    Get1[i][0] = Get1[i][1]
    sm.qqplot(Get1[i], line = 'r')
    plt.title(Matrix[i][0])
    plt.show()
    
print('3.3.\nRefer to plots 3.3\n')

#Question 4

data = pd.read_csv('ford.csv', delimiter =',')
Returns_5 = data['FORD']

Sample_Mean = Returns_5.mean()
Sample_SD = Returns_5.std()
Sample_Median = np.quantile(Returns_5.values, 0.5)

print('4.1.\nSample Mean =',round(Sample_Mean, 5),'\nSample Median =',Sample_Median,'\nSample Standard Deviation =',round(Sample_SD, 3),'\n')

sm.qqplot(Returns_5.values, line = 'r')
plt.title('4.2: QQ Plot for Ford Returns')
plt.show()

print('4.2.\nRefer to Plot 4.2\n')
