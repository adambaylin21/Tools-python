from flask import Flask, redirect, url_for, request , render_template
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name

@app.route('/')
def indexx():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)