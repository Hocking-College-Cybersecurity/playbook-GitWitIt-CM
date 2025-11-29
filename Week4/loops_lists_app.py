
items = []  #list to store items

while True:     #main menu loop
    print("\n1) Add  2) Show  3) Remove  4) Exit")
    choice = input("Choose 1-4: ")

    if not choice.isdigit():    #input validation
        print("Enter numbers only.")
        continue

    c = int(choice)

    if c == 1:     #add item
        items.append(input("Item to add: "))

    elif c == 2:   #show list
        print("\nList:")
        for i in items: 
            print("-", i)

    elif c == 3:  #remove item
        itm = input("Item to remove: ")
        if itm in items:
            items.remove(itm)
        else:
            print("Not found.")

    elif c == 4:  #exit program
        print("Goodbye!")
        break

    else:
        print("Pick 1-4.")  #input validation for out of range numbers
 