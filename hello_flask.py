from flask import Flask
from flask import render_template
from flask.ext.sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
SQLALCHEMY_TRACK_MODIFICATIONS = True


@app.route('/')
def hello_world():
    return render_template('hello.html')

if __name__ == '__main__':
    app.run()
