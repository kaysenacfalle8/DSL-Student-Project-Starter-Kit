"""
functions.py
Write your functions here.
Each function should do one specific task.
The features below are just for example, replace them with your own project features.
"""

import os

DATA_FILE = "data/data.txt"

def feature_one():
    """Example: Save a user input to a file"""
    user_input = input("Type something to save: ")
    with open(DATA_FILE, "a") as file:
        file.write(user_input + "\n")
    print("✅ Saved successfully!")

def feature_two():
    """Example: Display stored data"""
    if not os.path.exists(DATA_FILE):
        print("No data found yet.")
        return

    with open(DATA_FILE, "r") as file:
        print("\n--- Stored Data ---")
        print(file.read())
