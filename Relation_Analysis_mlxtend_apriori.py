from mlxtend.frequent_patterns import apriori
from mlxtend.preprocessing import TransactionEncoder
import pandas as pd
from konlpy.tag import Okt
import os

path = os.getcwd()

kor_df = pd.read_excel(path + "\data\clean_kor.xlsx", engine='openpyxl')

tagger = Okt()
kor_df = kor_df['kor_nouns'].apply(lambda x: tagger.nouns(x))
transactions = kor_df.tolist()

te = TransactionEncoder()
dataset = te.fit(transactions).transform(transactions)
df = pd.DataFrame(data=dataset, columns=te.columns_)

print(df.shape)
print(df)

data = apriori(df, use_colnames=True, min_support=0.01, max_len=2)
#한 데이터세트 즉 하나의 행에 해당 단어가 포함되는 확율 = keywords/all columns
print(data.itemsets[1])

