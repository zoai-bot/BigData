import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np


df = pd.read_excel("D:\SYun\BigData\Corona\kospi_corona.xlsx", engine='openpyxl')
df = df.dropna()

x_pos = np.arange(len(df['Date']))
plt.figure(figsize=(15, 7))
plt_Coronic = plt.subplot(1,2,1)
plt_Kospi = plt_Coronic.twinx()

plt_Kospi.plot(df['Date'], df['Kospi'], color='b', marker='^', label='kospi')
plt_Coronic.plot(df['Date'], df['Coronic'], color='r', marker='*', linewidth=2, label='coronic')
plt_Coronic.xaxis.set_major_locator(ticker.AutoLocator())
plt_Coronic.tick_params(axis='x', which='major', rotation=45)
# plt_Coronic.set_xticklabels(df['Date'], rotation=90, minor=False)
plt_Coronic.legend(loc='upper left')
plt_Kospi.legend(loc='upper right')

plt_corr = plt.subplot(1,2,2)
plt_corr.scatter(x=df['Coronic'], y=df['Kospi'], color='black')
plt_corr.set_ylabel('Kospi')
plt_corr.set_xlabel('Coronic')

plt.subplots_adjust(wspace=0.5)
plt.show()

