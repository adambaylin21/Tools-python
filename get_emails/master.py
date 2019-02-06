# -*- coding: utf-8 -*-

import os, json, re
from random import randint
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()  
chrome_options.add_argument("--headless")

class get_emails():
    def __init__(self):
        self.url_tool = "https://www.teezily.com/"
    
    def start_driver(self):
        print('Starting driver...')
        where = where_mf('driver/chromedriver')
        self.driver = webdriver.Chrome(where)
        # self.driver = webdriver.Chrome(where, chrome_options=chrome_options)
        sleep(3)

    def get_page(self, url):
        print('Getting page...')
        self.driver.get(url)
        sleep(randint(2,3))

    def parse(self):
        self.start_driver()
        self.get_page(self.url_tool)
        cookie = load_cookie()
        cookie = json.loads(cookie)
        for cook in cookie:
            self.driver.add_cookie(cook)
        spy_email(self)
        sleep(5)

def spy_email(self):
    url = self.url_tool + 'account/orders'
    current_window = self.driver.current_window_handle
    self.driver.get(url)
    sleep(5)
    for i in range(1,414):
        sleep(7)
        list_emails = self.driver.page_source
        data = re.findall(r'<p class="oo__table-email ng-binding">(.*?)</p>', list_emails)
        for email in data:
            write_email(email)
            print(email)
        element = self.driver.find_element_by_xpath('//*[@id="orders_overview"]/div/div[3]/ul/li[4]/a').click()
        print ('Get Page:', i)
        sleep(7)

def write_email(data):
    with open('emails.txt', 'a') as email:
        email.write(data + '\n') 

def load_cookie():
    where = where_mf('cookies/teezily')
    filename = where
    with open(filename, 'r') as cookie:
        cookies = cookie.read()
    return cookies

def where_mf(where):
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    rel_path = where
    abs_file_path = os.path.join(fileDir, rel_path)
    return abs_file_path


email_tz = get_emails()
email_tz.parse()