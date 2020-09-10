import redpitaya_scpi as scpi
import numpy as np
import tsfresh
from joblib import load
import time

rp = scpi.scpi('192.168.128.1')
while 1:
    rp.tx_txt('ACQ:DEC 64')
    rp.tx_txt('ACQ:TRIG EXT_PE')
    rp.tx_txt('ACQ:TRIG:DLY 8192')
    rp.tx_txt('ACQ:START')
    while 1:
        rp.tx_txt('ACQ:TRIG:STAT?')
        if rp.rx_txt() == 'TD':
            break
    rp.tx_txt('ACQ:SOUR1:DATA?')
    str = rp.rx_txt()[1:-1]
    measRes = np.fromstring(str,dtype=float,sep=',')
    data = np.array(measRes[3500:])
    feature1 = tsfresh.feature_extraction.feature_calculators.abs_energy(data)
    feature2 = tsfresh.feature_extraction.feature_calculators.sum_values(data)
    feature3 = tsfresh.feature_extraction.feature_calculators.skewness(data)
    features = np.array([[feature1, feature2, feature3]])
    clf_loaded = load('BayesClassifierModel.joblib') 
    class_pred = clf_loaded.predict(features)
    if class_pred == -1:
        rp.tx_txt('DIG:PIN LED1,1')  
        rp.tx_txt('DIG:PIN LED2,0')  
        rp.tx_txt('DIG:PIN LED3,0')   
    elif class_pred == 0:
        rp.tx_txt('DIG:PIN LED1,0')  
        rp.tx_txt('DIG:PIN LED2,1')  
        rp.tx_txt('DIG:PIN LED3,0')
    elif class_pred == 1:
        rp.tx_txt('DIG:PIN LED1,0')  
        rp.tx_txt('DIG:PIN LED2,0')  
        rp.tx_txt('DIG:PIN LED3,1')
    time.sleep(1)
