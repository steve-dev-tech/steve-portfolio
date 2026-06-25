import json

FILE_NAME = "contacts.json"


def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return {"contacts": []}


def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


def add_contact():
    
    data = load_data()

    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    data["contacts"].append(contact)

    save_data(data)

    print("Contact added successfully.")


def view_contacts():
    
    data = load_data()

    print("\n----- CONTACTS -----")

    for index, contact in enumerate(data["contacts"], start=1):

        print(
            f'{index}. Name: {contact["name"]} | '
            f'Phone: {contact["phone"]} | '
            f'Email: {contact["email"]}'
        )


def search_contact():
    
    data = load_data()

    name = input("Enter contact name: ")

    found = False

    for contact in data["contacts"]:

        if name.lower() in contact["name"].lower():

            print(
                f'Name: {contact["name"]} | '
                f'Phone: {contact["phone"]} | '
                f'Email: {contact["email"]}'
            )

            found = True

    if not found:
        print("Contact not found.")


def delete_contact():
    
    data = load_data()

    if len(data["contacts"]) == 0:
        print("No contacts found.")
        return

    print("\n----- CONTACTS -----")

    for index, contact in enumerate(data["contacts"], start=1):

        print(
            f'{index}. {contact["name"]} | '
            f'{contact["phone"]}'
        )

    try:
        choice = int(input("Enter contact number to delete: "))

        deleted = data["contacts"].pop(choice - 1)

        save_data(data)

        print(f'Deleted: {deleted["name"]}')

    except:
        print("Invalid choice.")


def menu():

    while True:

        print("\n--- CONTACT MANAGER ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_contact()

        elif choice == "2":
            view_contacts()

        elif choice == "3":
            search_contact()

        elif choice == "4":
            delete_contact()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option")


menu()