import numpy as np
from scipy import stats
from sklearn import preprocessing


mid_score = np.array([])
final_score = np.array([])


def load_data(url):
    for line in open(url):
        global mid_score, final_score
        mid_score = np.append(mid_score, int(line.split()[1]))
        final_score = np.append(final_score, int(line.split()[2]))


load_data("./data/data.online.scores.txt")

# question 1-a
print "------ question 1-a ------"

print "min mid-term score:",
print np.min(mid_score)
print "max mid-term score:",
print np.max(mid_score)


# question 1-b
print "------ question 1-b ------"


print "Q1 of mid-term score:",
print np.percentile(mid_score, 25)
print "median of mid-term score:",
print np.percentile(mid_score, 50)
print "Q3 of mid-term score:",
print np.percentile(mid_score, 75)


# question 1-c
print "------ question 1-c ------"


print "mean of mid-term score:",
print round(np.mean(mid_score), 3)


# question 1-d
print "------ question 1-d ------"


print "mode of mid-term score:"

count = {}

for score in mid_score:
    if count.has_key(score):
        count[score] += 1
    else:
        count[score] = 1

max = sorted(count.values())[len(count) - 1]

for score in count:
    if count[score] == max:
        print score


# question 1-e
print "------ question 1-e ------"


print "experience variance of mid-term score:",
print round(np.var(mid_score, ddof = 1), 3)


mid_score_z = preprocessing.scale(mid_score)

# question 2-a
print "------ question 2-a ------"


print "experience variance of mid-term score:",
print round(np.var(mid_score, ddof = 1), 3)
print "experience variance of z-score normalized mid-term score:",
print np.var(mid_score_z)


# question 2-b
print "------ question 2-b ------"


print "z-score normalized of 90:",
print round((90 - np.mean(mid_score)) / np.std(mid_score, ddof = 1), 3)


# question 2-c
print "------ question 2-c ------"


print "correlation coefficient between midterm scores and final scores:",
print round(np.corrcoef(mid_score, final_score)[1][0], 3)


# question 2-d
print "------ question 2-d ------"


print "Covariance between midterm scores and final scores",
print round(np.cov(mid_score, final_score)[1][0], 3)





