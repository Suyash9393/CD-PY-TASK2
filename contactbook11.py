# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 21:30:38 2024

@author: suyash morye
"""

import sqlite3

def init_db():
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS contacts
                 (id INTEGER PRIMARY KEY, name TEXT, phone TEXT, email TEXT, address TEXT)''')
    conn.commit()
    conn.close()

def add_contact(name, phone, email, address):
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute("INSERT INTO contacts (name, phone, email, address) VALUES (?, ?, ?, ?)",
              (name, phone, email, address))
    conn.commit()
    conn.close()

def view_contacts():
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute("SELECT id, name, phone FROM contacts")
    contacts = c.fetchall()
    conn.close()
    return contacts

def search_contacts(query):
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute("SELECT id, name, phone FROM contacts WHERE name LIKE ? OR phone LIKE ?", 
              ('%' + query + '%', '%' + query + '%'))
    results = c.fetchall()
    conn.close()
    return results

def update_contact(contact_id, name, phone, email, address):
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute("UPDATE contacts SET name = ?, phone = ?, email = ?, address = ? WHERE id = ?",
              (name, phone, email, address, contact_id))
    conn.commit()
    conn.close()

def delete_contact(contact_id):
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
    conn.commit()
    conn.close()

def display_contacts(contacts):
    if contacts:
        for contact in contacts:
            print(f"ID: {contact[0]}, Name: {contact[1]}, Phone: {contact[2]}")
    else:
        print("No contacts found.")

def main():
    init_db()
    
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contacts")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            add_contact(name, phone, email, address)
            print("Contact added successfully.")
        
        elif choice == '2':
            contacts = view_contacts()
            display_contacts(contacts)
        
        elif choice == '3':
            query = input("Enter name or phone to search: ")
            results = search_contacts(query)
            display_contacts(results)
        
        elif choice == '4':
            try:
                contact_id = int(input("Enter contact ID to update: "))
                name = input("Enter new name: ")
                phone = input("Enter new phone: ")
                email = input("Enter new email: ")
                address = input("Enter new address: ")
                update_contact(contact_id, name, phone, email, address)
                print("Contact updated successfully.")
            except ValueError:
                print("Invalid contact ID. Please enter a valid number.")
        
        elif choice == '5':
            try:
                contact_id = int(input("Enter contact ID to delete: "))
                delete_contact(contact_id)
                print("Contact deleted successfully.")
            except ValueError:
                print("Invalid contact ID. Please enter a valid number.")
        
        elif choice == '6':
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()

