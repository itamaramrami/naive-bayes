import pandas as pd
from DB.db import TestData
from test.test import Tester
from server.MenuRender import SimpleRunner
from conntrolers.dal import NaiveBayesClassifier

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