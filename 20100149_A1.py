'''
Financial Modelling and Analysis
Assisnment 1
Fahad Hassan
2020-10-0149
'''

#Importing Libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import pandas as pd

#Question 2
print('__________________________________________________\n\nQuestion 2\n__________________________________________________\n')

meu = 0.0002
sigma = 0.03

meu_20= 20*meu
sigma_20= np.sqrt(20)*sigma
x=np.log(100/97)

CDF_norm_dist=norm.cdf(x, loc=meu_20, scale=sigma_20)
P=1-CDF_norm_dist
print('Associated Probability = ',P,'\n')

#Question 3
print('__________________________________________________\n\nQuestion 3\n__________________________________________________\n')

#Part 2
print('__________________________________________________\n\nPart 2\n__________________________________________________\n')

meu3 = 0.06
var = 0.47

meu_4= 4*meu3
std_4= np.sqrt(4*var)
x_value=2

p=norm.cdf(2, loc=meu_4, scale=std_4)

print('Associated Probability = ',p,'\n')

#Question 4
print('__________________________________________________\n\nQuestion 4\n__________________________________________________\n')

mean=0.1
std=0.2

#Part 1
print('__________________________________________________\n\nPart 1\n__________________________________________________\n')

new_mean=3*mean
new_std=np.sqrt(3)*std
Z= np.log(1.2)

norm_dist= norm.cdf(Z ,new_mean, new_std)
Prob= 1-norm_dist

print('Associated Probability = ',Prob,'\n')

#Part 3
print('__________________________________________________\n\nPart 3\n__________________________________________________\n')

t=1                         #Day One
norm_dist_value= 0.01          
prob_value= 0.01
Z_value= np.log(2)

while prob_value < 0.900:
    new_mean= mean*t
    new_std= np.sqrt(t)*std        
    norm_dist_value= norm.cdf(Z_value, loc=new_mean, scale=new_std)
    prob_value= 1- norm_dist_value
    t=t+1

print('At t = ',t,' days, probability = ',prob_value,' > 0.09\n=> Minimum Days = ',t-1,'\n')

#Question 5
print('__________________________________________________\n\nQuestion 5\n__________________________________________________\n')
dat = pd.read_csv("Stock_Bond.csv", delimiter=',')

#Part 1
print('__________________________________________________\n\nPart 1\n__________________________________________________\n')

gm_ac = dat['GM_AC']
f_ac = dat ['F_AC']

n= gm_ac.size

gr_gm_ac=np.zeros(n-1)    # Gross Return arrays 
gr_f_ac=np.zeros(n-1)

for i in range (n-1):
    gr_gm_ac[i]=gm_ac[i+1]/gm_ac[i]
    gr_f_ac[i]=f_ac[i+1]/f_ac[i]
    
print ('Gross Returns for GM_AC\n\n',gr_gm_ac,'\n\n','Gross Returns for F_AC\n\n',gr_f_ac,'\n')

correlation_gr=np.corrcoef(gr_gm_ac,gr_f_ac)
print ('Correlation Coefficient = ',correlation_gr[0][1],'\n')

print('Refer to plot Gross Returns\n')
    
fig = plt.figure(figsize=(8,4),dpi=200)
bx = fig.add_subplot(111)
bx.set_title('Plot of Gross Returns')
bx.scatter(gr_gm_ac,gr_f_ac, color='blue', s=0.05) ;
plt.show()

#Part 2
print('__________________________________________________\n\nPart 2\n__________________________________________________\n')

gm_ac = dat['GM_AC']   
f_ac = dat ['F_AC']

n= gm_ac.size

logr_gm_ac=np.zeros(n-1)       # Log Return arrays 
logr_f_ac=np.zeros(n-1)

for i in range (n-1):
    logr_gm_ac[i]=np.log(gm_ac[i+1]/gm_ac[i])
    logr_f_ac[i]=np.log(f_ac[i+1]/f_ac[i])
    
print ('Log Returns for GM_AC\n\n',logr_gm_ac,'\n\n','Log Returns for F_AC\n\n',logr_f_ac,'\n')

correlation_lr=np.corrcoef(logr_gm_ac,logr_f_ac)
print ('Correlation Coefficient = ',correlation_lr[0][1],'\n')

print('Refer to plot Log Returns\n')

fig = plt.figure(figsize=(8,4),dpi=200)
ax = fig.add_subplot(111)
ax.set_title('Plot of Log Returns')
ax.scatter(logr_gm_ac,logr_f_ac, color='red', s=0.05) ;
plt.show()

#Part 3
print('__________________________________________________\n\nPart 3\n__________________________________________________\n')

print('Refer to plot Comparison\n')

fig = plt.figure(figsize=(8,4),dpi=200)
cx = fig.add_subplot(111)
cx.set_title('Comparison')
cx.scatter(gr_gm_ac,gr_f_ac, color='blue', s=0.05) ;
cx.scatter(logr_gm_ac,logr_f_ac, color='red', s=0.05) ;
cx.legend('GL')
plt.show()