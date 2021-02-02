import pandas as pd
import os
from konlpy.tag import Okt
from collections import Counter
import re
import nltk
from nltk.corpus import stopwords
import pickle


path = os.getcwd()

df = pd.read_excel(path + "\crawling_Corona.xlsx", engine="openpyxl")
content_text = ''.join(df['content'].tolist())


with open(path + "\eng_stopwords.txt", 'w') as file:
    eng_stopwords = stopwords.words('english')
    file.write(",".join(eng_stopwords))
file.close()


def filter_eng(content):
    words = []
    eng = re.compile('[^a-zA-Z]+')
    gener = eng.sub(' ',content)
    no_capital = gener.lower()

    word_tokens = nltk.word_tokenize(no_capital)
    tokens_pos = nltk.pos_tag(word_tokens)

    stop_taggs = ['NN','NNP','FW']

    nouns = [noun for noun, pos in tokens_pos if pos in stop_taggs]
    words = [words for words in nouns if len(words) > 1]

    eng_stopwords = path + "\eng_stopwords.txt"
    # with open(korean_stopwords, encoding='utf8') as file:
    #     stopwords = file.readlines()
    # stopwords = [x.strip() for x in stopwords]
    print(nouns)


    # eng_stopwords = set(stopwords.words('english'))
    # no_stopwords = [word for word in eng_list if not word in eng_stopwords]

    pass


# word_tokens = nltk.word_tokenize(content_text)


aa = filter_eng(content_text)