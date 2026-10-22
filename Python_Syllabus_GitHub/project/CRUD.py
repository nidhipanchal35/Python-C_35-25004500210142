
movie = []

def add():
    mid = int(input("Enter Movie ID: "))
    mname = input("Enter Movie Name: ")
    genre = input("Enter Movie Genre: ")
    rating = float(input("Enter IMDb Rating: "))
    status = input("Enter Status (To Watch/Watched): ")

    d1 = {
        "MID": mid,
        "MName": mname,
        "Genre": genre,
        "Rating": rating,
        "Status": status
    }

    movie.append(d1)
    print("Movie added to wishlist successfully!")


def display():
    if not movie:
        print("Your movie wishlist is empty.")
        return

    print("\n==============================================")
    print("ID   Movie Name   Genre   Rating   Status")
    print("==============================================")

    for m1 in movie:
        print(m1["MID"], "  ", m1["MName"], "  ",
              m1["Genre"], "  ", m1["Rating"], "  ",
              m1["Status"])


def search():
    mid = int(input("Enter Movie ID to search: "))
    found = 0

    for m1 in movie:
        if m1["MID"] == mid:
            found = 1
            break

    if found == 1:
        print("Movie found!")
        print(m1)
    else:
        print("Movie not found.")


def updateName():
    mid = int(input("Enter Movie ID to update: "))
    found = 0

    for m1 in movie:
        if m1["MID"] == mid:
            found = 1
            break

    if found == 1:
        print("Movie found!")
        print("1. Update Movie Name")
        print("2. Update Genre")
        print("3. Update Rating")
        print("4. Update Status")

        ch = input("Enter your choice: ")

        if ch == "1":
            m1["MName"] = input("Enter New Movie Name: ")
        elif ch == "2":
            m1["Genre"] = input("Enter New Genre: ")
        elif ch == "3":
            m1["Rating"] = float(input("Enter New Rating: "))
        elif ch == "4":
            m1["Status"] = input("Enter New Status: ")
        else:
            print("Invalid choice.")
            return

        print("Movie details updated successfully!")
        print(m1)
    else:
        print("Movie not found.")


def deletebyPID():
    mid = int(input("Enter Movie ID to delete: "))
    found = 0

    for m1 in movie:
        if m1["MID"] == mid:
            movie.remove(m1)
            found = 1
            print("Movie deleted from wishlist successfully!")
            break

    if found == 0:
        print("Movie not found.")


def sortByRating():
    if not movie:
        print("No movies available to sort.")
        return

    movie.sort(key=lambda x: x["Rating"], reverse=True)
    print("Movies sorted by rating successfully!")
    display()
