import pandas as pd
from db import *
from dal import *



def menu():
    query = {}
    used_columns = set()

    while True:
        print("\n---Available columns:---")
        columns = db.columns.tolist()
        for i, col in enumerate(columns):
            if col not in used_columns:
                print(f"{i}. {col}")

        user_input = input("Select a column number or exit to exit. ").strip()
        if user_input.lower() == 'exit':
            break

        if not user_input.isdigit() or int(user_input) >= len(columns):
            print("Invalid selection, try again.")
            continue

        col_index = int(user_input)
        column_name = columns[col_index]

        if column_name in used_columns:
            print("You have already selected this column.")
            continue

        unique_values = db[column_name].dropna().unique().tolist()
        print(f"\n---Column values: '{column_name}' ---")
        for i, val in enumerate(unique_values):
            print(f"{i}. {val}")

        val_input = input("Select a value ").strip()
        if not val_input.isdigit() or int(val_input) >= len(unique_values):
            print("Invalid selection")
            continue

        value = unique_values[int(val_input)]
        query[column_name] = value
        used_columns.add(column_name)

        if len(used_columns) == len(columns):
            print("You selected all columns.")
            break

    return query
