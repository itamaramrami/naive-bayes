import uvicorn
import numpy as np
from fastapi import FastAPI ,Request
from Classifie.classifie import NaiveBayesPredictor
import requests
app = FastAPI()
print("hello v2")
predictor = NaiveBayesPredictor()
response = requests.get("http://model:81/predict")  #מחזיר את המודל
summary = response.json()
responsedata = requests.get("http://model:81/data")  # מחזיר את הטסט
data = responsedata.json()



def convert_numpy_to_python(obj):
    if isinstance(obj, dict):
        return {convert_numpy_to_python(k): convert_numpy_to_python(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_numpy_to_python(i) for i in obj]
    elif isinstance(obj, (np.integer, np.floating)):
        return obj.item()  
    elif hasattr(obj, "item"):  
        return obj.item()
    else:
        return obj





@app.get("/test")
async def get_test():
    return data




@app.get("/call-model")
async def predict(request: Request):
    query_params = dict(request.query_params)
    prediction, scores = predictor.predict_from_summary(summary, query_params)
    return {
        "prediction": int(prediction),
        "scores": convert_numpy_to_python(scores)
    }



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
