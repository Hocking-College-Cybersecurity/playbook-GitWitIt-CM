"""
Volunteer Hours Logger
Author: Cameron McKenzie
Course: CYBR-2101 Python Essentials (Service-Learning)
Date: December 12, 2025

Description:
This program provides a command-line tool for tracking volunteer hours
for student groups and community organizations. Entries are stored in a
local CSV file to ensure persistence across sessions.

Service-Learning Impact:
This tool reduces reliance on paper logs and manual spreadsheets,
helping small organizations manage volunteer data accurately while
keeping all records stored locally to support privacy and accessibility.
"""


import csv
import os
from datetime import datetime

FILE_NAME = "volunteers.csv"


def initialize_file():
    """Create the CSV file with headers if it does not exist."""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Hours", "Date"])


def add_entry():
    """Add a new volunteer hours entry."""
    name = input("Enter volunteer name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    try:
        hours = float(input("Enter hours worked: "))
        if hours <= 0:
            print("Hours must be greater than zero.")
            return
    except ValueError:
        print("Invalid input. Hours must be a number.")
        return

    date = datetime.now().strftime("%Y-%m-%d")

    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, hours, date])

    print("Entry added successfully.")


def view_entries():
    """Display all logged volunteer entries."""
    if not os.path.exists(FILE_NAME):
        print("No entries found.")
        return

    with open(FILE_NAME, mode="r") as file:
        reader = csv.reader(file)
        next(reader, None)  # Skip header

        print("\nVolunteer Hours Log:")
        for row in reader:
            print(f"Name: {row[0]} | Hours: {row[1]} | Date: {row[2]}")
        print()


def main_menu():
    """Main program loop."""
    initialize_file()

    while True:
        print("\nVolunteer Hours Logger")
        print("1. Add volunteer entry")
        print("2. View all entries")
        print("3. Exit")

        choice = input("Select an option (1-3): ").strip()

        if choice == "1":
            add_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid selection. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main_menu()
