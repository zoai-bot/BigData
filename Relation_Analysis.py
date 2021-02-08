import pandas as pd
import os
from konlpy.tag import Okt
from apyori import apriori
import time
import datetime
from collections import Counter
import numpy as np

# start = time.time()
# seconds = time.time()-start
# end = datetime.timedelta(seconds=seconds)


path = os.getcwd()

kor_df = pd.read_excel(path + "\data\clean_kor.xlsx", engine="openpyxl")

with open(path + "/data/korean_stopwords.txt", encoding='utf8') as file:
    kor_stopword = file.readlines()
    kor_stopwords = [x.strip() for x in kor_stopword]
    file.close()

def filter_kor_noun(content):
    tagger = Okt()
    nouns = tagger.nouns(content)
    noun = [noun for noun in nouns if noun not in kor_stopwords]

    return noun

support_df = kor_df['kor_content'].apply(lambda x: filter_kor_noun(x))
transactions = support_df.tolist()

results = list(apriori(transactions,
              min_support=(0.05),
              min_confidence=0.05,
              min_lift=1.1,
              max_length=2)
              )
#한 데이터세트 즉 하나의 행에 해당 단어가 포함되는 확율 = keywords/all rows
print(results)
network_df = pd.DataFrame(columns=['source','target','support'])

for result in results:
    items = [x for x in result.items]
    row = [items[0], items[1], result.support]
    series = pd.Series(row, index=network_df.columns)
    network_df = network_df.append(series, ignore_index=True)

print(network_df)
network_df.to_excel(path + "/data/network_df.xlsx", engine="openpyxl", index=False)

corpus = "".join(kor_df['kor_content'])
filtered_kor = filter_kor_noun(corpus)
node_count = Counter(filtered_kor)

node_df = pd.DataFrame(node_count.items(), columns=['node','nodesize'])

node_df = node_df[node_df['nodesize']>=50]
print(node_df.shape)
node_df.to_excel(path+"/data/node_df.xlsx", engine="openpyxl", index=False)

import networkx as nx
import matplotlib.pyplot as plt

plt.figure(figsize=(25,25))

graph = nx.Graph()

for index, row in node_df.iterrows():
    graph.add_node(row['node'], nodesize=row['nodesize'])

print("node: {}".format( [graph.nodes[node]['nodesize'] for node in graph] ) )

for index, row in network_df.iterrows():
    graph.add_weighted_edges_from([(row['source'], row['target'], row ['support'])])

print("weight: {}".format( [graph.nodes[node] for node in graph] ) )

pos = nx.spring_layout(graph, k=0.6, iterations=50)
sizes = [graph.nodes[node]['nodesize']*25 for node in graph]
nx.draw(graph, pos=pos, node_size=sizes)

nx.draw_networkx_labels(graph, pos=pos, font_family='gulim', font_size=25)

ax = plt.gca()
print(ax)
if network_df is not None:
    plt.show()











