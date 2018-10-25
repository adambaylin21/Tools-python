import requests, os

cookies = {
    'PHPSESSID': 'bshpivt3ua1ufhfdv5f30410l0',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:62.0) Gecko/20100101 Firefox/62.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en',
    'Referer': 'https://uid.danseo.net/',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'DNT': '1',
    'Connection': 'keep-alive',
}

params = (
    ('uid', ''),
)

data = {
  'captcha': '03AMGVjXjMSnNRHjkYznXE1UQSrGrpqAR6ybCrIn2eRnhmQ79nhVb1KSheugVf_kvE-Y5DztdOfbbl2UsrjT6Nvjb0Xnyj0gKOAjw7UE4ykOubUIk3iQkt-uq3XkTF5GolMai1-_wzT1pgUSpDQFOv_ifzyumBC2Df_F_c_pBi6Z3juCAtmADpnGt7GxGRv2AfhxEPHQc2arQBCi169ExUx4HS1_im9x0t-sOCyZ9bbQbq3zfoqF4E6quJvwTuCWJy-607TcJRS9qLpczFtZGpPbOd24w0rCvXoA'
}

def convert(uid):
    params = (('uid', uid),)
    response = requests.post('https://uid.danseo.net/api/1_Convert.php', headers=headers, params=params, cookies=cookies, data=data)
    tel = response.json()
    if tel['code'] == 200:
        return tel['phone']
    else:
        return 404

def open_file(stt,filename):
    with open(filename, 'r') as fp:
        line = fp.readline()
        list_uid = {}
        while line:
            uid = line.strip()
            tel = convert(uid)
            if tel != 404:
                list_uid[uid] = tel
                stt += 1
                print ('{}. {} - {}'.format(stt,uid,tel))
            line = fp.readline()
        return list_uid

def write_file(filename,data):
    with open(filename, 'a') as file_object:
        for uid,phone in data.items():
            a = '{}\t{}'.format(uid,phone) + '\n'
            final = file_object.write(a)

def main_cv():
    where = where_mf('files/')
    upload = get_upload(where)
    uid_file = {}
    i = 1
    stt = 0
    for i in range(len(upload)):
        name = upload[i]
        file = open_file(stt,'files/{}'.format(name))
        write_file(name,file)
        print ('Done')

def where_mf(where):
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    rel_path = where
    abs_file_path = os.path.join(fileDir, rel_path)
    return abs_file_path

def get_upload(where):
    a = os.listdir(where)
    a.sort(key=lambda f: int(filter(str.isdigit, f)))
    return a

if __name__ == "__main__":
    main_cv()
