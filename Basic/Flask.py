from flask import Flask
app = Flask(__name__)
print('__name__ is :',__name__)
@app.route('/')
def index():
    return "<p style='color:red'>Wellcome !!</p>"

if __name__ == "__main__":
    app.run()