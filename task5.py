contacts = {}

while True:
    print("\n===== CONTACT MANAGEMENT =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. View All Contacts")
    print("6. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter name: ")

        if name in contacts:
            print("Contact already exists")
        else:
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")

            contacts[name] = {
                "phone": phone,
                "email": email,
                "address": address
            }

            print("Contact added successfully")
            
    elif choice == "2":
        name = input("Enter name to search: ")

        if name in contacts:
            print("\nName:", name)
            print("Phone:", contacts[name]["phone"])
            print("Email:", contacts[name]["email"])
            print("Address:", contacts[name]["address"])
        else:
            print("Contact not found")

    elif choice == "3":
        name = input("Enter name to update: ")

        if name in contacts:
            print("Leave blank if no change")

            phone = input("New phone: ")
            email = input("New email: ")
            address = input("New address: ")

            if phone != "":
                contacts[name]["phone"] = phone
            if email != "":
                contacts[name]["email"] = email
            if address != "":
                contacts[name]["address"] = address

            print("Contact updated")
        else:
            print("Contact not found")

    elif choice == "4":
        name = input("Enter name to delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted")
        else:
            print("Contact not found")

    elif choice == "5":
        if contacts == {}:
            print("No contacts saved")
        else:
            print("\n--- All Contacts ---")
            for name, info in contacts.items():
                print("\nName:", name)
                print("Phone:", info["phone"])
                print("Email:", info["email"])
                print("Address:", info["address"])

    elif choice == "6":
        print("Exiting program")
        break

    else:
        print("Invalid choice")
