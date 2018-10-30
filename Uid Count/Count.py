import os

def where_mf(where):
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    rel_path = where
    abs_file_path = os.path.join(fileDir, rel_path)
    return abs_file_path

def get_upload(where):
    a = os.listdir(where)
    if len(a) > 1:
        a.sort(key=lambda f: int(filter(str.isdigit, f)))
    return a

def open_file(stt,filename):
    with open(filename, 'r') as fp:
        line = fp.readline()
        while line:
            uid = line.strip()
            stt += 1
            line = fp.readline()
    return stt

def main_count(folder):
    where = where_mf(folder)
    upload = get_upload(where)
    b = len(upload)
    i = 0
    stt = 0
    while i < b:
        name = upload[i]
        i += 1
        file = open_file(stt,'{}{}'.format(folder,name))
        stt = file
    return stt

def sub_folder():
	where = where_mf('')
	a = [x[1] for x in os.walk(where)]
	for b in a:
		for c in b:
			folder = '{}/'.format(c)
			d = main_count(folder)
			print ('Folder: {} - {} UID'.format(c,d))

if __name__ == "__main__":
	sub_folder()
