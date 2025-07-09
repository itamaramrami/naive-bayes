import pandas as pd
from db import *
from dal import *
from menu import *
from test import *


def mein():
    # resQuery = menu()
    query = {
    "AgeofDomain": "1",
    "Redirecting//": "1",
    "DomainRegLen": "1"
}
    # summary = dictofsummary()
    # summary = dictofsummary()
    # result, probs = predict_from_summary(summary, query)
    # print("result:", result)
    # print("percentage:", probs)
    # print(db.columns)
    print(test())
    


if __name__ == '__main__':
    mein()