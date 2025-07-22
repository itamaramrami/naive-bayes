import pandas as pd
from DB.db import TestData

class NaiveBayesClassifier:
    def __init__(self):
        data_loader = TestData()
        
        self.db = data_loader.get_train_data()

    def TargetVariable(self):
        last_column = self.db.columns[-1]
        value_counts = self.db[last_column].value_counts()
        target_variable = value_counts.to_dict()
        return target_variable

    def CountTarget(self):
        last_column = self.db.columns[-1]
        value_counts = self.db[last_column].count()
        return value_counts

    def dictofsummary(self):
        last_column = self.db.columns[-1]
        coloms = self.db.columns[:-1]
        res = {}
        for target in self.db[last_column].unique():
            re_d = self.db[self.db[last_column] == target]
            inner_dict = {}
            for colom in coloms:
                value_counts = re_d[colom].value_counts(normalize=True)
                inner_dict[colom] = value_counts.to_dict()
            res[target] = inner_dict  
        return res

    def predict_from_summary(self, summary, query):
        scores = {}
        target_counts = self.TargetVariable()  
        total_count = sum(target_counts.values())
        priors = {k: v / total_count for k, v in target_counts.items()}

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