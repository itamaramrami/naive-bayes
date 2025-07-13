import pandas as pd
from db import TestData
from test import Tester
from MenuRender import SimpleRunner
from dal import NaiveBayesClassifier

def mein():
    # resQuery = menu()
    # summary = dictofsummary()
    # result, probs = predict_from_summary(summary, resQuery)
    # print("result:", result)
    # print("percentage:", probs)
   
    # test=Tester()
    # test.run_test()
    
    SimpleRunner()

if __name__ == '__main__':
    
    mein()