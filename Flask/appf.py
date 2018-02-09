from flask import Flask , render_template
from config import Config

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html',username='Adam Baylin')

if __name__ == "__main__":
    app.run()