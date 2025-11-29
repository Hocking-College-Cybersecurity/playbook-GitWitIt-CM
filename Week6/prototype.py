
# tuple (fixed categories)
CATEGORIES = ("Food Pantry", "Tutoring", "Cleanup")

# dictionary (tracks entries)
data = {
    "Food Pantry": [],
    "Tutoring": [],
    "Cleanup": []
}


def choose_category():
    """Select a category using a tuple with exception handling."""
    print("\nService Categories:")
    for i, c in enumerate(CATEGORIES, start=1):
        print(f"{i}. {c}")

    while True:
        try:
            choice = int(input("Pick a number: "))
            if choice not in range(1, len(CATEGORIES) + 1):
                raise ValueError("Number out of range.")
            return CATEGORIES[choice - 1]

        except ValueError as e:
            print(f"Invalid input: {e}")
        except Exception:
            print("Unexpected error, try again.")

def add_entry(category):
    """Add a volunteer name to the dictionary with error handling."""
    try:
        name = input("Volunteer name: ").strip()
        if not name:
            raise ValueError("Name cannot be empty.")
        data[category].append(name)
        print("Saved.")
    except ValueError as e:
        print(f"Input error: {e}")
    except KeyError:
        print("Category does not exist.")
    except Exception:
        print("Unexpected error while adding entry.")


# MAIN PROGRAM

def main():
    print("=== Service-Learning Prototype ===")

    while True:
        category = choose_category()
        add_entry(category)

        again = input("Add another? (yes/no): ").lower()
        if again.startswith("n"):
            break

    print("\n=== SUMMARY ===")
    for cat, names in data.items():
        print(f"{cat}: {names}")

    print("\nProgram completed successfully.")

if __name__ == "__main__":
    main()
