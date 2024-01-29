# Disease Prediction
## Deployed on Flask Server
1.  Navigate where the python file ```diseasePredictionServer.py``` is.
2.  Run ```python diseasePredictionServer.py``` on terminal.
3.  API is deployed on ```http://127.0.0.1:5000/predict```
4.  Test using postman
5.  Data format is a list:
   
   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0,0, 0, 0, 0, 0]
  
  4. Where 1 is indication of the symptom and 0 is absence of the symptom
  5. Results will return as: ```{"prediction": "Urinary tract infection"}```
  
