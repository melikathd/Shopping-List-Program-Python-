shoppings_list = []


def add_list():
    item = input("What do you want to add?")
    shoppings_list.append(item)


def remove_list():
    item = input("What do you want to remove?")
    if item in shoppings_list:
        shoppings_list.remove(item)
    else:
        print("this item does not exist")


def show_item():
    print("Shopping List:", shoppings_list)


def count_item():
    print("number of items:", len(shoppings_list))


def show_item_with_a():
    for i in shoppings_list:
        if i.startwith("a"):
            print(i)


while True:
    print("\n1.Add List")
    print("2.Remove List")
    print("3.show All item")
    print("4.Count item")
    print("5.Show items Starting with 'a'")
    print("0.Exit")
    choice = input("Select:")
    if choice == "1":
        add_list()
    elif choice == "2":
        remove_list()
    elif choice == "3":
        show_item()
    elif choice == "4":
        count_item()
    elif choice == "5":
        show_item_with_a()
    elif choice == "0":
        print("Good Bye")
        break
    else:
        print("Invalid option")
