# class ContactBook:
#     def __init__(self, name, number) -> None:
#         self.name = name
#         self.number = number
        

#     contact_list = {}
#     def add_contact(self, name, number):
        

import json

contacts = {}
while True:
    print("\n1. Add Contact: ")
    print("2. View Contacts: ")
    print("3. Search Contacts: ")
    print("4. Delete Contact: ")
    print("5. Bulk Add Contacts: ")
    print("6. Bulk Delete Contacts: ")
    print("7. Save to json and Exit: ")
    choice = input("Enter a number of your choice: ")
    
    if choice=="1": # Add contact
        name = input("Enter Name: ").strip()
        phone = input("Enter the phone number: ").strip()

        if not name or not phone:
            print("Name and phone number cannot be empty.")
            continue
        if name in contacts:
            print("Contact already exists.")
        contacts[name] = phone
        print("Contact added. ")
    
    elif choice=="2": # Show contact
        if not contacts:
            print("No contacts found.")
        else:
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
    
    elif choice=="3":  # Search contact
        search_name = input("Enter the name to search").strip()
        print(contacts.get(search_name, "Contact Not Found"))

    elif choice=="4": # Delete contact
        delete_name = input("Enter the name to delete contact.").strip()
        if delete_name in contacts:
            del contacts[delete_name]
            print("Contact deleted.")
        else:
            print("Contact not found.")

    elif choice=="5": # Bulk add contacts
        bulk_contacts = input("Enter contacts in the format 'Name:Phone, Name:Phone,...'").strip()
        for item in bulk_contacts.split(","):
            try:
                name, phone = item.split(":")
                name, phone = name.strip(), phone.strip()
                if not name or not phone:
                    print(f"Invalid entry '{item}'. Name and phone number cannot be empty.")
                    continue
                if name in contacts:
                    print(f"Contact '{name}' already exists. Skipping.")
                    continue
                contacts[name] = phone
            except ValueError:
                print(f"Invalid format for entry '{item}'. Skipping.")
        print("Bulk contacts added.")

    elif choice=="6": # Bulk delete contacts
        bulk_delete = input("Enter names to delete in the format 'Name, Name,...'").strip()
        for name in bulk_delete.split(","):
            name = name.strip()
            if name in contacts:
                del contacts[name]
                print(f"Contact '{name}' deleted.")
            else:
                print(f"Contact '{name}' not found. Skipping.")

    elif choice=="7": # Save to json and exit
        print("Exiting the contact book. Goodbye!")
        json.dump(contacts, open("contacts.json", "w"), indent=4)
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

