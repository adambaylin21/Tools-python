import requests

cookies = {
    'jreject': '1',
    'PHPSESSID': 'sa9uvgclr946450uu7m0eqk1r0',
    'ci_session': 'Tik4m6xzrq7wU2YNKdOC3wdWRxEOkke8hjsVoPnKUhaZ3ZcDqumgZaHQwESD3u5Dl8Tbl2qHw3FTccxyicD9D8lOsvJm1A%2FkReyQBJ9hoyl%2FHfY%2BDxxIrwb0oNxTl2jyGCMzSIA4iqf6fTfxnxTsdd82CXcp0HogY8cnU6%2BU4weq8vYrDzw%2BEYmCDv1SjyI%2BYTMTHfNrOQIrJ6KNhGK645ARJ5fvnEsTHbhAzX55g4v3j46Eo2EVU%2BeJVL1oMHygIbBfi%2FUSrIczVgowQjx4tbmVaV%2FxrVXMLbFYXubmc2Ltp97rL0ztrcedA7z8ee69FYAdVwqc7a2jnVZ3KXZMzomSttQW2Alil567Fel6YKp%2BieA29ZBYdUzqDmUq8DhnLZLA96VziVi09%2F%2BgPM0GFq0MLrgkqTT4APdf5Mr%2FOUfsZf2ny6oDADH0dfoBVMkz3PWVnrebCrLPYTaOUxEBbTZSJFQ2S7neiivIclegb2OvjZYlnyxmW1HFTYP3HhYJ9lWaC7QDUX1Az43j71ExnQffNr6skZAjjepkMSSLWQNWf2JMJSoOqCfAq85zEXTVdBebYZKFoztHJFVeYNzQmkmlh3asKRfFKfwmihIh2rYq3Z%2FYrvwMEPJUls5FRer5KAWTvTSWEBOX1Urx8gNj9EDep0jv6MEwrDcOR8gmjaWmdQzAdrN4jo%2BTeQyP65oFABtlP184ZU58sSp38m5GulYQplCU%2BjoG4ocbn0Z6JXGOhE%2BT8vkjo%2B8L1s3KPX%2B3qZUDbRD4AfOCXzKCR6RSsu8tQvIGMxHNoinPioVSc%2BM1ckIsQZ%2F%2BBakgB5xfU3Rk313TeL1gDXb1%2FF9kt8qVqWxahhqTwSoXXZSMgOwhMEXja0dNnw%2FG8g0wi4vSBHrw',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:62.0) Gecko/20100101 Firefox/62.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'Referer': 'https://vnphones.com/convert/findbyuid',
    'Content-Type': 'multipart/form-data; boundary=---------------------------664954317661452002837468707',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}

params = {
   'Content-Disposition': 'form-data',
   'ListUidTextarea':'100001794021366',
}

response = requests.post('https://vnphones.com/convert/findbyuid#', headers=headers, cookies=cookies, params = params)
print (type(response))
print (response.headers)
print (response.content)
