from selenium import webdriver
import time
import timeit
import os

path = os.getcwd()

driver = webdriver.Chrome(path+"\chromedriver.exe")
driver.get('https://www.instagram.com')
time.sleep(2)

def login(id, password):
    email = id
    input_id = driver.find_elements_by_css_selector('input._2hvTZ.pexuQ.zyHYP')[0]
    input_id.clear()
    input_id.send_keys(email)

    password = password
    input_pw = driver.find_elements_by_css_selector('input._2hvTZ.pexuQ.zyHYP')[1]
    input_pw.clear()
    input_pw.send_keys(password)
    input_pw.submit()
    time.sleep(5)
login('','')

def insta_searching(word):
    url = 'https://www.instagram.com/explore/tags/' + word
    driver.get(url)
word = '코로나'
insta_searching(word)
time.sleep(5)

def select_first(driver):
    first = driver.find_elements_by_css_selector('div._9AhH0')[0]
    first.click()
select_first(driver)
time.sleep(3)

import re
from bs4 import BeautifulSoup
import unicodedata

def get_content(driver):

    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')

    try:
        content = soup.select('div.C4VMK > span')[0].text #내용
        content = unicodedata.normalize('NFC', content)
    except:
        content = ' '

    tags = re.findall(r'#[^\s#,\\d]+', content)

    date = soup.select('time._1o9PC.Nzb55')[0]['datetime'][:10]

    try:
        like = soup.select_one('article > div.eo2As > section.EDfFK.ygqzn > div > div > button').text
    except:
        like = soup.select_one(
            'article > div.eo2As > section.EDfFK.ygqzn > div > span').text

    try:
        place = soup.select(
            'body > div._2dDPU.CkGkG > div.zZYga > div > article > header > div.o-MQd > div.M30cS > div.JF9hh > a')[0].text
        place = unicodedata.normalize('NFC', place)
    except:
        place = ''

    data = [content, date, like, place, tags]
    return data
get_content(driver)


def move_next(driver):
    right = driver.find_element_by_css_selector ('a.coreSpriteRightPaginationArrow')
    right.click()
    time.sleep(4)
move_next(driver)

results = []
crawling_pages = 10
error_num = 0
start = timeit.default_timer()
for i in range(crawling_pages):

    try:
        data = get_content(driver)
        results.append(data)
        move_next(driver)
        print(i)
    except:
        error_num = error_num + 1
        print('error: %d' % error_num)
        time.sleep(5)
        move_next(driver)

import pandas as pd

results_df = pd.DataFrame(results)
results_df.columns = ['content','data','like','place','tags']
results_df.to_excel(path+'\crawling_Corona2.xlsx', engine='openpyxl')
end = timeit.default_timer()
print("end time: ", end)
print("time took: ", end - start)






