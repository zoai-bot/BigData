import pandas as pd
import os
from konlpy.tag import Okt
from collections import Counter
import re


path = os.getcwd()

df = pd.read_excel(path + "\data\crawling_Corona.xlsx", engine="openpyxl")

with open(path + "\data\korean_stopwords.txt", encoding='utf8') as file:
    kor_stopword = file.readlines()
    kor_stopwords = [x.strip() for x in kor_stopword]
    file.close()

def filter_kor(content):
    korean = re.compile(r'[^ㄱ-ㅎ가-힣]')
    sub_content = korean.sub(" ", content)
    for noun in sub_content:
        if noun not in kor_stopwords:
            bound = noun + noun
            

    return bound

df['kor_nouns'] = df['content'].apply(lambda x: filter_kor(x))
print(df['kor_nouns'])

#
# def filter_kor(content):
#     nouns = Okt().nouns(sub_content)
#
#     noun = [noun for noun in nouns if noun not in kor_stopwords]
#
#     return noun
#
# df['kor_nouns'] = df['content'].apply(lambda x: filter_kor(x))
#
# joining = ' '.join(df['content'])
# noun = filter_kor(joining)
#
# df['kor_nouns'].to_excel(path + "\data\clean_kor.xlsx", engine="openpyxl", index=False)
# print(df['kor_nouns'].shape)
# print(df['kor_nouns'][2][1])
# #index행과, 단어의 개수 = 트렌젝션 수를 반환
#
#
#
