import pandas as pd
from db import *



def TargetVariable():
    last_column = db.columns[-1]
    value_counts = db[last_column].value_counts()
    target_variable = value_counts.to_dict()
    return target_variable
def CountTarget():
    last_column = db.columns[-1]
    value_counts = db[last_column].count()
    return value_counts
    
def dictofsummary():
    last_column = db.columns[-1]
    coloms=db.columns[:-1]
    res={}
    for target in db[last_column].unique():
        re_d=db[db[last_column]==target]
        inner_dict={}
        for colom in coloms:
            value_counts=re_d[colom].value_counts(normalize=True)
            inner_dict[colom]=value_counts.to_dict()
        res[target]=inner_dict    
    return res

def predict_from_summary(summary, query):
    scores = {}
    target_counts = TargetVariable()  
    total_count = sum(target_counts.values())
    priors = {k: v / total_count for k, v in target_counts.items()}
    if query is None:
        print("query is None")
        return
    for target_value in summary:
        prob = priors.get(target_value, 0.0001)
        for feature, feature_value in query.items():
            feature_probs = summary[target_value].get(feature, {})
            value_prob = feature_probs.get(feature_value, 0.0001)  
            prob *= value_prob

        scores[target_value] = prob

    best_target = max(scores, key=scores.get)
    return best_target, scores




# summary = dictofsummary()
# result, probs = predict_from_summary(summary, query)
# print("ניחוש:", result)
# print("הסתברויות:", probs)



