import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
USDCAD = pd.read_csv('DAT_MT_USDCAD_M1_201707.csv', index_col=0)
USDCAD_open = np.array(USDCAD['Open'])
USDCAD_high = np.array(USDCAD['High'])
USDCAD_low = np.array(USDCAD['Low'])
USDCAD_close = np.array(USDCAD['Close'])

USDCAD['Date'] = USDCAD.index.values
USDCAD['Datetime'] = USDCAD['Date'] + ' ' + USDCAD['Time']
USDCAD['Datetime'] = pd.to_datetime(USDCAD['Datetime'])
USDCAD = USDCAD.drop(USDCAD.columns[[0, 5, 6]], axis=1)



CADJPY = pd.read_csv('DAT_MT_CADJPY_M1_201707.csv', index_col=0)
CADJPY_open = np.array(CADJPY['Open'])
CADJPY_high = np.array(CADJPY['High'])
CADJPY_low = np.array(CADJPY['Low'])
CADJPY_close = np.array(CADJPY['Close'])

CADJPY['Date'] = CADJPY.index.values
CADJPY['Datetime'] = CADJPY['Date'] + ' ' + CADJPY['Time']
CADJPY['Datetime'] = pd.to_datetime(CADJPY['Datetime'])
CADJPY = CADJPY.drop(CADJPY.columns[[0, 5, 6]], axis=1)



EURUSD = pd.read_csv('DAT_MT_EURUSD_M1_201707.csv', index_col=0)
EURUSD_open = np.array(EURUSD['Open'])
EURUSD_high = np.array(EURUSD['High'])
EURUSD_low = np.array(EURUSD['Low'])
EURUSD_close = np.array(EURUSD['Close'])

EURUSD['Date'] = EURUSD.index.values
EURUSD['Datetime'] = EURUSD['Date'] + ' ' + EURUSD['Time']
EURUSD['Datetime'] = pd.to_datetime(EURUSD['Datetime'])
EURUSD = EURUSD.drop(EURUSD.columns[[0, 5, 6]], axis=1)




EURJPY = pd.read_csv('DAT_MT_EURJPY_M1_201707.csv', index_col=0)
EURJPY_open = np.array(EURJPY['Open'])
EURJPY_high = np.array(EURJPY['High'])
EURJPY_low = np.array(EURJPY['Low'])
EURJPY_close = np.array(EURJPY['Close'])

EURJPY['Date'] = EURJPY.index.values
EURJPY['Datetime'] = EURJPY['Date'] + ' ' + EURJPY['Time']
EURJPY['Datetime'] = pd.to_datetime(EURJPY['Datetime'])
EURJPY = EURJPY.drop(EURJPY.columns[[0, 5, 6]], axis=1)


datetime1 = USDCAD['Datetime']
datetime2 = CADJPY['Datetime']
datetime3 = EURUSD['Datetime']
datetime4 = EURJPY['Datetime']

common_dt = pd.Series(list(set(datetime1).intersection(set(datetime2), set(datetime3), set(datetime4)))).order().tolist()

USDCAD = USDCAD[USDCAD['Datetime'].isin(common_dt)]
CADJPY = CADJPY[CADJPY['Datetime'].isin(common_dt)]
EURUSD = EURUSD[EURUSD['Datetime'].isin(common_dt)]
EURJPY = EURJPY[EURJPY['Datetime'].isin(common_dt)]

'USD/CAD * CAD/JPY * JPY/EUR * EUR/USD'

non_arb = np.array(USDCAD['Close'])*np.array(CADJPY['Close'])*np.array(EURUSD['Close'])/np.array(EURJPY['Close'])

plt.plot(non_arb)
plt.show()
