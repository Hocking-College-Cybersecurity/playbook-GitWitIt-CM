while True:
        # Questions
    coffee = input("Do you like coffee? (yes/no): ").lower()
    tired = input("Are you tired? (yes/no): ").lower()
    sleep = int(input("How many hours of sleep did you get? "))

        # Decisions
    if tired == "yes" and coffee == "yes":
        print("Drink some coffee to boost your energy!")
    elif tired == "yes" and coffee == "no":
        print("Maybe rest or take a nap instead.")
    elif sleep < 5:
        print("Try to get more sleep tonight.")
    else:
        print("You seem well-rested and ready for the day!")

         # Repeat
    again = input("Try again? (yes/no): ").lower()
    if again != "yes":
        print("Goodbye!")
        break
