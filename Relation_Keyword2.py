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

print(df['content'])

# add_stopwords = ", ootd, http, co, kr, dm, fallow, fallowforfollow, instalike, www, https, xl, selfie, followforfollowback, com, lol, instagood, facebook, "

# with open(path + "\eng_stopwords.txt", 'wt') as file:
#     eng_stopwords = ', '.join(stopwords.words('english'))
#     file.write(eng_stopwords)
#     file.write(add_stopwords)
#     file.close()


with open(path+ "\eng_stopwords.txt", "rt") as file:
    eng_stopwords = file.readline().split(', ')
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
    no_stopwords = [word for word in words if word not in eng_stopwords]

    return no_stopwords


# word_tokens = nltk.word_tokenize(content_text)


# aa = filter_eng(content_text)
