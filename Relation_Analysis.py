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

kor_df = pd.read_excel(path + "\data\clean_kor.xlsx", engine='openpyxl')

tagger = Okt()
kor_df = kor_df['kor_nouns'].apply(lambda x: tagger.nouns(x))
transactions = kor_df.tolist()

results = list(apriori(transactions,
              min_support=(0.02),
              min_confidence=0.2,
              min_lift=5,
              max_length=2)
              )
#한 데이터세트 즉 하나의 행에 해당 단어가 포함되는 확율 = keywords/all rows

network_df = pd.DataFrame(columns=['source','target','support'])

for result in results:
    items = [x for x in result.items]
    row = [items[0], items[1], result.support]
    series = pd.Series(row, index=network_df.columns)
    network_df = network_df.append(series, ignore_index=True)

print(network_df)

# for noun in clean_df['kor_nouns']:
#     for num in range(len(noun)):
#         nouns_list.append(noun[num])
#
# print("noun length: {}".format(len(nouns_list)) )
#
# count_nouns = Counter(nouns_list)
# print(count_nouns)
#
# node_df = pd.DataFrame(count_nouns.items(), columns=['node','nodesize'])
# node_df = node_df[node_df['nodesize']>=8].sort_values(by=['nodesize'], ascending=False)
#
# import networkx as nx
# import matplotlib.pyplot as plt
#
# plt.figure(figsize=(25,25))
#
# graph = nx.Graph()
#
# for index, row in node_df.iterrows():
#     graph.add_node(row['node'], nodesize=row['nodesize'])
#
# print("print: {}".format( [graph.nodes[node]['nodesize'] for node in graph] ) )
#
# for index, row in network_df.iterrows():
#     graph.add_weighted_edges_from([(row['source'], row['target'], row ['support'])])
#
# print("print2: {}".format( [graph.nodes[node] for node in graph] ) )
#
# pos = nx.spring_layout(graph, k=0.6, iterations=50)
# sizes = [graph.nodes[node]['nodesize']*25 for node in graph]
# nx.draw(graph, pos=pos, node_size=sizes)
#
# nx.draw_networkx_labels(graph, pos=pos, font_family='gulim', font_size=25)
#
# ax = plt.gca()
# print(ax)
# plt.show()










