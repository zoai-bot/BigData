import pandas as pd
import os
from apyori import apriori
import time
import datetime

path = os.getcwd()

df = pd.read_excel(path + "\clean_data.xlsx", engine="openpyxl")

transactions = df['kor_nouns'].tolist()

transaction = [transaction for transaction in transactions]

start = time.time()

result = list(apriori(transaction,
              min_support=(300/1000),
              min_confidence=0.2,
              min_lift=5)
              )

print(result)

seconds = time.time()-start
end = datetime.timedelta(seconds=seconds)
print(end)