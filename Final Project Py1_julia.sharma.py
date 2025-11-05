inventory = []

#define functions
def add_item():
    try:
        #prompt user to enter item information
        name = input("Enter item name: ").strip()
        price = float(input("Enter item price: "))
        quantity = int(input("Enter item quantity: "))
        category = input("Enter item category: ").strip()

        #check if item already exists
        for item in inventory:
            if item['name'].lower() == name.lower():
                print("Item already exists. Use update_item to modify it.")
                return
        #create a dictionary
        item = {
            "name": name,
            "price": price,
            "quantity": quantity,
            "category": category
        }
        #adds item to inventory
        inventory.append(item)
        print(f"✅ Item '{name}' added successfully.")
    except ValueError:
        print("❌ Invalid input. Please enter correct data types.")

def update_item():
    try:
        name = input("Enter name of item you wish to update: ").strip()
        #loop to search through items in inventory
        for item in inventory:
            if item['name'].lower() == name.lower():
                #if name is found, prompt for updated information
                updated_price = float(input("Enter updated price: "))
                updated_quantity = int(input("Enter updated quantity: "))
                updated_category = input("Enter updated category: ").strip()

                #update dictionary
                item["price"] = updated_price
                item["quantity"] = updated_quantity
                item["category"] = updated_category

                print(f"✅ Item '{name}' updated successfully.")
                return
        #if name is not found
        print(f"❌ Item '{name}' not found in inventory.")
    except ValueError:
        print("❌ Invalid input. Please enter correct data types.")

def view_inventory():
    #if inventory does not have items
    if not inventory:
        print("Inventory is empty.")
        return
    #Display items in inventory
    for item in inventory:
        print(f"Name: {item['name']}")
        print(f"Price: ${item['price']:.2f}")
        print(f"Quantity: {item['quantity']}")
        print(f"Category: {item['category']}")
        print("*"*30)

def remove_item():
    try:
        name = input("Enter name of item you wish to remove: ").strip()
        #loop to search through items in inventory
        for item in inventory:
            if item['name'].lower() == name.lower():
                #if name is found, remove item
                inventory.remove(item)
                print(f"✅ Item '{name}' removed successfully.")
                return

        # if name is not found
        print(f"❌ Item '{name}' not found in inventory.")
    except ValueError:
        print("❌ Invalid input. Please enter correct data type.")

def search_by_category():
    try:
        category = input("Enter category you wish to view: ").strip()
        found = False

        print(f"Items in category '{category}':")
        for item in inventory:
            if item['category'].lower() == category.lower():
                print(f"-{item['name']} (Price: ${item['price']:.2f}, Quantity: {item['quantity']})")
                found = True

        if not found:
                print(f"❌ Category '{category}' not found in inventory.")
            
    except ValueError:
        print("❌ Invalid input. Please enter correct data type.")


        #establish main menu
def main():
    while True:
        print("\n====== 🛒 Market Inventory Menu 🛒====== ")
        print("1. Add Item")
        print("2. Update Item")
        print("3. View Inventory")
        print("4. Remove Item")
        print("5. Search by Category")
        print("6. Exit")
        print() #adds a space before user input

        choice = input("Choose an option (1-6): ").strip()
        print()

        if choice == '1':
            add_item()
        elif choice == '2':
            update_item()
        elif choice == '3':
            view_inventory()
        elif choice == '4':
            remove_item()
        elif choice== '5':
            search_by_category()
        elif choice == '6':
            print("Thanks for using Market Inventory. Goodbye!")
            exit()
        else:
            print("Invalid Option. Please enter a number between 1 and 6")
if __name__ == "__main__":
    main()