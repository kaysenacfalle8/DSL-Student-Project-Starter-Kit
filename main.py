"""
Project Title: ______________________
Student Name: ______________________
Date: ______________________
Description:
    Briefly describe what your project does.
"""

from functions import *

def main():
    print("\nWelcome to [Your Project Name Here]!")

    while True:
        print("\n--- Main Menu ---")
        print("1. Option 1")
        print("2. Option 2")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            feature_one()
        elif choice == "2":
            feature_two()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
