import pandas as pd
import numpy as np
import os

path = os.getcwd()

eco_file = path + "/data/ECOS_TABLE_20210118_154159.xlsx"
corona_file = path +"/data/101_DT_COVID19_005_D_20210118235058.xlsx"

#2020년4월 1일부터 2021년 1월15일 data
pd_eco = pd.read_excel(eco_file, engine='openpyxl')
dates = np.array(pd_eco.columns[66:])
df_kospi = pd.DataFrame(data=dates, columns=['Date'])
kospi_value = np.array(pd_eco.loc[0])
kospi_value = kospi_value[66:]

df_kospi['Kospi'] = kospi_value

pd_corona = pd.read_excel(corona_file, engine='openpyxl')
corona_dates = np.array(pd_corona.iloc[0])[4:]
corona_date = []
for each in corona_dates:
    string = each.replace(". ", "/")
    corona_date.append(string)

df_corona = pd.DataFrame(data=corona_date, columns=['Date'])
corona_value = np.array(pd_corona.iloc[3])
corona_value = corona_value[4:]
df_corona['Coronic'] = corona_value

df = pd.merge(df_corona, df_kospi, left_on='Date', right_on='Date', how='outer')

df.to_excel(path+"/data/kospi_corona.xlsx", index=False, engine='openpyxl')

df = pd.read_excel(path+"/data/kospi_corona.xlsx", engine='openpyxl')

d = df.dropna()

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

Date_list = df['Date'].tolist()
X_pos = np.arange(len(Date_list))
Coronic_Value = df['Coronic'].tolist()
Kospi_Value = df['Kospi'].tolist()

plt.figure(figsize=(13, 9))

plt_Corona = plt.subplot(2,2,1)
plt_Corona.bar(Date_list, Coronic_Value, align='center', color='r')
plt_Corona.tick_params(axis='x', rotation=90)
plt_Corona.set_title('coronic')
plt_Corona.set_ylabel('coronic data')
plt_Corona.xaxis.set_major_locator(ticker.AutoLocator())

plt_Kospi = plt.subplot(2,2,2)
plt_Kospi.tick_params(axis='x', rotation=90)
plt_Kospi.bar(Date_list, Kospi_Value, align='center', color='b')
plt_Kospi.set_title('Kospi')
plt_Kospi.set_ylabel('Kospi value')
plt_Kospi.set_ylim(1500,3500)
plt_Kospi.xaxis.set_major_locator(ticker.AutoLocator())
# plt_Kospi.set_xticklabels(Date_list, rotation=90)



plt_df1 = plt.subplot(2,2,3)
plt_df1.tick_params(axis='x', rotation=90)
plt_df2 = plt_df1.twinx()
plt_df1.bar(Date_list, Coronic_Value, align='center', color='r', label='coronic')
plt_df2.bar(Date_list, Kospi_Value, align='center', color='b', label='kospi')
plt_df2.set_ylim(1500,3500)
plt_df1.legend(loc='upper left')
plt_df2.legend(loc='upper right')
plt_df1.xaxis.set_major_locator(ticker.AutoLocator())

plt.subplots_adjust(wspace=0.5, hspace=0.5)
plt.show()

