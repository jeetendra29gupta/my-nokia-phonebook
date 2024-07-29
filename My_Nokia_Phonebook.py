contacts = {}


def add_contact(name, phone):
    if name in contacts:
        return "Contact already exists."
    contacts[name] = phone
    return f"Contact {name} added."


def search_contact(name):
    if name in contacts:
        return f"Phone number of {name} is {contacts[name]}."
    return "Contact not found."


def delete_contact(name):
    if name in contacts:
        del contacts[name]
        return f"Contact {name} deleted."
    return "Contact not found."


def list_contacts():
    if contacts:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    return "Phonebook is empty."


def display_menu():
    print("\nPhonebook Application")
    print("1. Add a New Contact")
    print("2. Search for a Contact")
    print("3. Delete a Contact")
    print("4. List All Contacts")
    print("5. Exit")


def main():
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ")

        if choice == '5':
            print("Exiting the application.")
            break

        elif choice == '4':
            print(list_contacts())

        elif choice == '3':
            name = input("Enter the contact name to delete: ")
            print(delete_contact(name))

        elif choice == '2':
            name = input("Enter the contact name to search: ")
            print(search_contact(name))

        elif choice == '1':
            name = input("Enter the contact name: ")
            phone = input("Enter the phone number: ")
            print(add_contact(name, phone))

        elif choice not in ['1', '2', '3', '4']:
            print("Invalid choice, please select a valid option.")
        else:
            print("Invalid choice, please select a valid option.")


if __name__ == '__main__':
    print("Phonebook Contacts:")
    main()
