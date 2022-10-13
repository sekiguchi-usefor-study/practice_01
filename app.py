from flask import flask
import os

app = Flask(__name__)

@app.route('Hello, Heroku')
def hello():
  return "Hello, Heroku"


if __name__ == '__main__':
  app.run()

