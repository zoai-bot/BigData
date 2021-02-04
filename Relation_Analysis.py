import pandas as pd
import os
from apyori import apriori
import time
import datetime
from collections import Counter
import numpy as np

path = os.getcwd()

clean_df = pd.read_json(path + "\clean_data.json")


transactions = clean_df['kor_nouns'].tolist()

# start = time.time()

results = list(apriori(transactions,
              min_support=(100/2931),
              min_confidence=0.2,
              min_lift=5,
              max_length=2)
              )

# seconds = time.time()-start
# end = datetime.timedelta(seconds=seconds)

network_df = pd.DataFrame(columns=['source','target','support'])

for result in results:
    items = [x for x in result.items]
    row = [items[0], items[1], result.support]
    series = pd.Series(row, index=network_df.columns)
    network_df = network_df.append(series, ignore_index=True)

nouns_list = []

clean2_df = pd.read_excel(path + "\clean_data.xlsx", engine="openpyxl")

for noun in clean_df['kor_nouns']:
    for num in range(len(noun)):
        nouns_list.append(noun[num])

print(Counter(nouns_list))








