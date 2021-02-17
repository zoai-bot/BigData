import io
import os
import pandas as pd

path = os.getcwd()

aa = pd.read_excel("ECOS_TABLE_20210118_154159.xlsx", engine='openpyxl')

aa.to_csv(path + "/data/ECOS_TABLE_20210118_154159.csv", encoding='utf-8', index=False)

bb = pd.read_excel("101_DT_COVID19_005_D_20210118235058.xlsx", engine='openpyxl')

bb.to_csv(path + "/data/101_DT_COVID19_005_D_20210118235058.csv", encoding='utf-8', index=False)