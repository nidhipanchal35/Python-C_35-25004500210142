
import CRUD as c1

while True:
    print("\n*** MOVIE WISH LIST MANAGEMENT SYSTEM ***")
    print("1. Add Movie")
    print("2. Display Movies")
    print("3. Update Movie")
    print("4. Delete Movie")
    print("5. Search Movie")
    print("6. Sort Movies by Rating")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")
    print("---------------------------------")

    if choice == "1":
        c1.add()
    elif choice == "2":
        c1.display()
    elif choice == "3":
        c1.updateName()
    elif choice == "4":
        c1.deletebyPID()
    elif choice == "5":
        c1.search()
    elif choice == "6":
        c1.sortByRating()
    elif choice == "7":
        print("Exiting Movie Wish List. Goodbye!")
        break
    else:
        print("Invalid option. Please choose between 1 and 7.")
