# -*- encode:uft8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, random, re
from unidecode import unidecode

_punct_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')

browser = webdriver.Firefox()
browser.get('https://mikgroup-imperiaskygarden.com')

def slugify(text, delim=u'-'):
    """Generates an ASCII-only slug."""
    result = []
    for word in _punct_re.split(text.lower()):
        result.extend(unidecode(word).split())
    return unidecode(delim.join(result))

def ffos(name,emails,phones):
    username = browser.find_element_by_name('your-name')
    email = browser.find_element_by_name('your-email')
    phone = browser.find_element_by_name('your-tel')
    username.send_keys(name)
    phone.send_keys(phones)
    email.send_keys(emails, Keys.RETURN)
    time.sleep(5)

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
    k = {'name':d, 'email':e, 'phone':j}
    # print (k['name'],k['email'], k['phone'])
    return k

for i in range(0,100):
    a = gen_if()
    ffos(a['name'],a['email'],a['phone'])
    browser.refresh()

# if __name__ == "__main__":
    # gen_if()

