from flask import Flask
from flask import render_template
from flask.ext.sqlalchemy import SQLAlchemy
import datetime as dt
app = Flask(__name__)
app.config.from_object('config.Config')
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    tweets = db.relationship('Tweet')

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return 'User {}'.format(self.username)


class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(140), unique=False)
    user = db.Column(db.Integer, db.ForeignKey('user.id'))
    datetime = db.Column(db.DateTime)

    def __init__(self, text, user):
        self.text = text
        self.user = user
        self.datetime = dt.datetime.now()

    def __repr__(self):
        return '{} by {} at {}'.format(self.text, self.user, self.datetime)



@app.route('/')
def hello_world():
    return render_template('hello.html', tweets = Tweet.query.all())

if __name__ == '__main__':
    app.run()
