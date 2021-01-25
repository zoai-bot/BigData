import pandas as pd
import os

path = os.getcwd()
file_name = "\crawling_Corona.xlsx"
file_directory = path + file_name

df = pd.read_excel(file_directory, engine='openpyxl')

tags_total = []
for tags in df['tags']:
    tags_list = tags[2:-2].split("', '")
    for tag in tags_list:
        tags_total.append(tag)

from collections import Counter

stopwords = ['', '#맞팔', '#좋아요', '#일상', '#선팔', '#좋반', '#소통', '#좋아요반사', '#follow', '#데일리',
             '#instagoo', '#팔로우', '#선팔하면맞팔', '#선팔맞팔', '#인친', '#첫줄', '#팔로우늘리기', '#일상스타그램', '#얼스타그램',
             '#팔로워', '#셀피', '#첫줄반사', '#협찬', '#selfie', '#맛스타그램', '#좋아요테러', '#좋테', '#팔로워판매', '#좋아요판매',
             '#팔로워구매', '#소개계정맞팔', '#셀스타그램']

tag_selection = []
for tag in tags_total:
    if tag not in stopwords:
        tag_selection.append(tag)

tag_counts = Counter(tag_selection)

import matplotlib.pyplot as plt
from wordcloud import WordCloud
import platform

if platform.system() == 'Windows':
    font_path = "c:/Windows/Fonts/gulim.ttc"
elif platform.system() == "Darwin":   #Mac 의 경우
    font_path = "/Users/$USER/Library/Fonts/AppleGothic.ttf"

wordcloud = WordCloud(font_path= font_path,
                    background_color="white",
                    max_words=100,
                    relative_scaling= 0.2,
                    width = 1000,
                    height = 600)
wordcloud.generate_from_frequencies(tag_counts)
plt.figure(figsize=(15,8))

# plt_word = plt.subplot(1,2,1)
# plt_word.imshow(wordcloud)
# plt_word.axis('off')
# plt.savefig(path+"\hashtag_wordcloud")
# plt.show()
tag_common = tag_counts.most_common(10)

print(tag_common)














