from flask import Flask
from flask import render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
import datetime as dt

app = Flask(__name__)
app.config.from_object('config.Config')
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '{}'.format(self.username)


class Tweet(db.Model):
    __tablename__ = 'tweet'
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    text = db.Column(db.String(140), unique=False)
    datetime = db.Column(db.DateTime)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    author = db.relationship("User", backref = 'tweets')



    def __init__(self, text, author):
        self.text = text
        self.author = author
        self.datetime = dt.datetime.now()

    def __repr__(self):
        return '{} by {} at {}'.format(self.text, self.author, self.datetime)



@app.route('/')
def hello_world():
    return render_template('hello.html', tweets = Tweet.query.all())

if __name__ == '__main__':
    app.run()
