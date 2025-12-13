# Return a person's age from a dictionary
def get_age(people_dict, name):
    return people_dict.get(name, "Not found")


# Add a person and age to the dictionary
def add_person(people_dict, name, age):
    people_dict[name] = age
    return people_dict


# Format a person's info as text
def format_person(name, age):
    return f"Name: {name}, Age: {age}"



# Calculate the average age in the dictionary
def average_age(people_dict):
    total = sum(people_dict.values())
    count = len(people_dict)
    return total / count


# Main program
def main():

    people = {
        "Timmy": 14,
        "Tommy": 9,
        "Johnny": 17
    }

    print("Timmy's age:", get_age(people, "Timmy"))

    people = add_person(people, "Samantha", 21)

    print(format_person("Samantha", 21))

    print("Average age:", average_age(people))

    print("Updated dictionary:", people)



if __name__ == "__main__":
    main()
