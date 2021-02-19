import pandas as pd
import os

path = os.getcwd()
file_name = "/data/crawling_Corona.xlsx"
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
from matplotlib import font_manager, rc

if platform.system() == 'Windows':
    font_path = "c:/Windows/Fonts/gulim.ttc"
elif platform.system() == "Darwin":   #Mac 의 경우
    font_path = "c:/Users/$USER/Library/Fonts/AppleGothic.ttf"

font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

wordcloud = WordCloud(font_path=font_path,
                    background_color="white",
                    max_words=100,
                    relative_scaling= 0.2,
                    width = 1500,
                    height = 1000)
wordcloud.generate_from_frequencies(tag_counts)
plt.figure(figsize=(10, 5))

plt_word = plt.subplot(1, 2, 1)
plt_word.imshow(wordcloud)
plt_word.axis('off')
plt.savefig(path+"/data/hashtag_wordcloud")

tag_common = tag_counts.most_common(10)

pie_label = []
pie_value = []
for i in range(10):
    pie_label.append(tag_common[i][0])
for i in range(10):
    pie_value.append(tag_common[i][1])

explode = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
plt_pie = plt.subplot(1, 2, 2)

textprops = dict(horizontalalignment="center",
                     verticalalignment="top",
                     rotation=0,
                     rotation_mode="anchor",
                     size=7, color="black")

plt_pie.pie(pie_value, explode=explode, labels=pie_label, autopct="%.0f%%", shadow=True, textprops=textprops)
# plt_pie.setp(plt_pie, fontproperties=fontprop)
plt_pie.set_title("코로나 해쉬태그(#) 순위 10 비율")
plt.show()
