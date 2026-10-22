"""Practical: 3.5 Phone Book"""

phone_book = {
    "Aarav": "9876500001",
    "Nidhi": "9876500002",
    "Riya": "9876500003",
    "Dev": "9876500004",
    "Mira": "9876500005",
}
phone_book["Kabir"] = input("Add Kabir's phone number: ")
name = input("Search contact name: ")
print("Number:", phone_book.get(name, "Contact not found"))
update_name = input("Which contact number should be updated? ")
if update_name in phone_book:
    phone_book[update_name] = input("Enter new number: ")
delete_name = input("Which contact should be deleted? ")
if delete_name in phone_book:
    del phone_book[delete_name]
print("\nPhone book (sorted by name):")
for name in sorted(phone_book):
    print(f"{name}: {phone_book[name]}")
