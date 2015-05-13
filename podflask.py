#! /usr/bin/python
# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------------
# Author:   Fabien Marteau <fabien.marteau@armadeus.com>
# Created:  13/05/2015
#-----------------------------------------------------------------------------
#  Copyright (2014)  Armadeus Systems
#-----------------------------------------------------------------------------
""" class podflask
"""
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
