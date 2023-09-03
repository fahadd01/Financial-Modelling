''' Fahad Hassan
    2020-10-0149
    Financial Modelling and Analysis: MATH 242
    Assignment 2: Fixed Income Securities
'''

#Importing libraries
import Bond
import numpy as np
from scipy import integrate

#Question 1

My_Bond_1 = Bond.CouponBond(maturityTime=5)

Forward_Rate_1 = lambda t: 0.032 + (0.001 * t) + (0.0002 * t ** 2)
integral = integrate.quad(Forward_Rate_1, 0, 5)
Spot_Rate = integral[0]/5
print('1.1.\n5 year Continuously Compounded Spot rate =',Spot_Rate,'i.e',round(Spot_Rate*100,2),'%\n')

My_Bond_1 = Bond.CouponBond(maturityTime=5, couponRate = Spot_Rate)
Price_1 = My_Bond_1.ZCB_ContinousCompound()
print('1.2.\nPrice of zero-coupon bond maturing in 5 years = $',round(Price_1,2),'\n')

#Question 2

YT_at0 = lambda t: 0.04 + 0.001 * t
My_Bond_2a = Bond.CouponBond(couponRate = YT_at0(10))
Price_2a = My_Bond_2a.ZCB_ContinousCompound()
print('2.1.\nPrice of a par = $1000, zero-coupon bond with a maturity of 10 years = $',round(Price_2a,2),'\n')

YT_at1 = lambda t: 0.042 + 0.001 * t
My_Bond_2b = Bond.CouponBond(maturityTime = 9, couponRate = YT_at1(9))
Price_2b = My_Bond_2b.ZCB_ContinousCompound()
Net_Return = (Price_2b-Price_2a)/Price_2a
print('2.2.\nNet return on the bond as such = ',Net_Return,'i.e', round(Net_Return*100,2),'%\n')

#Question 4

Forward_Rate_4 = lambda t: 0.022 + 0.005 * t - 0.004 * ( t ** 2 ) + 0.0003 * ( t ** 3 )
T = np.zeros(8)
C = 21
Par = 1000
r = np.zeros(8)
Price_4 = np.zeros(8)

for i in range (8):
    T[i] = 0.5 + 0.5 * i
    integral = integrate.quad(Forward_Rate_4, 0 , T[i])
    r[i] = (integral[0]/T[i])
    
for i in range (7):
    Price_4[i] = C/np.exp(r[i]*T[i])
    
Price_4[7] = (Par+C)/np.exp(r[7]*T[7])

Bond_Price = sum(Price_4)
print('4.\nPrice of the bond as such = $',round(Bond_Price,2),'\n')

#Question 5

Par = 1000
T = [1, 2, 3, 4, 5]
Spot_Rates = [0.031, 0.035, 0.04, 0.042, 0.043]
DiscountedPrice_1 = np.zeros(5)

for i in range (5):
    r = Spot_Rates[i]
    m_t = T[i]
    My_Bond_5_1 = Bond.CouponBond(maturityTime = m_t, couponRate = r)
    DiscountedPrice_1[i] = My_Bond_5_1.ZCB_SemiAnnual()
    
print('5.1.\nCurrent price of 1-year zero-coupon bonds with par values of $1, 000 = $',round(DiscountedPrice_1[0],2))
print('Current price of 3-year zero-coupon bonds with par values of $1, 000 = $',round(DiscountedPrice_1[2],2))
print('Current price of 5-year zero-coupon bonds with par values of $1, 000 = $',round(DiscountedPrice_1[4],2),'\n')

DiscountedPrice_2 = np.zeros(5)

for i in range (5):
    r = Spot_Rates[i-1]
    m_t = T[i]-1
    My_Bond_5_2 = Bond.CouponBond(maturityTime = m_t, couponRate = r)
    DiscountedPrice_2[i] = My_Bond_5_2.ZCB_SemiAnnual()

print('5.2.\n1 year from now price of 1-year zero-coupon bonds with par values of $1, 000 (With same Spot Rates) = $',round(DiscountedPrice_2[0],2))
print('1 year from now price of 3-year zero-coupon bonds with par values of $1, 000 (With same Spot Rates) = $',round(DiscountedPrice_2[2],2))
print('1 year from now price of 5-year zero-coupon bonds with par values of $1, 000 (With same Spot Rates) = $',round(DiscountedPrice_2[4],2),'\n')

Spot_Rates_inc = np.zeros(5)

for i in range(5):
    Spot_Rates_inc[i] = Spot_Rates[i] + 0.005

DiscountedPrice_3 = np.zeros(5)

for i in range (5):
    r = Spot_Rates_inc[i-1]
    m_t = T[i]-1
    My_Bond_5_3 = Bond.CouponBond(maturityTime = m_t, couponRate = r)
    DiscountedPrice_3[i] = My_Bond_5_3.ZCB_SemiAnnual()

print('5.3.\n1 year from now price of 1-year zero-coupon bonds with par values of $1, 000 (With incremented Spot Rates) = $',round(DiscountedPrice_3[0],2))
print('1 year from now price of 3-year zero-coupon bonds with par values of $1, 000 (With incremented Spot Rates) = $',round(DiscountedPrice_3[2],2))
print('1 year from now price of 5-year zero-coupon bonds with par values of $1, 000 (With incremented Spot Rates) = $',round(DiscountedPrice_3[4],2),'\n')

Net_Return_Correct = np.zeros(5)

for i in range (5):
    Net_Return_Correct [i] = (DiscountedPrice_3[i]-DiscountedPrice_1[i])/DiscountedPrice_1[i]

print('5.4.\nIf Spot Rates increase by 0.005\nNet return on 1-year zero-coupon bonds with par values of $1, 000 = ',Net_Return_Correct[0],'i.e.',round((Net_Return_Correct[0]*100),2),'%')
print('Net return on 3-year zero-coupon bonds with par values of $1, 000 = ',Net_Return_Correct[2],'i.e.',round((Net_Return_Correct[2]*100),2),'%')
print('Net return on of 5-year zero-coupon bonds with par values of $1, 000 = ',Net_Return_Correct[4],'i.e.',round((Net_Return_Correct[4]*100),2),'%\n')

Net_Return_InCorrect = np.zeros(5)

for i in range (5):
    Net_Return_InCorrect [i] = (DiscountedPrice_2[i]-DiscountedPrice_1[i])/DiscountedPrice_1[i]

print('5.5.\nIf Spot Rates stay same\nNet return on 1-year zero-coupon bonds with par values of $1, 000 = ',Net_Return_InCorrect[0],'i.e.',round((Net_Return_InCorrect[0]*100),2),'%')
print('Net return on 3-year zero-coupon bonds with par values of $1, 000 = ',Net_Return_InCorrect[2],'i.e.',round((Net_Return_InCorrect[2]*100),2),'%')
print('Net return on of 5-year zero-coupon bonds with par values of $1, 000 = ',Net_Return_InCorrect[4],'i.e.',round((Net_Return_InCorrect[4]*100),2),'%\n')

print('5.6.\nWhen Spot Rates remain same, maximum one year net return = ',max(Net_Return_InCorrect),'occurs against 3 year maturity, Whereas max Current Spot Rate = ',max(Spot_Rates),'is for 5 year maturity\nThis implies that the statement by the analyst is incorrect')