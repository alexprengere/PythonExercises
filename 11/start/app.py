#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html', text='The text!')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
