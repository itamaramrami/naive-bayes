import uvicorn
from fastapi import FastAPI ,Request
from fastapi import FastAPI
from test import Tester
import numpy as np
from dal import NaiveBayesClassifier
from menu import menu

app = FastAPI()

menu_instance = menu()
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



@app.get("/options")
async def get_options():
    options = {}
    for col in menu_instance.columns:
        unique_vals = menu_instance.db[col].dropna().unique().tolist()
        options[col] = unique_vals
    return options



@app.get("/test")
async def get_test():
    test=Tester()
    t=test.run_test()
    return t

@app.get("/predict")
async def predict(request: Request):
    query_params = dict(request.query_params)
    print(query_params)

    
    classifier = NaiveBayesClassifier()
    summary = classifier.dictofsummary()
    prediction, scores = classifier.predict_from_summary(summary, query_params)
    return {
        "prediction": int(prediction),
        "scores": convert_numpy_to_python(scores)
    }



if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)