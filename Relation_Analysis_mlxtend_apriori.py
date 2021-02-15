from mlxtend.frequent_patterns import apriori
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import association_rules
import pandas as pd
from konlpy.tag import Okt
import os
from collections import Counter

path = os.getcwd()

# pd.set_option('display.max_columns',8)
kor_df = pd.read_excel(path + "/data/clean_kor.xlsx", engine='openpyxl')


tagger = Okt()
kor_nouns = kor_df['kor_nouns'].apply(lambda x: tagger.nouns(x))
transactions = kor_nouns.tolist()

te = TransactionEncoder()
dataset = te.fit(transactions).transform(transactions)
df = pd.DataFrame(data=dataset, columns=te.columns_)

data = apriori(df, use_colnames=True, min_support=700/10000, max_len=2)
#한 데이터세트 즉 하나의 행에 해당 단어가 포함되는 확율 = keywords/all columns

print(data)

association_data = association_rules(data, metric="confidence", min_threshold=0.1)

print(association_data)

with open(path + "/data/korean_stopwords.txt", encoding='utf8') as file:
    kor_stopword = file.readlines()
    kor_stopwords = [x.strip() for x in kor_stopword]
    file.close()

def filter_kor_noun(content):
    tagger = Okt()
    nouns = tagger.nouns(content)
    noun = [noun for noun in nouns if noun not in kor_stopwords]

    return noun

corpus = "".join(kor_df['kor_content'])
filtered_kor = filter_kor_noun(corpus)
node_count = Counter(filtered_kor)

node_df = pd.DataFrame(node_count.items(), columns=['node','nodesize'])

node_df = node_df[node_df['nodesize']>=80]

#노드 50이상의 값으로 노드(단어) 수 제한
print(node_df['node'].tolist())

import networkx as nx
import matplotlib.pyplot as plt

plt.figure(figsize=(25,25))

graph = nx.Graph()

for index, row in node_df.iterrows():
    graph.add_node(row['node'], nodesize=row['nodesize'])

print("node: {}".format( [graph.nodes[node] for node in graph] ) )
print("node: {}".format( [graph.nodes[node]['nodesize'] for node in graph] ) )

for index, row in association_data.iterrows():
    graph.add_weighted_edges_from([(row['antecedents'], row['consequents'], row ['support'])])

print("weight: {}".format( [graph.nodes[node] for node in graph] ) )
print("node: {}".format( [graph.nodes[node]['nodesize'] for node in graph] ) )

#제한된 노드(단어) 수보다 많은 단어 검출되면 에러

pos = nx.spring_layout(graph, k=0.8, iterations=50)

sizes = [graph.nodes[node]['nodesize']*25 for node in graph]

nx.draw(graph, pos=pos, node_size=sizes)

nx.draw_networkx_labels(graph, pos=pos, font_family='gulim', font_size=25)

ax = plt.gca()
print(ax)
plt.show()