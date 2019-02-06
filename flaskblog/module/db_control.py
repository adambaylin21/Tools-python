from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker

# Configure Database
db_name = 'datax.db'

db_app = Flask(__name__)
db_app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_name}'
db_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'
db = SQLAlchemy(db_app)
engine = create_engine(f'sqlite:///{db_name}', echo=True)
Session = sessionmaker(bind=engine)

class acc_blog(db.Model):
    id = db.Column('id', db.Integer, primary_key = True)
    uname = db.Column(db.String())
    passx = db.Column(db.String())

def __init__ (self,idx,uname,passx):
    self.id = idx
    self.uname = uname
    self.passx = passx

def acc_master(typex,idx='',uname='',passx=''):
    if typex == 'add':
        data = acc_blog(uname=uname, passx=passx)
        db.session.add(data)
        db.session.commit()
    if typex == 'edit':
        data = acc_blog.query.filter_by(id=idx).first()
        data.uname=uname
        data.passx=passx
        db.session.commit()
    if typex == 'delete':
        data = acc_blog.query.filter_by(id=idx).first()
        db.session.delete(data)
        db.session.commit()
    if typex == 'all':
        data = acc_blog.query.all()
        return data
    

