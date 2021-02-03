import pandas as pd
import os
from konlpy.tag import Okt
from collections import Counter
import re

path = os.getcwd()

df = pd.read_excel(path + "\crawling_Corona.xlsx", engine="openpyxl")

korean_stopwords = path + "\korean_stopwords.txt"

'''
with open(korean_stopwords, encoding='utf8') as file:
    stopwords = file.readlines()
    stopwords = [x.strip() for x in stopwords]
    file.close()

with open(path + "\korean_stopwords2.txt", mode='w') as file:
    file.write(', '.join(stopwords))
    file.close()
'''

with open(path + "\korean_stopwords2.txt", mode='r') as file:
    kor_stopwords = file.readline().split(', ')

def filter_kor(content):
    korean = re.compile(r'[^ㄱ-ㅎ가-힣]')
    sub_content = korean.sub(" ", content)
    nouns = Okt().nouns(sub_content)

    noun = [noun for noun in nouns if noun not in kor_stopwords]

    return noun


df['kor_nouns'] = df['content'].apply(lambda x: filter_kor(x))

df.to_excel(path + "\clean_data.xlsx", engine="openpyxl")





