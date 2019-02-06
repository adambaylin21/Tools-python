from flask import Flask, request, flash, url_for, redirect, render_template, session, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from passlib.hash import sha256_crypt
from module.db_control import acc_master

# Configure Database
db_name = 'datax.db'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'
db = SQLAlchemy(app)
engine = create_engine(f'sqlite:///{db_name}', echo=True)
Session = sessionmaker(bind=engine)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/post/<post_name>')
def post(post_name):
    if post_name == 'Test':
        return 'Test Done'


if __name__ == '__main__':
    # app.run(debug=True)
    acc = acc_master('all')
    for datax in acc:
        print (datax.uname)
        print (datax.passx)
