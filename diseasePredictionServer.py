from flask import Flask, request, jsonify
import pickle
import numpy as np


app = Flask(__name__)

def load_model(model_path):
    with open(model_path, "rb") as file:
        model = pickle.load(file)
    return model

model = load_model('RFPredictDiesease.pkl')

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    npArray = np.array(data)
    reshaped_data = npArray.reshape(1,-1)
    prediction = model.predict(reshaped_data)
    return jsonify({"prediction": prediction[0]})

if __name__ == "__main__":
    app.run(debug=True)