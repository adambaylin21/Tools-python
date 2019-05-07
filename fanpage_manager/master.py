# -*- coding: utf-8 -*-
import facebook
import os, json, re
import requests
import sys, io

def where_mf(where):
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    rel_path = where
    abs_file_path = os.path.join(fileDir, rel_path)
    return abs_file_path

# Page Self Reflected
token = ''
page_id = '1928385924086493'

def get_file(where):
    a = os.listdir(where)
    a.sort(key=lambda x: os.path.getctime(where + x))
    return a

where = where_mf('posts/')
list_folder = get_file(where)

def write_log(logx):
	where = where_mf('log_posts')
	with open (where, 'a') as log:
		log.write(logx)
		log.write('\n')

def upload_allpost():
	for i in range(1,len(list_folder)+1):
		folder_ct = where_mf('posts/{}/img/'.format(i))
		try:
			imgx = get_file(folder_ct)
			list_photos = []
			for j in range(0, len(imgx)):
				link = folder_ct + imgx[j]
				graph = facebook.GraphAPI(access_token=token, version='3.2')
				a = graph.put_photo(image=open(link, 'rb'), message='', published='false', profile_id=page_id)
				list_photos.append(a['id'])
			content = where_mf('posts/{}/content'.format(i))
			with open (content, 'r') as xcontent:
				contentf = xcontent.read()
			attached_media = {
				'message': contentf,
				'access_token': token
			}
			for z in range(0, len(list_photos)):
				b = '{media_fbid:' + list_photos[z] + '}'
				attached_media['attached_media[{}]'.format(z)] = b
			data = attached_media
			response = requests.post('https://graph.facebook.com/1928385924086493/feed', data=data)
			post_photo = json.loads(response.content)
			c = post_photo['id']
			logx = '{} - {}'.format(i,c)
			write_log(logx)
			print (logx)
		except:
			pass

upload_allpost()


# Update Status
# status = """Hello Fans! 😅"""
# response = requests.post('https://graph.facebook.com/{}/feed?message={}?&access_token={}'.format(page_id,status,token))
# id_post = json.loads(response.content)
# print (id_post)

# Upload Img
# link = where_mf('posts/1/img/2.png')
# graph = facebook.GraphAPI(access_token=token, version='3.2')
# a = graph.put_photo(image=open(link, 'rb'), message='', published='false', profile_id=page_id)
# print (a['id'])

# Mutil Posting
# data = {
#   'message': 'Testing multi-photo post!',
#   'attached_media[0]': '{media_fbid:2279789165612832}',
#   'attached_media[1]': '{media_fbid:2279790125612736}',
#   'access_token': token
# }
# response = requests.post('https://graph.facebook.com/1928385924086493/feed', data=data)
# post_photo = json.loads(response.content)
# print (post_photo)