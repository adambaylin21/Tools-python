from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ast import literal_eval
from smsapi import *

app = Flask(__name__)
db = SQLAlchemy(app)

engine = create_engine('sqlite:///luxuryfan.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
s = Session()

class datax(db.Model):
    id = db.Column('id', db.Integer, primary_key = True)
    tenkh = db.Column(db.String())
    sdt = db.Column(db.String())
    sosp = db.Column(db.String())
    time = db.Column(db.String())
    code = db.Column(db.String())
    sms = db.Column(db.String())


def smstouser(datax):
    data = session.query(datax).filter_by(sms="0")
    for raw in data:
        j = literal_eval(raw.code)
        z = raw.sdt
        code = ''
        for i in range (0,len(j)):
            code += j[i] + ', '
        fmess = """Cam on Quy khach da mua Quat tran My tai LuxuryFan. Ma du thuong CTKM "Mua Quat tran My - Vi vu Hoa Ky" cua Quy khach la:"""+code+"""Chi tiet quay thuong vui long xem tai: www.quattranmy.com"""
        logsms = ('Da gui cho: %s - Code la: %s \n'%(z,code))
        if sendsms(fmess,str(z)) == 'Done':
            wlog(logsms)
            smsxx = session.query(datax).filter_by(id=raw.id).first()
            smsxx.sms = '1'
            session.commit()
            print (raw.id)
        else :
            logsms = ('Chua gui sms cho: %s \n'%(z))
            wlog(logsms)
        
def wlog(log):
    with open('logsms.txt', 'a') as post:
        post.write(log)
    
if __name__ == "__main__":
    smstouser(datax)