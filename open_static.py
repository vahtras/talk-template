#!/usr/bin/env python

import pathlib
import random

import flask

root = pathlib.Path(__file__).parent
app = flask.Flask(
    __name__,
    static_folder=root,
    static_url_path=f'/{root.stem}',
    template_folder=root,
)


@app.route('/')
def index():
    return flask.render_template('index.html')


port = int(5000 + 5000*random.random())
app.run(debug=True, port=port)
