import pandas as pd
import os
from konlpy.tag import Okt
import re

path = os.getcwd()

df = pd.read_excel(path + "/data/crawling_Corona.xlsx", engine="openpyxl")

with open(path + "/data/korean_stopwords.txt", encoding='utf8') as file:
    kor_stopword = file.readlines()
    kor_stopwords = [x.strip() for x in kor_stopword]
    file.close()


def filter_kor(content):
    korean = re.compile(r'[^ㄱ-ㅎ가-힣]')
    sub_content = korean.sub(" ", content)
    return sub_content


df['kor_content'] = df['content'].apply(lambda x: filter_kor(x))


def filter_kor_noun(content):
    tagger = Okt()
    nouns = tagger.nouns(content)
    noun = [noun for noun in nouns if noun not in kor_stopwords]

    return noun


df['kor_nouns'] = df['kor_content'].apply(lambda x: filter_kor_noun(x))

df[['kor_content', 'kor_nouns']].to_excel(path + "/data/clean_kor.xlsx", engine="openpyxl", index=False)
print(df.head())
print(df['kor_nouns'].shape)
# index 행과, 단어의 개수 = 트렌젝션 수를 반환
