import pandas as pd
import os
from konlpy.tag import Okt
from collections import Counter
import re
import nltk
from nltk.corpus import stopwords

path = os.getcwd()

df = pd.read_excel(path + "\crawling_Corona.xlsx", engine="openpyxl")

content_text = "".join(df['content'].tolist())

korean_stopwords = path + "\korean_stopwords.txt"
with open(korean_stopwords, encoding='utf8') as file:
    stopwords = file.readlines()
stopwords = [x.strip() for x in stopwords]

def clean_text(content):
    gen_spword = re.compile(r'[#]+|www+|com')
    sub_content = gen_spword.sub(" ", content)
    gen_word = re.compile(r'[a-zA-Z가-힣#]+')
    text = gen_word.findall(sub_content)
    # combine_text = ' '.join(text)

    nouns = [noun for noun in text if noun not in stopwords]

    return nouns

print("-----"*10)

clean_text = clean_text(content_text)
print(clean_text)




# nouns = []
# nouns_tagger = Okt()
# nouns = nouns_tagger.nouns(sample)
# count = Counter(nouns)





