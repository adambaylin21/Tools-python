# -*- coding: utf-8 -*-

import requests
import json, re, os, random
from time import sleep
from random import randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from unidecode import unidecode

chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--window-size=1000x520")

def where_mf(where):
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    rel_path = where
    abs_file_path = os.path.join(fileDir, rel_path)
    return abs_file_path

class Vote_auto():
    def __init__(self):
        self.url_web = "https://quattranmy.com"

    def start_driver(self):
        print ('Starting driver...')
        where = where_mf('driver/chromedriver')
        self.driver = webdriver.Chrome(where, chrome_options=chrome_options)

    def stop_driver(self):
        print ('Closing driver...')
        self.driver.quit()
    
    def get_page(self, url):
        print ('Open page...')
        self.driver.get(url)
        sleep(randint(2,3))

def open_vote():
    a = Vote_auto()
    a.start_driver()
    file_link = where_mf('website')
    with open(file_link, 'r') as full_list:
        for line in full_list:
            url = line
            print (url)
            start_vote(a, url)

def start_vote(a, url):
    list_review = reviewx()
    a.get_page(url)
    for i in range (0,9):
        author = gen_if()
        review = list_review[i]
        a.driver.find_element_by_xpath('//a[@class="btn-showreview"]').click()
        star = random.choice(('//a[@class="star-5"]','//a[@class="star-4"]'))
        a.driver.find_element_by_xpath(star).click()
        comment = a.driver.find_element_by_xpath('//textarea[@placeholder]')
        name = a.driver.find_element_by_xpath('//*[@id="author"]')
        comment.send_keys(review.decode('utf-8'))
        name.send_keys(author.decode('utf-8'))
        a.driver.find_element_by_xpath('//input[@name="submit"]').click()
        sleep(randint(10,15))

def gen_if():
    a = random.choice(('Phạm','Nguyễn','Trần','Lê','Đào','Đinh','Phan','Vũ','Võ','Bùi','Đỗ','Dương'))
    b = random.choice((' Thị',' Cẩm',' Hoài',' Diệu',' Thu',' Hà',''))
    c = random.choice((' Anh',' Linh',' Hiền',' Quỳnh',' Thư',' Quyên',' Ly',' Trang',' Ngân',' Yến',' Hân',' Hằng'))    
    f = random.choice((' Văn',' Hoàng',' Trường',' Hải',' Ngọc',' Bảo',' Hữu',' Minh',''))
    g = random.choice((' Sơn',' Tùng',' Tuấn',' Trung',' Thịnh',' Thiên',' Thành',' Toàn',' Quốc',' Quang',' Phúc',' Phong'))
    d, h = a + b + c, a + f + g
    return random.choice((d,h))

def get_review():
    file_review = where_mf('review')
    with open(file_review, 'rb') as full_list:
        i = 0
        for line in full_list:
            i+= 1
        return randint (0,i)

def reviewx():
    b = set()
    while True:
        a = get_review()
        b.add(a)
        if len(b) > 9:
            break
    list_rv = []
    for i in b:
        file_review = where_mf('review')
        with open(file_review, 'rb') as full_list:
            c = 0
            for line in full_list:
                if c == i:
                    list_rv.append(line)
                c+= 1
    return list_rv

if __name__ == '__main__':
    # start_vote()
    # review()
    open_vote()
