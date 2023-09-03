#Fahad Hassan 2020-10-0149
#Assignment 2 Econometrics

#Question 1a
head(hprice)
tail(hprice)
colMeans(hprice)

#Question 1b
lotsize = hprice$lotsize
price = hprice$price
bdrms = hprice$bdrms
par(mar = c(4,4,4,4))
plot(lotsize, price, xlab = "size of lot in square feet", ylab = "house price in $1000s", main = "Lot Size vs Price")

#Question 2a
model1 = lm(price ~ lotsize + bdrms)
summary(model1)
anova(model1)

#Intercept interpretation: No meaningful interpretation (is not significant)
#lotsize interpretation: For one square feet increase in the lot size, the price of the house increases by $2.858,  keeping all other variables constant
#bdrms interpretation: For one unit increase in bedrooms, the price increases by $5.731e04 by keeping all other variables constant

#Question 2b
confint(model1, level = 0.95)

#Question 2c
model2 = lm(log(price) ~ log(lotsize) + bdrms)
summary(model2)
anova(model2)

#Intercept interpretation: No meaningful interpretation (is not significant)
#lotsize interpretation: For 10% increase in lot size, the price of the house increases by $(1.1)^0.24449 by keeping all other variables constant
#bdrms  interpretation: For one unit increase in bedrooms, the price increases by 14.043% by keeping all other variables constant

#Question 2d
model3 = lm(price ~ lotsize + bdrms + I(bdrms^2))
summary(model3)
anova(model3)

#Intercept interpretatio: No meaningful interpretation (is not significant)
#lotsize Interpreataion: For one square feet increase in the lot size, the price of the house increases by $2.862 by keeping all other variables constant
#bdrms Interpreataion: For one unit increase in bedrooms, the price decreases by $1.092e04 by keeping all other variables constant
#bdrms^2 Interpreataion: For square increase in the number of bedrooms (non-linear), the price decreases by $8.5e03 by keeping all other variables constant

#Question 3a
install.packages("pkgconfig")
linearHypothesis(model2, c("log(lotsize)=1"))

#The P value is too less => Reject null hypothesis.
#P-value = 2.23e-16 and F-value =  252.81.
#Therefore, B1 must not be equal to 1.

#Question 3b
linearHypothesis(model3, c("bdrms","I(bdrms^2)"))
linearHypothesis(model3, c("bdrms-I(bdrms^2)"))

#The P value is too less => Reject null hypothesis.
#P-value = 3.493e-06 and F value =  14.646.
#Therefore, B2 and B3 must not be equal to 0.

save.image("20100149_Econo_A2.Rdata")
