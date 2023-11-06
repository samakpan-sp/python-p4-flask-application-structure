#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello World! Welcome to my page</h1>"

# @app.route('/<username>')
# def user(username):
#     return f'Profile for {username}'

@app.route('/<student>')
def student(student):
    return f'Student: {student}'

@app.route('/<string:username>')
def user(username):
    return f'<h1>Profile for {username}</h1>'

if __name__ == '__main__':
    app.run(port=5555)