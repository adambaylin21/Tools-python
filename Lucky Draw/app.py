from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from getcode import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///luxuryfan.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'
app.config['SECRET_KEY'] = "what do you mean"

db = SQLAlchemy(app)
present = datetime.now().strftime('%H:%M %d-%m-%Y')

class datax(db.Model):
   id = db.Column('id', db.Integer, primary_key = True)
   tenkh = db.Column(db.String(100))
   sdt = db.Column(db.String(50))
   sosp = db.Column(db.String(50))
   time = db.Column(db.String(50))
   code = db.Column(db.String(200))

def __init__ (self,tenkh,sdt,code,sosp,time):
   self.tenkh = tenkh
   self.sdt = sdt
   self.sosp = sosp
   self.time = time
   self.code = code


@app.route('/')
def show_all():
   return render_template('show_all.html', datax = datax.query.all())



@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['sdt'] or not request.form['sosp']:
            flash('Vui lòng nhập dữ liệu vào tất cả các ô', 'thiếu dữ liệu')
        else:
            sospx = int(request.form['sosp'])
            gencode = str(lay_code(sospx))
            data = datax(tenkh=request.form['name'], sdt=request.form['sdt'],
              code = gencode, sosp = request.form['sosp'], time = present)
            db.session.add(data)
            db.session.commit()

            flash('Dữ liệu đã được cập nhật')
            return redirect(url_for('show_all'))
    return render_template('new.html')

if __name__ == '__main__':
   # db.create_all()
   app.run(debug = True)
    