import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import *
 
engine = create_engine('sqlite:///tutorial.db', echo=True)
 
# create a Session
Session = sessionmaker(bind=engine)
session = Session()
s = Session()

# add user name
def sign_up(acc,passw): 
	dupx = False
	for instance in session.query(User).order_by(User.id):
		# check duplicate
		if instance.username != acc:
			dupx = False
		else:
			dupx = True
	if not dupx:
		user = User(acc,passw)
		session.add(user)
		session.commit() 

if __name__ == '__main__':
	sign_up('admin','123')
