import re, os

def done(data):
	with open('uid.txt','a') as codex:
		codex.write(str(data) + '\n')

def search(string):
	try:
		data = re.search(r';id=3D(.*?)&', string).group(1)
		if data != "None":
			return data
	except:
		pass
	return "None"

def get_file(where):
    a = os.listdir(where)
    a.sort(key=lambda x: os.path.getctime(where + x))
    return a

def where_mf(where):
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    rel_path = where
    abs_file_path = os.path.join(fileDir, rel_path)
    return abs_file_path

def read_file(where,file):
	filename = where + file
	with open(filename, 'r') as file_object:
		data_embed = file_object.read()
	return data_embed

where = where_mf('yahoo/')
list_file = get_file(where)

for file in list_file:
	data = read_file(where,file)
	uid = search(data)
	if uid != "None":
		print (uid)
		done(uid)

# re.search(r'Part 1(.*?)Part 3', s).group(1)
# print (kq)


