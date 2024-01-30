from flask import Flask, request, jsonify
import pickle
import numpy as np


app = Flask(__name__)

def load_model(model_path):
    with open(model_path, "rb") as file:
        model = pickle.load(file)
    return model

#Load ML Model
model = load_model("RFPredictDiesease.pkl")

#Symptoms Dictionary
symptoms_dict = {0: "itching", 1: "skin rash", 2: "nodal skin eruptions", 3: "dischromic  patches", 4: "continuous sneezing", 
                 5: "shivering", 6: "chills", 7: "watering from eyes", 8: "stomach pain", 9: "acidity", 10: "ulcers on tongue", 
                 11: "vomiting", 12: "cough", 13: "chest pain", 14: "yellowish skin", 15: "nausea", 16: "loss of appetite", 
                 17: "abdominal pain", 18: "yellowing of eyes", 19: "burning micturition", 20: "spotting  urination", 
                 21: "passage of gases", 22: "internal itching", 23: "indigestion", 24: "muscle wasting", 25: "patches in throat", 
                 26: "high fever", 27: "extra marital contacts", 28: "fatigue", 29: "weight loss", 30: "restlessness", 31: "lethargy", 
                 32: "irregular sugar level", 33: "blurred and distorted vision", 34: "obesity", 35: "excessive hunger", 
                 36: "increased appetite", 37: "polyuria", 38: "sunken eyes", 39: "dehydration", 40: "diarrhoea", 41: "breathlessness", 
                 42: "family history", 43: "mucoid sputum", 44: "headache", 45: "dizziness", 46: "loss of balance", 
                 47: "lack of concentration", 48: "stiff neck", 49: "depression", 50: "irritability", 51: "visual disturbances", 
                 52: "back pain", 53: "weakness in limbs", 54: "neck pain", 55: "weakness of one body side", 56: "altered sensorium", 
                 57: "dark urine", 58: "sweating", 59: "muscle pain", 60: "mild fever", 61: "swelled lymph nodes", 62: "malaise", 
                 63: "red spots over body", 64: "joint pain", 65: "pain behind the eyes", 66: "constipation", 67: "toxic look (typhos)", 
                 68: "belly pain", 69: "yellow urine", 70: "receiving blood transfusion", 71: "receiving unsterile injections", 
                 72: "coma", 73: "stomach bleeding", 74: "acute liver failure", 75: "swelling of stomach", 76: "distention of abdomen", 
                 77: "history of alcohol consumption", 78: "fluid overload", 79: "phlegm", 80: "blood in sputum", 
                 81: "throat irritation", 82: "redness of eyes", 83: "sinus pressure", 84: "runny nose", 85: "congestion", 
                 86: "loss of smell", 87: "fast heart rate", 88: "rusty sputum", 89: "pain during bowel movements", 
                 90: "pain in anal region", 91: "bloody stool", 92: "irritation in anus", 93: "cramps", 94: "bruising", 
                 95: "swollen legs", 96: "swollen blood vessels", 97: "prominent veins on calf", 98: "weight gain", 
                 99: "cold hands and feets", 100: "mood swings", 101: "puffy face and eyes", 102: "enlarged thyroid", 
                 103: "brittle nails", 104: "swollen extremeties", 105: "abnormal menstruation", 106: "muscle weakness", 
                 107: "anxiety", 108: "slurred speech", 109: "palpitations", 110: "drying and tingling lips", 111: "knee pain", 
                 112: "hip joint pain", 113: "swelling joints", 114: "painful walking", 115: "movement stiffness", 
                 116: "spinning movements", 117: "unsteadiness", 118: "pus filled pimples", 119: "blackheads", 120: "scurring", 
                 121: "bladder discomfort", 122: "foul smell of urine", 123: "continuous feel of urine", 124: "skin peeling", 
                 125: "silver like dusting", 126: "small dents in nails", 127: "inflammatory nails", 128: "blister", 
                 129: "red sore around nose", 130: "yellow crust ooze"}

#Handle symptoms string data and convert to 1 and 0 array for ML model
def handleSymptoms(symptomList):
    symptomsArray = [0 for i in range(131)]
    symptomsKeys = [key for key, value in symptoms_dict.items() if value in symptomList]
    for i in range(len(symptomsKeys)):
        pos = symptomsKeys[i]
        symptomsArray[pos] = 1
    
    return symptomsArray


@app.route("/predict", methods=["GET"])
def predict():
    data = request.get_json()
    #Check for no input
    if data is None or (all(element == "" for element in data)):
        return jsonify({"message": "No symptoms were selected!"})
    else:
        sympData = handleSymptoms(data)
        #Check if returned array is all 0 (i.e no symptoms match symptoms dictionary)
        if (all(element == 0 for element in sympData)):
            return jsonify({"message": "No symptoms were selected!"})
        else:
            npArray = np.array(sympData)
            reshaped_data = npArray.reshape(1,-1)
            prediction = model.predict(reshaped_data)
            return jsonify({"prediction": prediction[0]})

if __name__ == "__main__":
    app.run(debug=True)


"""

The input format for the API:
["itching", "skin rash",  "nodal skin eruptions", "yellow crust ooze"]

"""
"""
The input format for the ML model:
[1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
"""