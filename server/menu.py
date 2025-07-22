import pandas as pd
from DB.db import TestData
from logger.logger import Logger


class menu:
    def __init__(self):
        self.data_loader = TestData()
        self.db = self.data_loader.get_train_data()
        self.columns = self.db.columns.tolist()
        self.query = {}
        self.used_columns = set()

    def display_available_columns(self):
        print("\n--- Available columns ---")
        for i, col in enumerate(self.columns):
            if col not in self.used_columns:
                print(f"{i}. {col}")

    def display_column_values(self, column_name):
        unique_values = self.db[column_name].dropna().unique().tolist()
        print(f"\n--- Column values for '{column_name}' ---")
        for i, val in enumerate(unique_values):
            print(f"{i}. {val}")
        return unique_values

    def build_query(self):
        while True:
            self.display_available_columns()

            user_input = input("Select a column number or type 'exit' to exit: ").strip()
            if user_input.lower() == 'exit':
                break

            if not user_input.isdigit() or int(user_input) >= len(self.columns):
                print("Invalid selection, try again.")
                continue

            col_index = int(user_input)
            column_name = self.columns[col_index]

            if column_name in self.used_columns:
                print("You have already selected this column.")
                continue

            unique_values = self.display_column_values(column_name)
            val_input = input("Select a value: ").strip()

            if not val_input.isdigit() or int(val_input) >= len(unique_values):
                print("Invalid selection")
                continue

            selected_value = unique_values[int(val_input)]
            self.query[column_name] = selected_value
            self.used_columns.add(column_name)

            if len(self.used_columns) == len(self.columns):
                print("You selected all columns.")
                break
        Logger.log(f"Query: {self.query}")
        return self.query
