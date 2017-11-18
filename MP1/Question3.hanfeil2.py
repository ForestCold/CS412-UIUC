import numpy as np
from scipy import stats
from sklearn import preprocessing


CML = np.array([])
CBL = np.array([])


def load_data(url):
    for line in open(url):
        global CML, CBL
        if line.split()[0] == "CML":
            for book in line.split():
                if book != "CML":
                    CML = np.append(CML,int(book))
            continue
        if line.split()[0] == "CBL":
            for book in line.split():
                if book != "CBL":
                    CBL = np.append(CBL,int(book))

load_data("./data/data.libraries.inventories.txt")


# question 3-a
print "------ question 3-a ------"

print "Jaccard coefficient between CML and CBL:",
print round(float(58) / float(2 + 120 + 58), 3)


# question 3-b
print "------ question 3-b ------"

print "When h = 1, the minkowski distance is:",
print np.sum(np.fabs(CBL - CML))
print "When h = 2, the minkowski distance is:",
print round(np.sqrt(np.sum((CBL - CML)**2)), 3)
print "When h = plus infinity, the minkowski distance is:",
print np.max(np.fabs(CBL - CML))


# question 3-c
print "------ question 3-c ------"

print "the cosine similarity between CML and CBL:",
print round(np.sum(CML * CBL) / (np.linalg.norm(CBL) * np.linalg.norm(CML)), 3)


# question 3-d
print "------ question 3-d ------"

print "the Kullbac-Leibler divergence between CML and CBL:",
print round(np.sum((CML / np.sum(CML)) * np.log((CML / np.sum(CML)) / (CBL / np.sum(CBL)))), 3)
