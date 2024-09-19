import json
import os

class ContactManager:
    file_path = 'contacts_store.json'
    
    def __init__(self):
        self.contacts = {}
        self.load()
        self.menu()

    def load(self):
        """Load contacts from the JSON file."""
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as f:
                self.contacts = json.load(f)
        else:
            self.contacts = {}

    def save_contacts(self):
        """Save contacts to the JSON file."""
        with open(self.file_path, 'w') as f:
            json.dump(self.contacts, f, indent=4)
        print("Contacts saved to file.")

    def menu(self):
        """Display the menu and handle user choices."""
        while True:
            print("\nContact Management System")
            print("1. Add a new contact")
            print("2. View all contacts")
            print("3. Edit an existing contact")
            print("4. Delete a contact")
            print("5. Exit")
            user_choice = input("Select the option (1-5): ")
            if user_choice == '1':
                self.new_contact()
            elif user_choice == '2':
                self.view()
            elif user_choice == '3':
                self.edit()
            elif user_choice == '4':
                self.delete()
            elif user_choice == '5':
                print("Exiting the program...")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

    def new_contact(self):
        """Add a new contact."""
        name = input("Enter the contact's name: ")
        mobile = input("Enter the contact's phone number: ")
        email = input("Enter the contact's email address: ")
    
        if name in self.contacts:
            print("Contact already exists. Use the edit option to modify it.")
        else:
            self.contacts[name] = {"mobile no": mobile, "email": email}
            self.save_contacts()
            print("Contact added successfully.")


    def view(self):
        """Display all contacts."""
        if self.contacts:
            for name, info in self.contacts.items():
                print(f"Name: {name}")
                print(f"Mobile no: {info['mobile no']}")
                print(f"Email: {info['email']}\n")
        else:
            print("No contacts found.")

    def edit(self):
        """Edit an existing contact."""
        name = input("Enter the name of the contact to edit: ")
    
        if name in self.contacts:
            mobile = input("Enter the new phone number: ")
            email = input("Enter the new email address: ")
            self.contacts[name] = {"mobile no": mobile, "email": email}
            self.save_contacts()
            print("Contact updated successfully.")
        else:
            print("Contact not found.")


    def delete(self):
        """Delete a contact."""
        name = input("Enter the name of the contact to delete: ")
        
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

h=ContactManager()
