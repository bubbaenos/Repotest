import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib.finance import candlestick_ohlc
import matplotlib.dates as mdates
import pandas as pd
import pandas_datareader.data as web

# style.use('ggplot')

###This is setting the date with datetime for the pandas dataframe.
# start = dt.datetime(2000,1,1)
# end = dt.datetime(2016,12,31)

###This is the pandas datareader pulling data from yahoo for the time defined.
# df = web.DataReader('TSLA', 'yahoo', start, end)

# print(df.head())

###This converts the dataframe to csv.
# df.to_csv('tsla.csv')

###This reads the dataframe from csv and assigns the date as the index. Can read SQL, JSON, etc.
df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)

# print(df.head())

###This plots the Adj Close.
# df['Adj Close'].plot()
# plt.show()

###This creates a new column in the dataframe called 100ma.
# df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()
# df.dropna(inplace=True)
# print(df.head())

# ax1.plot(df.index, df['Adj Close'])
# ax1.plot(df.index, df['100ma'])
# ax2.bar(df.index, df['Volume'])

# plt.show()

###This resamples for every 10 day period.
df_ohlc = df['Adj Close'].resample('10D').ohlc()
df_volume = df['Volume'].resample('10D').sum()

df_ohlc.reset_index(inplace=True)

df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)

ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)
ax1.xaxis_date()

candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup='g')
ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0)
plt.show()



