import pandas as pd
import os
from apyori import apriori
from konlpy.tag import Okt
from collections import Counter
from konlpy.tag import Okt

samples = [['말', '사자', '판다'],
           ['호랑이', '사자'],
           ['곰', '사자', '판다'],
           ['원숭이', '사자', '판다', '부엉이']]

for sample in samples:
    str_sample = [word for word in sample]

pr = Counter(str_sample)
print(pr)

another_sample = "아버지 가방에 들어가시신다"

tagger = Okt()
nouns = tagger.nouns(another_sample)
print(nouns)


# apriori_cals = list(apriori(sample))
#
# case = []
# print(apriori_cals)
#
# for apriori_cal in apriori_cals:
#     if len(apriori_cal.items) == 2:
#         print("Section: {}".format(apriori_cal.items))
#
#
# from mlxtend.preprocessing import TransactionEncoder
# from mlxtend.frequent_patterns import apriori
# import os
#
# path = os.getcwd()
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



