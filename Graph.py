import pandas as pd
import numpy as np
import xlsxwriter

# eco_file =  "D:\SYun\BigData\Corona\ECOS_TABLE_20210118_154159.xlsx"
# corona_file = "D:/SYun/BigData/Corona/101_DT_COVID19_005_D_20210118235058.xlsx"
# pd_economic = pd.DataFrame()
#
# #4월 1일부터 1월15일
# ex_eco = pd.read_excel(eco_file, engine='openpyxl')
# dates = np.array(ex_eco.columns[66:])
# df_kospi = pd.DataFrame(data=dates, columns=['Date'])
# kospi_value = np.array(ex_eco.loc[0])
# kospi_value = kospi_value[66:]
#
# df_kospi['Kospi'] = kospi_value
#
# ex_corona = pd.read_excel(corona_file, engine='openpyxl')
# corona_dates = np.array(ex_corona.iloc[0])[4:]
# corona_date = []
# for each in corona_dates:
#     string = each.replace(". ", "/")
#     corona_date.append(string)
#
# df_corona = pd.DataFrame(data=corona_date, columns=['Date'])
# corona_value = np.array(ex_corona.iloc[3])
# corona_value = corona_value[4:]
# df_corona['Coronic'] = corona_value
#
# df = pd.merge(df_corona, df_kospi, left_on='Date', right_on='Date', how='outer')
#
# df.to_excel('D:\SYun\BigData\Corona\kospi_corona.xlsx', index=False, engine='openpyxl')

df = pd.read_excel("D:\SYun\BigData\Corona\kospi_corona.xlsx", engine='openpyxl')

d = df.dropna()

import matplotlib.pyplot as plt

Date_list = df.index.tolist()
X_pos = np.arange(len(Date_list))
Coronic_Value = df['Coronic'].tolist()
Kospi_Value = df['Kospi'].tolist()

plt.figure(figsize=(12, 3))
plt_Corona = plt.subplot(1,2,1)
plt_Corona.bar(X_pos, Coronic_Value, align='center')
plt.ylabel('coronic')
plt.title('coronic data')
plt_Kospi = plt.subplot(1,2,2)
plt_Kospi.bar(X_pos, Kospi_Value, align='center')
plt.xlim()



plt.subplots_adjust(wspace=0.5)

plt.show()



