# db.py

import pandas as pd

class TestData:
    def __init__(self):
        self.df = pd.read_csv(
            r"C:\Users\IMOE001\Desktop\data\naive bayes\phishing.csv.csv",
            encoding="utf-8-sig",
            index_col=0
        )

    def get_train_data(self):
        train = self.df.sample(frac=0.7, random_state=42)
        return train.dropna()

    def get_test_data(self):
        train = self.df.sample(frac=0.7, random_state=42)
        test = self.df.drop(train.index)
        return test.dropna()
