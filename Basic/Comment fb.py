import requests, json
import facebook

# /{object-id}/comments
token = ''
id_comment = '100014655317159_584459862052519'

graph = facebook.GraphAPI(access_token=token, version='3.2')

while True:
	for i in range (1,51):
		comment = i
		a = graph.put_comment(object_id=id_comment, message=comment)
		print (i, a['id'])