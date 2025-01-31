from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd
import pickle

application = Flask(__name__)
app = application
ml_model = pickle.load(open('regression.pkl','rb'))

@app.route("/")
def helloWorld():
    return "Hello World"

@app.route("/predict", methods =['GET','POST'])
def prediction():
    if request.method=="POST":
       interest_rate = float(request.form.get('Interest Rate'))
       unemployment_rate = float(request.form.get('Unemployment Rate'))
       result = ml_model.predict([[interest_rate,unemployment_rate]])
       return render_template('home.html', results = result[0])
       
    else:
        return render_template("home.html")


if __name__=="__main__":
    app.run(debug=True)