from selenium import webdriver
import time

driver = webdriver.Chrome("c:/chromedriver.exe")
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
login('black0401@gmail.com','zy9241zy')

def insta_searching(word):
    url = 'https://www.instagram.com/explore/tags/' + word
    driver.get(url)
word = '코로나'
insta_searching(word)
time.sleep(5)

def select_first(driver):
    first = driver.find_elements_by_css_selector('div._9AhH0')[0] #첫개시물
    first.click()
select_first(driver)
time.sleep(3)

import re
from bs4 import BeautifulSoup
import unicodedata

def get_content(driver):
    # ① 현재 페이지 html 정보 가져오기
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    # ② 본문 내용 가져오기
    try:
        content = soup.select('div.C4VMK > span')[0].text #내용
        content = unicodedata.normalize('NFC', content)
    except:
        content = ' '
    # ③ 본문 내용에서 해시태그 가져오기(정규식 활용)
    tags = re.findall(r'#[^\s#,\\d]+', content)
    # ④ 작성일자 정보 가져오기
    date = soup.select('time._1o9PC.Nzb55')[0]['datetime'][:10]
    # ⑤ 좋아요 수 가져오기
    try:
        like = soup.select_one('article > div.eo2As > section.EDfFK.ygqzn > div > div > button').text
    except:
        like = soup.select_one(
            'article > div.eo2As > section.EDfFK.ygqzn > div > span').text
    # ⑥ 위치정보 가져오기
    try:
        place = soup.select(
            'body > div._2dDPU.CkGkG > div.zZYga > div > article > header > div.o-MQd > div.M30cS > div.JF9hh > a')[0].text
        place = unicodedata.normalize('NFC', place)
    except:
        place = ''
    # ⑦ 수집한 정보 저장하기
    data = [content, date, like, place, tags]
    return data
get_content(driver)

def move_next(driver):
    right = driver.find_element_by_css_selector ('a.coreSpriteRightPaginationArrow')
    right.click()
    time.sleep(4)
move_next(driver)

results = []
crawling_pages = 100
error_num = 0
for i in range(crawling_pages):
    # 게시글 수집에 오류 발생시(네트워크 문제 등의 이유로)  2초 대기 후, 다음 게시글로 넘어가도록 try, except 구문 활용
    try:
        data = get_content(driver)    # 게시글 정보 가져오기
        results.append(data)
        move_next(driver)
        print(i)
    except:
        error_num = error_num + 1
        print('error: %d' % error_num)
        time.sleep(2)
        move_next(driver)

import pandas as pd

results_df = pd.DataFrame(results)
results_df.columns = ['content','data','like','place','tags']
results_df.to_excel('./files/1_crawling_Corona.xlsx')






