# -*- coding : utf-8 -*-

import requests
import json, random, re
from unidecode import unidecode

_punct_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')

def slugify(text, delim=u'-'):
    """Generates an ASCII-only slug."""
    result = []
    for word in _punct_re.split(text.lower()):
        result.extend(unidecode(word).split())
    return unidecode(delim.join(result))
    
cookies = {
    'PHPSESSID': '2m3mcrbn7vtvkfm9831f17i0o5',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0',
    'Accept': 'text/html, */*; q=0.01',
    'Accept-Language': 'en',
    'Referer': 'http://imperiaskygardenminhkhaii.com/',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'DNT': '1',
    'Connection': 'keep-alive',
}

data = {
  'avia_1_1': '093%20132%203666',
  'avia_2_1': 'Test%40gmail.com',
  'avia_3_1': '',
  'avia_generated_form1': '1'
}

def fos(data):
    response = requests.post('http://imperiaskygardenminhkhaii.com/', headers=headers, cookies=cookies, data=data)
    return response

for i in range (0,1000):
    a = random.choice(('Phạm','Nguyễn','Trần','Lê','Đào','Đinh','Phan'))
    b = random.choice((' Thị',' Cẩm',' Hoài',' Đức',' Bá',' Diệu',' Thu',' Hà',''))
    c = random.choice((' Anh',' Linh',' Hiền',' Quỳnh',' Thư',' Quyên',' Ly',' Trang',' Ngân',' Yến',' Hân',' Hằng'))
    d = a + b + c
    # e = json.dumps(d)
    e = d.replace(" ", "")
    e = slugify(e) + str(random.randint(10,1989)) + '@gmail.com'
    f = random.choice(('096','097','098','090','093','091','094'))
    g = random.choice(('1234','1511','4361','4103','6810','4308','6603','4061','1571','6920','1508','6909'))
    h = random.choice(('183','531','961','814','348','683','261','592','313','888','999','780','587','548'))
    j = f + g + h
    data['avia_2_1'] = e
    data['avia_1_1'] = j
    k = fos(data)
    print ('Name: {} - {} - {}'.format(e,j,k))