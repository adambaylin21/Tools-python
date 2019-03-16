# -*- coding : utf-8 -*-
import re, os

def search(string):
	try:
		data = re.search(r'([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)', string).group(1)
		if data != "None":
			return data
	except:
		pass
	return "None"

def where_mf(where):
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    rel_path = where
    abs_file_path = os.path.join(fileDir, rel_path)
    return abs_file_path

def read_file():
    b = set()
    file = where_mf('emails')
    with open(file) as infile:
        for line in infile:
            a = search(line)
            print ('{} - {}'.format(line.index, a))
            b.add(a)
    return b

def get_emails():
    a = read_file()
    with open('emails', 'w') as emailx:
        for b in a:
            emailx.write(str(b) + '\n')

if __name__ == "__main__":
    get_emails()
