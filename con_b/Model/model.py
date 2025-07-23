from DB.db import TestData

class NaiveBayesModel:
    def __init__(self):
        data_loader = TestData()
        self.db = data_loader.get_train_data()

    def target_variable(self):
        last_column = self.db.columns[-1]
        value_counts = self.db[last_column].value_counts()
        return value_counts.to_dict()

    def count_target(self):
        last_column = self.db.columns[-1]
        return self.db[last_column].count()

    def dict_of_summary(self):
        last_column = self.db.columns[-1]
        columns = self.db.columns[:-1]
        res = {}
        for target in self.db[last_column].unique():
            filtered_df = self.db[self.db[last_column] == target]
            inner_dict = {}
            for col in columns:
                value_counts = filtered_df[col].value_counts(normalize=True)
                inner_dict[col] = value_counts.to_dict()
            res[target] = inner_dict  
        return res
