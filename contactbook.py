import csv
import os

CSV_FILE = 'contacts.csv'
FIELDNAMES = ['name', 'phone', 'email', 'address']

if not os.path.isfile(CSV_FILE):
    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()


def add_contact(name, phone, email, address):
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writerow({'name': name, 'phone': phone, 'email': email, 'address': address})
    print("Contact added successfully.")


def view_contacts():
    with open(CSV_FILE, mode='r') as file:
        reader = csv.DictReader(file)
        contacts = list(reader)
    if contacts:
        for contact in contacts:
            print(contact)
    else:
        print("No contacts found.")


def update_contact(search_name, new_name=None, new_phone=None, new_email=None, new_address=None):
    updated = False
    with open(CSV_FILE, mode='r') as file:
        contacts = list(csv.DictReader(file))

    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        for contact in contacts:
            if contact['name'] == search_name:
                if new_name:
                    contact['name'] = new_name
                if new_phone:
                    contact['phone'] = new_phone
                if new_email:
                    contact['email'] = new_email
                if new_address:
                    contact['address'] = new_address
                updated = True
            writer.writerow(contact)

    if updated:
        print("Contact updated successfully.")
    else:
        print("Contact not found.")


def delete_contact(search_name):
    deleted = False
    with open(CSV_FILE, mode='r') as file:
        contacts = list(csv.DictReader(file))

    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        for contact in contacts:
            if contact['name'] != search_name:
                writer.writerow(contact)
            else:
                deleted = True

    if deleted:
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")


def search_contact(search_term):
    with open(CSV_FILE, mode='r') as file:
        reader = csv.DictReader(file)
        contacts = [contact for contact in reader if
                    search_term.lower() in contact['name'].lower() or search_term.lower() in contact[
                        'phone'].lower() or search_term.lower() in contact['email'].lower() or search_term.lower() in
                    contact['address'].lower()]

    if contacts:
        for contact in contacts:
            print(contact)
    else:
        print("No matching contacts found.")


def main():
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Search Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            add_contact(name, phone, email, address)
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_name = input("Enter the name of the contact to update: ")
            new_name = input("Enter new name (leave blank to keep unchanged): ")
            new_phone = input("Enter new phone (leave blank to keep unchanged): ")
            new_email = input("Enter new email (leave blank to keep unchanged): ")
            new_address = input("Enter new address (leave blank to keep unchanged): ")
            update_contact(search_name, new_name, new_phone, new_email, new_address)
        elif choice == '4':
            search_name = input("Enter the name of the contact to delete: ")
            delete_contact(search_name)
        elif choice == '5':
            search_term = input("Enter a name, phone, email, or address to search: ")
            search_contact(search_term)
        elif choice == '6':
            print("Exiting the Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
