import numpy as np

class CouponBond:

    def __init__(self, maturityTime=10, couponRate =0.06, faceValue = 1000, couponPayment =0.):
        self.par = faceValue
        self.r = couponRate
        self.T = maturityTime
        self.couponPayment = couponPayment

    def ZCB_Annual(self):
        return self.par/(1+self.r)**self.T

    def ZCB_SemiAnnual(self):
        return self.par/(1+0.5*self.r)**(2*self.T)

    def ZCB_ContinousCompound(self):
        return self.par/np.exp(self.r*self.T)