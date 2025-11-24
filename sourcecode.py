#GROCERY STORE MANAGEMENT SYSTEM 
import os
MY_STORE= "grocery_data.txt"

# Add item
def add_item():
    name = input("Enter item name: ").lower()
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    f = open(MY_STORE, "a")
    f.write(f"{name},{price},{quantity}\n")
    f.close()
    print("Item added successfully!\n")

# Display all items
def display_items():
    if not os.path.exists(MY_STORE):
        print("No item found!\n")
        return

    print("\n--- GROCERY ITEMS ---")
    
    f = open(MY_STORE, "r")
    data = f.readlines()
    f.close()

    for things in data:
        things = things.strip()
        parts = things.split(",")
        if len(parts) != 3:
            continue
        name, price, quantity = parts
        print(f"Name: {name.capitalize()}, Price: ₹{price}, Quantity: {quantity}")
    

#Searching an item
def search_item():
    search = input("Enter item name to search: ").lower()

    f = open(MY_STORE, "r")
    data = f.readlines()
    f.close()

    found = False
    for things in data:
        parts = things.strip().split(",")
        if len(parts) != 3:
            continue

        name, price, quantity = parts

        if name == search:
            print(f"Found! Name: {name.capitalize()}, Price: ₹{price}, Qty: {quantity}\n")
            found = True

    if not found:
        print("Item not found!\n")

#Update item
def update_item():
    search = input("Enter item name to update: ").lower()

    f = open(MY_STORE, "r")
    data = f.readlines()
    f.close()

    new_data = []
    found = False

    for things in data:
        parts = things.strip().split(",")
        if len(parts) != 3:
            continue
        name, price, quantity = parts

        if name == search:
            print("Which item do you want to update?")
            print("1. Price of the product")
            print("2. Quantity")
            choice = input("Enter your choice: ")

            if choice == "1":
                price = input("Enter new price: ")
            elif choice == "2":
                quantity = input("Enter new quantity: ")
            else:
                print("Invalid choice!")

            print("Item updated successfully!")
            found = True

        new_data.append(f"{name},{price},{quantity}\n")

    f = open(MY_STORE, "w")
    f.writelines(new_data)
    f.close()

    if not found:
        print("Item not found!\n")

# Delete item
def delete_item():
    search = input("Enter item to delete: ").lower()

    f = open(MY_STORE, "r")
    lines = f.readlines()
    f.close()

    f = open(MY_STORE, "w")
    found = False

    for line in lines:
        if line.split(",")[0].lower() != search:
            f.write(line)
        else:
            found = True

    f.close()

    if found:
        print("Item deleted!\n")
    else:
        print("Item not found!\n")


# purchasing an item
def billing():
    total = 0

    while True:
        item = input("Enter item (or 'done'): ").lower()
        if item == "done":
            break

        qty = int(input("Enter quantity: "))

        found = False
        f=open(MY_STORE, "r")
        for things in f:
                name, price, stock = things.strip().split(",")
                if name.lower() == item:
                    found = True
                    if int(stock) >= qty:
                        cost = float(price) * qty
                        total += cost
                        print(f"Added {item} x{qty} - ₹{cost}")
                    else:
                        print("Not enough stock!")
                    break

        if not found:
            print("Item not found!")

    print(f"\nTOTAL BILL = ₹{total}\n")


# Menu
while True:
    print("\n======= GROCERY STORE MANAGEMENT SYSTEM=======")
    print("1. Add Item")
    print("2. Display Item")
    print("3. Search Item")
    print("4. Update Item")
    print("5. Delete Item")
    print("6. Purchase Item")
    print("7. Exit")

    user_choice = input("Enter your choice:- ")

    if user_choice == "1":
        add_item()
    elif user_choice == "2":
        display_items()
    elif user_choice == "3":
        search_item()
    elif user_choice == "4":
        update_item()
    elif user_choice == "5":
        delete_item()
    elif user_choice == "6":
        billing()
    elif user_choice == "7":
        print("Exiting the program..... Thank you!")
        break
    else:
        print("Invalid choice!\nPlease enter accurate choice")
