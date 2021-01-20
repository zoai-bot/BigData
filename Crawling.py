from selenium import webdriver

driver = webdriver.Chrome("c:/chromedriver.exe")

# 예제 5-2 인스타그램 접속하기
import time

# 인스타그램 접속하기
driver.get('https://www.instagram.com')
time.sleep(2)
# 예제 5-3 인스타계정으로 로그인하기
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





