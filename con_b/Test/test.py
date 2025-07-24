import pandas as pd
from Model.model import NaiveBayesModel
from DB.db import TestData

class Tester:
    def __init__(self):
        self.data_loader = TestData()
        self.test_db = self.data_loader.get_test_data()
        self.predictor = NaiveBayesModel()
        self.summary = self.predictor.dict_of_summary()   
        self.target_col = self.test_db.columns[-1]

    def dict_of_test(self):
        return self.test_db.to_dict(orient='records')

    def predict_from_summary(self, summary, query):
        scores = {}
        total_count = sum(self.predictor.target_variable().values())
        priors = {k: v / total_count for k, v in self.predictor.target_variable().items()}

        if query is None:
            print("query is None")
            return

        fixed_query = {}
        for feature, feature_value in query.items():
            try:
                fixed_value = int(feature_value)
            except ValueError:
                try:
                    fixed_value = float(feature_value)
                except ValueError:
                    fixed_value = feature_value
            fixed_query[feature] = fixed_value

        for target_value in summary:
            prob = priors.get(target_value, 0.0001)
            for feature, feature_value in fixed_query.items():
                feature_probs = summary[target_value].get(feature, {})
                value_prob = feature_probs.get(feature_value, 0.0001)  
                prob *= value_prob

            scores[target_value] = prob
        best_target = max(scores, key=scores.get)

        return best_target, scores
    
    def run_test(self, verbose: bool = False):
        
        res = {"yes": 0, "no": 0}
        test_records = self.dict_of_test()

        for row in test_records:
            actual = row[self.target_col]
            query = row.copy()
            del query[self.target_col]

            prediction, scores = self.predict_from_summary(self.summary, query)
            
            
            if int(str(prediction).strip()) == int(str(actual).strip()):

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
