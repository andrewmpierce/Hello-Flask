from flask import Flask
from flask import render_template

import datetime as dt

app = Flask(__name__)
app.config.from_object('config.Config')



@app.route('/')
def hello_world():
    return render_template('hello.html', tweets = Tweet.query.all())

if __name__ == '__main__':
    app.run()
