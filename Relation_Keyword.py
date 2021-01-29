import pandas as pd
import os
from konlpy.tag import Okt
from collections import Counter
import re

path = os.getcwd()

df = pd.read_excel(path + "\crawling_Corona.xlsx", engine="openpyxl")

content_text = "".join(df['content'].tolist())
# print(content_text)
# print("-----"*10)
#
# list = "꾀꼬리가 하나가 가는길을 막는다 나머진 모른다"
# nouns = Okt().nouns(content_text)
# # count = Counter(nouns)
# print(nouns)

def clean_text(content):
    text = re.compile('[a-zA-Zㄱ-ㅎㄱ-힣#]+')
    return text.findall(content)

a = clean_text(content_text)
print(content_text)
print(a)

