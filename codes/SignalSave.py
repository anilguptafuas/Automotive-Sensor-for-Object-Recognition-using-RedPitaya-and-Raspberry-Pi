import redpitaya_scpi as scpi
import matplotlib.pyplot as plt
import numpy as np
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
    plt.plot(measRes)
    plt.show()
    signal = np.array([measRes])
    f = open("Wall.csv", "a")
    np.savetxt(f,signal,fmt='%3.8f',delimiter=',')
    f.close()
    time.sleep(3)
    plt.close()




