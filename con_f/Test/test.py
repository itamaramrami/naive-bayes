import pandas as pd
import requests
from Classifie.classifie import NaiveBayesPredictor
response_data = requests.get("http://model:81/data")
response = requests.get("http://model:81/predict")
summaryy = response.json()
class Tester:
    def __init__(self):
        self.test_db = pd.DataFrame(response_data.json())
        self.predictor = NaiveBayesPredictor()
        self.summary = summaryy     
        self.target_col = self.test_db.columns[-1]

    def dict_of_test(self):
        return self.test_db.to_dict(orient='records')


    def run_test(self, verbose: bool = False):
        res = {"yes": 0, "no": 0}
        test_records = self.dict_of_test()

        for row in test_records:
            actual = row[self.target_col]
            query = row.copy()
            del query[self.target_col]

            prediction, scores = self.predictor.predict_from_summary(self.summary, query)
            print("prediction and actual")
            print(type(prediction))
            print(type(actual))
            
            if str(prediction).strip() == str(actual).strip():
                res["yes"] += 1
            else:
                res["no"] += 1
                print(f"תיזחת: {prediction} | תמא: {actual}")

        total = res["yes"] + res["no"]
        accuracy = res["yes"] / total * 100 if total > 0 else 0
        if verbose:
            print(res)
            print(f"קויד זוחא: {accuracy:.2f}%")
        res["accuracy"] = accuracy
        return res
