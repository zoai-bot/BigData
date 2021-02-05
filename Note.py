import pandas as pd
import os
from apyori import apriori
from konlpy.tag import Okt

sample = [['말','사자','판다'],
          ['호랑이,사자'],
          ['곰','사자','판다'],
          ['원숭이','사자','판다','부엉이']]

apriori_cals = list(apriori(sample))

case = []
print(apriori_cals)

for apriori_cal in apriori_cals:
    if len(apriori_cal.items) == 2:
        print("Section: {}".format(apriori_cal.items))


print("============"*5)

from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
import os

path = os.getcwd()
# clean_data = pd.read_excel(path+"/data/clean_data.xlsx", engine="openpyxl")
# kors = clean_data['kor_nouns']


# for kor in kors:
#     repacking = [noun for noun in kor]


# te = TransactionEncoder()
# dataset = te.fit(kor).transform(kor)
# df = pd.DataFrame(data=dataset, columns=te.columns_)
#
# print(kor.shape)
#
#
# data = apriori(df, use_colnames=True, min_support=0.1, max_len=2)
# print(data)

from collections import Counter


print("".join(sample))