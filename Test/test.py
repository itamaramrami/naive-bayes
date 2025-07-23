import pandas as pd
from DB.db import TestData
from Model.model import NaiveBayesModel
from Classifie.classifie import NaiveBayesPredictor

class Tester:
    def __init__(self):
        self.data_loader = TestData()
        self.test_db = self.data_loader.get_test_data()
        self.classifier = NaiveBayesModel()
        self.predictor = NaiveBayesPredictor(self.classifier)
        self.summary = self.classifier.dict_of_summary()      
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

            if prediction == actual:
                res["yes"] += 1
            else:
                res["no"] += 1
                if verbose:
                    print(f"תיזחת: {prediction} | תמא: {actual}")

        total = res["yes"] + res["no"]
        accuracy = res["yes"] / total * 100 if total > 0 else 0
        if verbose:
            print(res)
            print(f"קויד זוחא: {accuracy:.2f}%")
        res["accuracy"] = accuracy
        return res
