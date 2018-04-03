from flask import Flask, request, flash, url_for, redirect, render_template, session, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from getcode import lay_code
from sentsms import smstouser

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///luxuryfan.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'
app.config['SECRET_KEY'] = "what do you mean"


db = SQLAlchemy(app)
present = datetime.now().strftime('%H:%M %d-%m-%Y')

engine = create_engine('sqlite:///luxuryfan.db', echo=True)
Session = sessionmaker(bind=engine)
sessionx = Session()
s = Session()

class datax(db.Model):
    id = db.Column('id', db.Integer, primary_key = True)
    tenkh = db.Column(db.String())
    sdt = db.Column(db.String())
    sosp = db.Column(db.String())
    time = db.Column(db.String())
    code = db.Column(db.String())
    sms = db.Column(db.String())

def __init__ (self,tenkh,sdt,code,sosp,time,sms):
    self.tenkh = tenkh
    self.sdt = sdt
    self.sosp = sosp
    self.time = time
    self.code = code
    self.sms = sms

@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'phamvanhai' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash ('Wrong password!')
    return show_all()

@app.route('/logout')
def logout():
    session['logged_in'] = False
    return show_all()

@app.route('/')
def show_all():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('show_all.html', datax = datax.query.all())

# Danh sách khách hàng chưa gửi sms
@app.route('/sms')
def sms_sent():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('sms.html',datax = sessionx.query(datax).filter_by(sms="0"))

# Gửi SMS cho khách hàng
@app.route('/sent')
def has_sent():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        smstouser(datax)
        return render_template('done.html')


@app.route('/new', methods=['GET', 'POST'])
def new():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        if request.method == 'POST':
            if not request.form['name'] or not request.form['sdt'] or not request.form['sosp']:
                flash('Vui lòng nhập dữ liệu vào tất cả các ô', 'thiếu dữ liệu')
            else:
                sospx = int(request.form['sosp'])
                gencode = str(lay_code(sospx))
                data = datax(tenkh=request.form['name'], sdt=request.form['sdt'],
                code = gencode, sosp = request.form['sosp'], time = present, sms = '0')
                db.session.add(data)
                db.session.commit()

                flash('Dữ liệu đã được cập nhật')
                return redirect(url_for('show_all'))
        return render_template('new.html')

if __name__ == '__main__':
    # db.create_all()
    app.run(debug=True)