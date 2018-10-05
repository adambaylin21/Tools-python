import json
import requests

api_token = '8dc0656f-604a-4e88-89dc-216176af38d6'
api_url_base = 'https://plus.teezily.com/apidocs/api-docs.json'


headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {0}'.format(api_token)}

def get_list():
    response = requests.get(api_url_base, headers=headers)
    data = response.json()
    print (data)
    print (response.basePath)
    print (response.headers)


if __name__ == '__main__':
	get_list()