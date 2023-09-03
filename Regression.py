''' 2020-10-0149
    Fahad Hassan
Financial Modelling and Analysis: Math 242
Assignment 4: Regression'''

#Importing Libraries

import numpy as np
import scipy.stats as stats
from scipy.stats import f
import datetime
import pandas_datareader as web
import statsmodels.api as sm

#Question 3

beta0 = 2
beta1 = 1
Var = 0.6

Mean_Con = beta0 + beta1
SD_Con = np.sqrt(Var)

CDF = stats.norm.cdf(3, Mean_Con, SD_Con)

print('3.\nConditional Mean =',Mean_Con,'\nConditional Standard Deviation =', round(SD_Con,4),'\nAssociated Probability =',CDF,'\n')

#Question 4

dfR = 2                         # No. of predictor variables
SSe = 3.250
p = 0.05

dfe = 14 - dfR

F = f.ppf(1-p, dfR, dfe)

MSe = SSe/12                    # MSE = SSE/dfE
MSR = F*MSe                     # f = MSR/MSE
SSR = MSR*dfR                   # MSR = SSR/dfR
SSt = SSe + SSR

x = SSe/SSt                     # R^2 = 1-(SSE*SST)
R_Square = 1 - x

print('4.\ndf Regression =', dfR,'df error =', dfe)
print('SS Regression =', round(SSR,3),'SS total =', round(SSt,3))
print('MS Regression =', round(MSR,3),'MS error =', round(MSe,3))
print('F-value =', round(F,3),'\nRsquare =', round(R_Square,3),'\n')

#Question 5

start = datetime.datetime(2019, 1, 1)
end = datetime.datetime(2020, 1, 1)

data = web.DataReader(['AAPL', 'IBM', 'MSFT'], 'yahoo', start, end)['Adj Close']

AAPL = data['AAPL']
IBM = data['IBM']
MSFT = data['MSFT']

AAPL_log = np.log(AAPL/AAPL.shift(1))
IBM_log = np.log(IBM/IBM.shift(1))
MSFT_log = np.log(MSFT/MSFT.shift(1))

AAPL_Log = np.zeros(len(AAPL_log)-1)
IBM_Log = np.zeros(len(IBM_log)-1)
MSFT_Log = np.zeros(len(MSFT_log)-1)

for i in range (len(AAPL_log)-1):
    AAPL_Log[i]=AAPL_log[i+1]
    IBM_Log[i]=IBM_log[i+1]
    MSFT_Log[i]=MSFT_log[i+1]

X = list()
Y = list()

for i in range (len(AAPL_Log)): 
    X.append([(MSFT_Log[i]), IBM_Log[i]])
    Y.append(AAPL_Log[i])

X = sm.add_constant(X)
model = sm.OLS(Y,X).fit()
predictions = model.predict(X) 
print('5.1.\n',model.summary())

dfk = 2
dfd = 3*(len(Y)-1)
F = stats.f_oneway(AAPL_Log, IBM_Log, MSFT_Log)
print('\n5.2.\nConfidence Level = ', f.pdf(F, dfk, dfd)*100,'%')
