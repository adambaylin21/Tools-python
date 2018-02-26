from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello/')
def hello_name():
    dictx = {'one':10,'two':20,'three':40}
    return render_template('test.html',marks = dictx)

if __name__ == '__main__':
    app.run(debug = True)