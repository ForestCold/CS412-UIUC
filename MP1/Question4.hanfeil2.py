import numpy as np
from scipy import stats
from sklearn import preprocessing

bear_diaper = 150
bear_nodiaper = 40
nobear_diaper = 15
nobear_nodiaper = 3300

bear = bear_diaper + bear_nodiaper
diaper = bear_diaper + nobear_diaper
nobear = nobear_diaper + nobear_nodiaper
nodiaper = bear_nodiaper + nobear_nodiaper
sum = bear + nobear

b_d = float((bear * diaper)) / float(sum)
b_nd = float((bear * nodiaper)) / float(sum)
nb_d = float((nobear * diaper)) / float(sum)
nb_nd = float((nobear * nodiaper)) / float(sum)

a = np.square(bear_diaper - b_d) / b_d
b = np.square(bear_nodiaper - b_nd) / b_nd
c = np.square(nobear_diaper - nb_d) / nb_d
d = np.square(nobear_nodiaper - nb_nd) / nb_nd

chi = a + b + c + d

# question 4
print "------ question 4 ------"

print "the chi-square correlation:",
print round(chi, 3)