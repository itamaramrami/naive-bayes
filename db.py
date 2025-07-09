import pandas as pd

df = pd.read_csv(r"C:\Users\IMOE001\Desktop\data\naive bayes\phishing.csv.csv",encoding="utf-8-sig",index_col=0)
db = df.sample(frac=0.7, random_state=42) 
db=db.dropna()
test_db = df.drop(db.index) 