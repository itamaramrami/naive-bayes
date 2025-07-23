import pandas as pd
from DB.db import TestData
from Test.test import Tester
from server.MenuRender import SimpleRunner
from Model.model import NaiveBayesModel

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