from flask import Flask
from flask import render_template
from flask.ext.sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return 'User {}'.format(self.username)



@app.route('/')
def hello_world():
    return render_template('hello.html')

if __name__ == '__main__':
    app.run()
