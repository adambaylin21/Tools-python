# -*- coding: utf-8 -*- 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, random, re, os
from unidecode import unidecode
from slugify import slugify

_punct_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')

def where_mf(where):
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    rel_path = where
    abs_file_path = os.path.join(fileDir, rel_path)
    return abs_file_path

where = where_mf('driver/chromedriver')
browser = webdriver.Chrome(where)
browser.get('http://imperiaskygardenminhkhaii.com')

def ffos(emails,phones):
    # username = browser.find_element_by_name('your-name')
    email = browser.find_element_by_name('avia_2_1')
    phone = browser.find_element_by_name('avia_1_1')
    # username.send_keys(name)
    phone.send_keys(phones)
    email.send_keys(emails, Keys.RETURN)
    time.sleep(7)

def gen_if():
    a = random.choice(('Phạm','Nguyễn','Trần','Lê','Đào','Đinh','Phan'))
    b = random.choice((' Thị',' Cẩm',' Hoài',' Đức',' Bá',' Diệu',' Thu',' Hà',''))
    c = random.choice((' Anh',' Linh',' Hiền',' Quỳnh',' Thư',' Quyên',' Ly',' Trang',' Ngân',' Yến',' Hân',' Hằng'))
    d = a + b + c
    e = d.replace(" ", "")
    e = slugify(e) + str(random.randint(10,1989)) + '@gmail.com'
    f = random.choice(('096','097','098','090','093','091','094'))
    g = random.choice(('1234','1511','4361','4103','6810','4308','6603','4061','1571','6920','1508','6909'))
    h = random.choice(('183','531','961','814','348','683','261','592','313','888','999','780','587','548'))
    j = f + g + h
    k = {'email':e, 'phone':j}
    # print (k['name'],k['email'], k['phone'])
    return k

i = 0
while True:
    a = gen_if()
    ffos(a['email'],a['phone'])
    i+=1
    print (i, '-', a['email'], a['phone'])
    browser.refresh()

# if __name__ == "__main__":
    # gen_if()

