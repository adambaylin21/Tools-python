import requests, os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en',
    'Content-Type': 'application/json',
    'RequestTime': '1606205998511',
    'Origin': 'https://khongquangcao.ais.gov.vn',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Referer': 'https://khongquangcao.ais.gov.vn/',
    'TE': 'Trailers',
}


def checkDnc(sdt):
    data = '{request_id:1606205998500,msisdn:'+sdt+',username:web,key:d45728c3caed6fae47a6342f94083f49cbb674b2bcb11500595af3f20d0bdb3c}'
    response = requests.post('https://khongquangcao.ais.gov.vn/apiback/sms_api/v1/api_search', headers=headers, data=data)
    b = response.content
    c = b.decode("utf-8")
    if 'da nam' in c:
        return True
    else: return False

def where_mf(where):
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    rel_path = where
    abs_file_path = os.path.join(fileDir, rel_path)
    return abs_file_path

def load_list():
    where = where_mf('list')
    filename = where
    with open(filename, 'r') as cookie:
        cookies = cookie.readlines()
    return cookies

def writeList(sdt):
    with open("final", "a") as myfile:
        myfile.write(sdt)
    print ('{} - Can SMS Marketing'.format(sdt))

def mainCheck():
    a = load_list()
    for b in a:
        c = checkDnc(b)
        if c != True:
            writeList(b)
        else:
            print ('{} - Can\'t SMS Marketing'.format(b))


if __name__ == '__main__':
    # sdt = '0964133557'
    # a = checkDnc(sdt)
    # print (a)

    mainCheck()