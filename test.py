import pandas as pd
from db import *
from dal import *

def dictOfTest():
    listoftest=test_db.to_dict(orient='records')
    return listoftest


def test():
    res = {"yes": 0, "no": 0}
    lisTtest = dictOfTest()
    target_col = test_db.columns[-1]
    summary = dictofsummary()

    for row in lisTtest:
        actual = row[target_col]
        query = row.copy()
        del query[target_col]
        prediction, scores = predict_from_summary(summary, query)

        if prediction == actual:
            res["yes"] += 1
        else:
            res["no"] += 1
            print(f"תיזחת: {prediction} | תמא: {actual} ")
    

    accuracy = res["yes"] / (res["yes"] + res["no"]) * 100
    print(f" קויד זוחא: {accuracy:.2f}%")
    return res

        
    