# This is a simple contact book app, where you can create, view, update, delete, search, and count contacts.

contacts = {}

while True:
    print("\nContact book app.")
    print("1. Create contact")
    print("2. View contact")
    print("3. Update contact")
    print("4. Delete contact")
    print("5. Search contact")
    print("6. Count contacts")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter your name: ")
        if name in contacts:
            print(f"The contact {name} already exists.")
        else:
            age = input("Enter your age: ")
            email = input("Enter email ID: ")
            mobile = input("Enter mobile number: ")
            contacts[name] = {'age': int(age), 'email': email, 'mobile': mobile}
            print(f"Contact {name} has been created successfully.")

    elif choice == 2:
        name = input("Enter the name: ")
        if name in contacts:
            contact = contacts[name]
            print(f"Name: {name}, Age: {contact['age']}, Email: {contact['email']}, Mobile: {contact['mobile']}")
        else:
            print("Contact not found.")

    elif choice == 3:
        name = input("Enter the name to update: ")
        if name in contacts:
            age = input("Enter updated age: ")
            email = input("Enter updated email ID: ")
            mobile = input("Enter updated mobile number: ")
            contacts[name] = {'age': int(age), 'email': email, 'mobile': mobile}
            print(f"Contact {name} has been updated successfully.")
        else:
            print("Contact not found.")

    elif choice == 4:
        name = input("Enter the name to delete: ")
        if name in contacts:
            del contacts[name]
            print(f"Contact {name} has been deleted successfully.")
        else:
            print("Contact not found.")

    elif choice == 5:
        search_name = input("Input contact name to search: ")
        found = False
        for name, contact in contacts.items():
            if search_name.lower() in name.lower():
                print(f"Found - Name: {name}, Age: {contact['age']}, Email: {contact['email']}, Mobile: {contact['mobile']}")
                found = True
        if not found:
            print("No contact found with that name.")

    elif choice == 6:
        print(f"Total contacts in your contact book: {len(contacts)}")

    elif choice == 7:
        print("Thank you for using the contact book program.")
        break

    else:
        print("Invalid input.")
