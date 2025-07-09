import pandas as pd
from db import *
from dal import *
from menu import *
from test import *


def mein():
    resQuery = menu()
    summary = dictofsummary()
    result, probs = predict_from_summary(summary, resQuery)
    print("result:", result)
    print("percentage:", probs)
   
    # print(test())
    


if __name__ == '__main__':
    mein()