import uvicorn
from fastapi import FastAPI 
from Model.model import NaiveBayesModel
from Test.test import Tester
from DB.db import TestData
import numpy as np


app = FastAPI()
print("hello v2")

model = NaiveBayesModel()  
data=TestData()

summary = model.dict_of_summary() 
variable=model.target_variable()




def convert_numpy_to_python(obj):
    if isinstance(obj, dict):
        return {convert_numpy_to_python(k): convert_numpy_to_python(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_numpy_to_python(i) for i in obj]
    elif isinstance(obj, tuple):
        return tuple(convert_numpy_to_python(i) for i in obj)
    elif isinstance(obj, (np.integer, np.int32, np.int64)):
        return int(obj)
    elif isinstance(obj, (np.floating, np.float32, np.float64)):
        return float(obj)
    elif isinstance(obj, np.ndarray):
        return obj.tolist()
    else:
        return obj



@app.get("/data")  # מחזיר את הטסט
async def data():
    dataloader=Tester()
    data=dataloader.run_test()
    return data
    
@app.get("/predict")  # מחזיר את המודל
async def predict():
    return convert_numpy_to_python(summary)

@app.get("/target_variable")  # מחזיק דיקשנרי עמודת מטרה
async def target_variabl():
    return convert_numpy_to_python(variable)




if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)
