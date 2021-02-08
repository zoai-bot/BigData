import pandas as pd
import os
from konlpy.tag import Okt
import re

path = os.getcwd()

df = pd.read_excel(path + "/data/crawling_Corona.xlsx", engine="openpyxl")

def filter_kor(content):
    korean = re.compile(r'[^ㄱ-ㅎ가-힣]')
    sub_content = korean.sub(" ", content)
    return sub_content


df['kor_content'] = df['content'].apply(lambda x: filter_kor(x))

df['kor_content'].to_excel(path + "/data/clean_kor.json", engine="openpyxl", index=False)
print(df.head())
# index 행과, 단어의 개수 = 트렌젝션 수를 반환
