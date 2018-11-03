from threading import Thread
import threading
import time

def ham1(thamso):
	for so in thamso:
		time.sleep(0.0000000002)
		print ('Tich:', so*so)

def ham2():
	for i in range(4):
		print (i)

mang = [1,3,7,9]

if __name__ == '__main__':
	try:
		t1 = threading.Thread(target=ham1, args=(mang,))
		t2 = threading.Thread(target=ham2,)
		t1.start()
		t2.start()
		t1.join()
		t2.join()
	except:
		print('error')