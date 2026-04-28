# Contact Management System
#Aditya M Pandaw

import json
import re
from datetime import datetime

contacts = {}

def validate_phone(phone):
    digits = re.sub(r'\D', '', phone)
    if 10 <= len(digits) <= 15:
        return True, digits
    return False, None

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def add_contact():
    print("\n--- ADD NEW CONTACT ---")

    name = input("Enter contact name: ")

    phone = input("Enter phone number: ")
    valid, phone = validate_phone(phone)

    email = input("Enter email (optional, press Enter to skip): ")
    address = input("Enter address (optional): ")
    group = input("Enter group (Friends/Work/Family/Other): ") or "Other"

    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address,
        "group": group,
        "created": datetime.now().isoformat()
    }

    print(f"✅ Contact '{name}' added successfully!")

def view_contacts():
    print("\n--- ALL CONTACTS ---")
    for name, info in contacts.items():
        print(name)
        print("📞", info["phone"])
        print("📧", info["email"])
        print("👥", info["group"])
        print("-" * 30)

def search_contact():
    term = input("Enter name to search: ").lower()

    print("\nFound contact(s):")
    for name, info in contacts.items():
        if term in name.lower():
            print(name)
            print("📞", info["phone"])
            print("📧", info["email"])
            print("📍", info["address"])
            print("👥", info["group"])

def save_json():
    try:
        with open("contacts_data.json", "w") as f:
            json.dump(contacts, f, indent=4)
        print("💾 Contacts saved to contacts_data.json")
    except Exception as e:
        print("Error saving file:", e)

def stats():
    print("\n--- CONTACT STATISTICS ---")
    print("Total Contacts:", len(contacts))

    group_count = {}
    for c in contacts.values():
        g = c["group"]
        group_count[g] = group_count.get(g, 0) + 1

    print("\nContacts by Group:")
    for g, count in group_count.items():
        print(g, ":", count)

def menu():
    while True:
        print("\n========== CONTACT MANAGEMENT SYSTEM ==========")
        print("1. Add New Contact")
        print("2. Search Contact")
        print("3. View All Contacts")
        print("4. View Statistics")
        print("5. Save to JSON")
        print("6. Exit")

        ch = input("Enter your choice: ")

        if ch == '1':
            add_contact()
        elif ch == '2':
            search_contact()
        elif ch == '3':
            view_contacts()
        elif ch == '4':
            stats()
        elif ch == '5':
            save_json()
        elif ch == '6':
            print("Thank you for using Contact Management System")
            break
        else:
            print("Invalid choice")

menu()