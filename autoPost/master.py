import os, json, re
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

class post_ctkm():
    def __init__(self):
        self.website = "https://quattranmy.com/"
        self.title = "BLACK FRIDAY"
        self.content = """<strong>Thời gian áp dụng: 22/11 - 01/12/2019.</strong>
        <ul><li>Holliston &amp; Hunter Original: Ưu đãi 5%</li>
        <li>Samaire FrankFurt (SA575), LuxAire Flight: Ưu đãi 20%</li>
        <li>Hunter Contempo WH, Hunter Solaris WH: Ưu đãi 25%</li>
        <li>Các sản phẩm khác: Ưu đãi 15%</li></ul>"""

    def start_driver(self):
        where = where_mf('driver/chromedriver')
        self.driver = webdriver.Chrome(where)
        # self.driver = webdriver.Chrome(where, chrome_options=chrome_options)

    def get_page(self, url):
        print('Opening page: {}'.format(url))
        self.driver.get(url)

    def doing(self):
        self.start_driver()
        self.get_page(self.website)
        cookie = load_cookie()
        cookiex = json.loads(cookie)
        for cook in cookiex:
            self.driver.add_cookie(cook)
        a = load_link()
        for b in a:
            editPost(self, b)
        print ('Finish')

def where_mf(where):
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    rel_path = where
    abs_file_path = os.path.join(fileDir, rel_path)
    return abs_file_path

def load_cookie():
    where = where_mf('quattranmy')
    filename = where
    with open(filename, 'r') as cookie:
        cookies = cookie.read()
    return cookies

def editPost(self, url):
    self.get_page(url)
    sleep(10)
    print ('Edit This Post')
    click1 = self.driver.find_element_by_xpath('//*[@id="wp-admin-bar-edit"]/a').click()
    sleep(10)
    price = self.driver.find_element_by_xpath('//*[@id="_regular_price"]').get_attribute("value")
    price  = int(price)
    print ('Calculate Price Sale Off')
    priceoff = int(price - (price/100*15))
    saleoff = self.driver.find_element_by_xpath('//*[@id="_sale_price"]')
    saleoff.send_keys('{}'.format(priceoff))
    title = self.driver.find_element_by_xpath('//div[@class="acf-input-wrap"]/input')
    print ('Add Information Promotion')
    title.send_keys(self.title)
    excontent = self.driver.find_element_by_xpath('//button[@class="wp-switch-editor switch-html" and @id="acf-editor-36-html"]').click()
    content = self.driver.find_element_by_xpath('//textarea[@id="acf-editor-36"]')
    content.send_keys(self.content)
    publish = self.driver.find_element_by_xpath('//input[@id="publish"]')
    finish = self.driver.execute_script("$(arguments[0]).click();", publish)
    sleep(15)

def load_link():
    where = where_mf('link')
    filename = where
    a = []
    with open(filename, 'r') as links:
        for line in links:
            line = line.rstrip('\n')
            a.append(line)
    return a

autoPost = post_ctkm()
autoPost.doing()