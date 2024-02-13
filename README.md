# Disease Prediction
## Deployed on Flask Server
1.  Navigate where the python file ```diseasePredictionServer.py``` is.
2.  Run ```python diseasePredictionServer.py``` on terminal.
3.  API is deployed on ```http://127.0.0.1:5000/predict```.
4.  Test using postman.
5.  GET REQUEST JSON format:

   ```["itching", "skin rash",  "nodal skin eruptions", "yellow crust ooze"]```

6. Server will convert the string list to 1s and 0s array(refer to point 7) for the ML model.
7. Input format for the Machine Learning model:

   [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 1]
  
8. Where 1 is indication of the symptom and 0 is absence of the symptom.
9. Results will return as JSON object: ```{"prediction": "Impetigo"}```.
10. OR ```["skin peeling", "silver like dusting", "small dents in nails", "inflammatory nails"]```
11. Results will return ```{"prediction": "Psoriasis"}```.
12. Server is also deployed in Azure: ```https://predictdisease.azurewebsites.net/predict```
  
