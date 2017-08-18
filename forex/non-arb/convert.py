import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
data1 = pd.read_csv('IF_curMonth_continuous.csv', index_col=0)

print len(data1)
print len(data1)
data1.columns = ['Code', 'Datetime', 'Open', 'High', 'Low', 'Close', 'TradeVolume', 'TradeAmount', 'TotalVolume']
data1.index.names = ['Exchange']


temp = pd.DatetimeIndex(data1['Datetime'])
data1['Date'] = temp.date
data1['Time'] = temp.time

data1 = data1.set_index('Date')
data1 = data1.drop(['Code'], 1)
data1 = data1[['Time', 'Open', 'High', 'Low', 'Close', 'TradeVolume', 'TotalVolume', 'TradeAmount', 'Datetime']]


data2 = pd.read_csv('IF_nextMonth_continuous.csv', index_col=0)
data2.columns = ['Code', 'Datetime', 'Open', 'High', 'Low', 'Close', 'TradeVolume', 'TradeAmount', 'TotalVolume']

data2.index.names = ['Exchange']
temp = pd.DatetimeIndex(data2['Datetime'])
data2['Date'] = temp.date
data2['Time'] = temp.time

data2 = data2.set_index('Date')
data2 = data2.drop(['Code'], 1)
data2 = data2[['Time', 'Open', 'High', 'Low', 'Close', 'TradeVolume', 'TotalVolume', 'TradeAmount', 'Datetime']]





datetime1 = data1['Datetime']
datetime2 = data2['Datetime']
common_dt = pd.Series(list(set(datetime1).intersection(set(datetime2)))).order().tolist()
#print common_dt

data1 = data1[data1['Datetime'].isin(common_dt)]
data2 = data2[data2['Datetime'].isin(common_dt)]



data1 = data1.drop(['Datetime'], 1)
data2 = data2.drop(['Datetime'], 1)


print len(data1)
print len(data1)
data1.to_csv('IF_curMonth_continuous_filtered.csv')
data2.to_csv('IF_nextMonth_continuous_filtered.csv')
















'''

print len(data1)
print len(data2)
print data1.tail()
print data2.tail()

#plt.plot(data1['Close'].tolist())
#plt.plot(data2['Close'].tolist())
#plt.plot((data2['Close']-data1['Close']).tolist())

#plt.show()



slope, intercept, r_value, p_value, std_err = stats.linregress(data1['Close'], data2['Close'])

spread = np.array((data2['Close'] - slope*data1['Close']))

std = np.std(spread)
mean = np.mean(spread)
print mean, std, slope
zScore_series = (spread - mean)/std
plt.plot(zScore_series)
plt.show()

for ii in range(len(zScore_series)):
    z = zScore_series[ii]
    if z > 2.0:
        print data1.iloc[ii, 1]    

'''
