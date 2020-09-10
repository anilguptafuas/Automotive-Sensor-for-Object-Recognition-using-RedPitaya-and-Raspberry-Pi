import numpy as np
from numpy import genfromtxt
import tsfresh

data1 = np.array(genfromtxt('CollectedData/Wall.csv',delimiter=','))
for i in range(data1.shape[0]):
    shortData1 = np.array([data1[i][3500:]])
    feature1 = tsfresh.feature_extraction.feature_calculators.abs_energy(shortData1[0])
    feature2 = tsfresh.feature_extraction.feature_calculators.sum_values(shortData1[0])
    feature3 = tsfresh.feature_extraction.feature_calculators.skewness(shortData1[0])
    features = np.array([[feature1, feature2, feature3]])
    f = open("FeaturedData/WallFeatures.csv", "a")
    np.savetxt(f,features,fmt='%3.8f',delimiter=',')
    f.close()
    
data2 = np.array(genfromtxt('CollectedData/Human.csv',delimiter=','))
for i in range(data2.shape[0]):
    shortData2 = np.array([data2[i][3500:]])
    feature1 = tsfresh.feature_extraction.feature_calculators.abs_energy(shortData2[0])
    feature2 = tsfresh.feature_extraction.feature_calculators.sum_values(shortData2[0])
    feature3 = tsfresh.feature_extraction.feature_calculators.skewness(shortData2[0])
    features = np.array([[feature1, feature2, feature3]])
    f = open("FeaturedData/HumanFeatures.csv", "a")
    np.savetxt(f,features,fmt='%3.8f',delimiter=',')
    f.close()
    
data3 = np.array(genfromtxt('CollectedData/Car.csv',delimiter=','))
for i in range(data3.shape[0]):
    shortData3 = np.array([data3[i][3500:]])
    feature1 = tsfresh.feature_extraction.feature_calculators.abs_energy(shortData3[0])
    feature2 = tsfresh.feature_extraction.feature_calculators.sum_values(shortData3[0])
    feature3 = tsfresh.feature_extraction.feature_calculators.skewness(shortData3[0])
    features = np.array([[feature1, feature2, feature3]])
    f = open("FeaturedData/CarFeatures.csv", "a")
    np.savetxt(f,features,fmt='%3.8f',delimiter=',')
    f.close()