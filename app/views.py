'''
Created on 20 Feb 2018

@author: elenalanigan
'''
from flask import render_template
from app import app

@app.route('/')
def index():
    returnDict = {}
    returnDict['user'] = 'Elena' # Feel free to put your name here!
    returnDict['title'] = 'Flask App'
    return render_template("index.html", **returnDict)