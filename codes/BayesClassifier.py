import numpy as np
from numpy import genfromtxt
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn import metrics
from joblib import dump, load

data1 = np.array(genfromtxt('FeaturedData/WallFeatures.csv',delimiter=','))
data2 = np.array(genfromtxt('FeaturedData/HumanFeatures.csv',delimiter=','))
data3 = np.array(genfromtxt('FeaturedData/CarFeatures.csv',delimiter=','))

x = np.concatenate((data1,data2,data3))

label1 = np.repeat(-1,data1.shape[0])
label2 = np.repeat(0,data2.shape[0])
label3 = np.repeat(1,data3.shape[0])

y = np.concatenate((label1,label2,label3))

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

clf = GaussianNB()
clf.fit(x_train, y_train)
dump(clf,'BayesClassifierModel.joblib') 

clf_loaded = load('BayesClassifierModel.joblib') 
y_pred = clf_loaded.predict(x_test)

print("Accuracy:",metrics.accuracy_score(y_test, y_pred))