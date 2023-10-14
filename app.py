import numpy as np
from flask import Flask, request, render_template
import pickle

#Create flask appp
app = Flask (__name__)

#Load the pickle model
model = pickle.load(open("model.pkl" , "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods =["POST"])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features =[ np.array(float_features)]
    prediction = model.predict(features)  
    if prediction == 0:
       prediction= "Bad"
    else:
       prediction= "Good"
    

    return render_template("index.html", prediction_text = "Your mental health is: {}". format(prediction))
if __name__ == "__main__": 
    app.run()
    