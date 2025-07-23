
from server.menu import menu  
from Model.model import NaiveBayesModel
class SimpleRunner:
    def __init__(self):
        self.menu_instance = menu()
        self.Naive = NaiveBayesModel()
        self.summary = self.Naive.dictofsummary()
        self.query = self.menu_instance.build_query()
        
        self.run_prediction()

    def run_prediction(self):
        if not self.query:
            print("לא הוזנה שאילתה. הפסקת תהליך.")
            return

        result, probs = self.Naive.predict_from_summary(self.summary, self.query)
        print("\n probability: ", result)
        print("percentage:")
        for k, v in probs.items():
            print(f"{k}: {v:.4f}")