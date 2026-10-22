"""Practical: 3.11 Inventory System"""

inventory = {"Pen": 10, "Notebook": 4, "Pencil": 20}

def add_item():
    name = input("Product name: ")
    qty = int(input("Quantity to add: "))
    inventory[name] = inventory.get(name, 0) + qty

def remove_item():
    name = input("Product name to remove: ")
    if name in inventory:
        del inventory[name]
    else:
        print("Product not found.")

def update_qty():
    name = input("Product name: ")
    if name in inventory:
        inventory[name] = int(input("New quantity: "))
    else:
        print("Product not found.")

def display_inventory():
    print("\nInventory:")
    for name, qty in sorted(inventory.items()):
        print(f"{name}: {qty}")

def low_stock():
    print("Low-stock items (quantity < 5):")
    for name, qty in sorted(inventory.items()):
        if qty < 5:
            print(f"{name}: {qty}")

while True:
    print("\n1.Add 2.Remove 3.Update quantity 4.Display 5.Low stock 6.Exit")
    choice = input("Choose: ")
    if choice == "1": add_item()
    elif choice == "2": remove_item()
    elif choice == "3": update_qty()
    elif choice == "4": display_inventory()
    elif choice == "5": low_stock()
    elif choice == "6": break
    else: print("Invalid choice.")
