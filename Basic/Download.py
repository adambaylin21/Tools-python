import urllib.request

def download(url,file_name):
    urllib.request.urlretrieve(url, file_name)

for i in range(139,307):
    url = 'https://drive.google.com/viewerng/img?id=ACFrOgA9Svt2Tnon9Q6jxb41lt7c5xYNpJWjoPO1IUjDzYLnBA3qXPsrMHm3EGPvfW0hwd0LZ2QGFn6JLeGe0bc6zWwx2fpDBBu6ruUvpmn5F8M4xhXcQebzkxFILys%3D&page={}&skiphighlight=true&w=1000'.format(i)
    file_name = '{}.png'.format(i)
    download(url,file_name)
    print ('Done - {}'.format(i))