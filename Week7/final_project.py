"""
Volunteer Hours Logger
Author: Cameron McKenzie
Course: CYBR-2101 Python Essentials (Service-Learning)
Date: December 9, 2025

Description:
This program allows community organizations and student groups to
track volunteer hours using a simple command-line interface.
Entries are saved to a CSV file so records persist between uses.

Service-Learning Impact:
The tool reduces reliance on paper logs and manual spreadsheets,
helping small organizations manage volunteer data accurately
while keeping all information stored locally for privacy.
"""

import csv
import os

FILENAME = "volunteers.csv"
FIELDS = ("name", "date", "hours")


def validate_hours(raw_hours):
    """Validate and return hours as a positive float."""
    try:
        hours = float(raw_hours)
        if hours <= 0:
            raise ValueError
        return hours
    except ValueError:
        raise ValueError("Hours must be a positive number.")


def add_entry(name, date, hours):
    """Create a volunteer entry dictionary."""
    return {
        "name": name.strip(),
        "date": date.strip(),
        "hours": hours
    }


def load_entries():
    """Load volunteer records from CSV if it exists."""
    entries = []

    if not os.path.exists(FILENAME):
        return entries

    try:
        with open(FILENAME, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    entries.append({
                        "name": row["name"],
                        "date": row["date"],
                        "hours": float(row["hours"])
                    })
                except (ValueError, KeyError):
                    continue
    except IOError:
        print("Warning: Could not read existing data file.")

    return entries


def save_entry(entry):
    """Save a single volunteer entry to CSV."""
    file_exists = os.path.exists(FILENAME)

    try:
        with open(FILENAME, "a", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDS)
            if not file_exists:
                writer.writeheader()
            writer.writerow(entry)
    except IOError:
        print("Error: Unable to save entry.")


def calculate_totals(entries):
    """Calculate total hours worked by each volunteer."""
    totals = {}
    for entry in entries:
        totals[entry["name"]] = totals.get(entry["name"], 0) + entry["hours"]
    return totals


def display_summary(entries):
    """Display summary of total hours."""
    totals = calculate_totals(entries)
    print("\n=== Volunteer Hours Summary ===")

    if not totals:
        print("No records available.")
        return

    for name, hours in totals.items():
        print(f"{name:<15} {hours:.2f} hours")


def view_individual(entries):
    """Display records for a single volunteer."""
    name = input("Volunteer name: ").strip()
    print(f"\n--- Records for {name} ---")

    found = False
    for entry in entries:
        if entry["name"].lower() == name.lower():
            print(f"{entry['date']} - {entry['hours']:.2f} hours")
            found = True

    if not found:
        print("No records found.")


def main():
    """Main program menu."""
    entries = load_entries()
    print("=== Volunteer Hours Logger ===")

    while True:
        print("\nMenu:")
        print("1. Add volunteer entry")
        print("2. View hours summary")
        print("3. View individual volunteer records")
        print("4. Exit")

        choice = input("Select an option (1–4): ").strip()

        if choice == "1":
            name = input("Volunteer name: ").strip()
            if not name:
                print("Name cannot be empty.")
                continue

            date = input("Date (MM/DD/YYYY): ").strip()
            if not date:
                print("Date cannot be empty.")
                continue

            try:
                hours = validate_hours(input("Hours worked: ").strip())
            except ValueError as error:
                print(error)
                continue

            entry = add_entry(name, date, hours)
            entries.append(entry)
            save_entry(entry)
            print("Entry saved successfully.")

        elif choice == "2":
            display_summary(entries)

        elif choice == "3":
            view_individual(entries)

        elif choice == "4":
            print("Program complete.")
            break

        else:
            print("Invalid selection. Please choose 1–4.")


if __name__ == "__main__":
    main()
