import tkinter as tk
from tkinter import messagebox
import json
import os

class ContactManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")

        self.contacts = self.load_contacts()

        self.name_label = tk.Label(root, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        self.phone_label = tk.Label(root, text="Phone:")
        self.phone_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.phone_entry = tk.Entry(root)
        self.phone_entry.grid(row=1, column=1, padx=5, pady=5)

        self.email_label = tk.Label(root, text="Email:")
        self.email_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.email_entry = tk.Entry(root)
        self.email_entry.grid(row=2, column=1, padx=5, pady=5)

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.view_button.grid(row=4, column=0, columnspan=2, pady=5)

        self.edit_button = tk.Button(root, text="Edit Contact", command=self.edit_contact)
        self.edit_button.grid(row=5, column=0, columnspan=2, pady=5)

        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=6, column=0, columnspan=2, pady=5)

    def load_contacts(self):
        try:
            with open("contacts.json", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_contacts(self):
        with open("contacts.json", "w") as f:
            json.dump(self.contacts, f, indent=4)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()

        if not name or not phone or not email:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        self.contacts.append({"name": name, "phone": phone, "email": email})
        self.save_contacts()
        messagebox.showinfo("Success", "Contact added successfully!")
        self.clear_entries()

    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Info", "No contacts found.")
            return

        contact_list = "\n".join([f"Name: {c['name']}, Phone: {c['phone']}, Email: {c['email']}" for c in self.contacts])
        messagebox.showinfo("Contacts", contact_list)

    def edit_contact(self):
        name = self.name_entry.get()
        if not name:
            messagebox.showerror("Error", "Please enter the name of the contact to edit.")
            return

        for contact in self.contacts:
            if contact["name"] == name:
                phone = self.phone_entry.get()
                email = self.email_entry.get()

                if phone:
                    contact["phone"] = phone
                if email:
                    contact["email"] = email

                self.save_contacts()
                messagebox.showinfo("Success", "Contact updated successfully!")
                self.clear_entries()
                return

        messagebox.showerror("Error", "Contact not found.")

    def delete_contact(self):
        name = self.name_entry.get()
        if not name:
            messagebox.showerror("Error", "Please enter the name of the contact to delete.")
            return

        for contact in self.contacts:
            if contact["name"] == name:
                self.contacts.remove(contact)
                self.save_contacts()
                messagebox.showinfo("Success", "Contact deleted successfully!")
                self.clear_entries()
                return

        messagebox.showerror("Error", "Contact not found.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManager(root)
    root.mainloop()


    