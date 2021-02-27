import json
import random
import time
import pandas as pd
from flask import Flask, render_template, jsonify
# Flask Setup
app =  Flask(__name__)


@app.route('/')
def home():

    return render_template("index.html")

@app.route("???")
def output1():
    return jsonify()
    
if __name__=="__main__":
    app.run(debug=True)