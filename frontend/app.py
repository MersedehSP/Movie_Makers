import json
import pandas as pd
from joblib import dump, load
from flask import Flask, render_template, request, jsonify
# Flask Setup
app =  Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/modelResults', methods=['POST'])
def modelResults():
    X=[]
    inputData = request.form.getlist("inputData[]")
    inputData = [int(i) for i in inputData] 
    X.append(inputData)
    classifier = load('Final_ML_Model.joblib')
    result=classifier.predict(X)
    if (result==0):
        outcome="Not Successful"
    else:
        outcome="Successful"
    return outcome


@app.route('/visuals')
def visuals():
    return render_template("visuals.html")
    
if __name__=="__main__":
    app.run(debug=True)