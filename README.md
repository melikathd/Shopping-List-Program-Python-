# Shopping-List-Program-Python-
#(This project is a simple Python program that allows the user to manage a shopping list using a menu system. The user can #add items, remove items, view the list, count the items, and display items that start with the letter "a".)






shopping_list=[]

def add_item():
    item = input("What do you want to add? ")
    shopping_list.append(item)

def remove_item():
    item = input("What do you want to remove? ")
    if item in shopping_list:
        shopping_list.remove(item)
    else:
        print("This item does not exist")

def show_item():
    print("Shopping list:", shopping_list)

def count_item():
    print("Number of items:", len(shopping_list))

def show_item_start_with_a():
    for i in shopping_list:
        if i.startswith("a"):
            print(i)

while True:
    print("\n1. Add item")
    print("2. Remove item")
    print("3. Show items")
    print("4. Count items")
    print("5. Show items starting with 'a'")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_item()
    elif choice == "2":
        remove_item()
    elif choice == "3":
        show_item()
    elif choice == "4":
        count_item()
    elif choice == "5":
        show_item_start_with_a()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
