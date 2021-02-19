from selenium import webdriver
import time
import os
from selenium.common.exceptions import NoSuchElementException
import timeit
from soupsieve import SelectorSyntaxError
import re
from bs4 import BeautifulSoup
import unicodedata
import pandas as pd

path = os.getcwd()

driver = webdriver.Chrome(path + "/chromedriver.exe")
driver.get('https://www.instagram.com')
time.sleep(2)


def login(userid, password):
    email = userid
    input_id = driver.find_elements_by_css_selector('input._2hvTZ.pexuQ.zyHYP')[0]
    input_id.clear()
    input_id.send_keys(email)

    password = password
    input_pw = driver.find_elements_by_css_selector('input._2hvTZ.pexuQ.zyHYP')[1]
    input_pw.clear()
    input_pw.send_keys(password)
    input_pw.submit()
    time.sleep(5)
    try:
        aa = driver.find_element_by_id("slfErrorAlert")
        print(aa)
    except NoSuchElementException:
        print("정성적으로 로그인 되었습니다.")


login('black0401@naver.com', '@zy9241zy')


def insta_searching(search):
    url = 'https://www.instagram.com/explore/tags/' + search
    driver.get(url)
    time.sleep(5)


word = '코로나'
insta_searching(word)


def select_first(driver):
    first = driver.find_elements_by_css_selector('div._9AhH0')[0]
    first.click()
    time.sleep(3)


select_first(driver)

html = driver.page_source
soup = BeautifulSoup(html, 'lxml')
content = soup.select('div.C4VMK > span')[0].text

with open(file=path + "/data/sample_content.txt", mode='w+', encoding='utf-8') as text:
    text.write(content)
text.close()


def get_content(driver):
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')

    article = soup.select_one('body > div._2dDPU.CkGkG > div.zZYga > div > article')

    try:
        content = article.select_one('div.eo2As > div.EtaWk > ul > div > li > div > div > div.C4VMK > span').text
        content = unicodedata.normalize('NFC', content)
    except (SelectorSyntaxError, AttributeError):
        content = ' '

    tags = re.findall(r'#[^\s#,\\d]+', content)

    date = article.select('time._1o9PC.Nzb55')[0]['datetime'][:10]

    try:
        like = article.select_one('div.eo2As > section.EDfFK.ygqzn > div > div > a > span').text
    except (SelectorSyntaxError, AttributeError):
        like = article.select_one('div.eo2As > section.EDfFK.ygqzn > div > span > span').text

    try:
        place = article.select('header > div.o-MQd > div.M30cS > div.JF9hh > a').text
        place = unicodedata.normalize('NFC', place)
    except (SelectorSyntaxError, AttributeError):
        place = ''

    data = [content, date, like, place, tags]
    return data


get_content(driver)


def move_next(driver):
    right = driver.find_element_by_css_selector('a.coreSpriteRightPaginationArrow')
    right.click()
    time.sleep(4)


move_next(driver)

results = []
crawling_pages = 5
error_num = 0
start = timeit.default_timer()

for i in range(crawling_pages):
    try:
        data = get_content(driver)
        results.append(data)
        move_next(driver)
    except:
        error_num = error_num + 1
        print('error: %d' % error_num)
        time.sleep(5)
        move_next(driver)


results_df = pd.DataFrame(results)
results_df.columns = ['content', 'data', 'like', 'place', 'tags']
results_df.to_excel(path+'/data/crawling_Corona2_sample.xlsx', engine='openpyxl')
end = timeit.default_timer()

print("time taken: ", end - start)
