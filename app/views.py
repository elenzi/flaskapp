'''
Created on 20 Feb 2018

@author: elenalanigan
'''
from flask import render_template
from app import app
import System_Info.main as si

@app.route('/')
def index():
    print(si.main())
    returnDict = {}
    returnDict['user'] = 'Elena' # Feel free to put your name here!
    returnDict['title'] = 'Flask App'
    returnDict['systeminfo'] = si.main()
    return render_template("index.html", **returnDict)