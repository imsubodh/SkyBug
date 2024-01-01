import tkinter as tk
from tkinter import messagebox

contacts = []

def add_contact():
    name = name_var.get()
    phone = phone_var.get()
    email = email_var.get()
    address = address_text.get("1.0", tk.END).strip()

    if name and phone:
        contact = {'Name': name, 'Phone': phone, 'Email': email, 'Address': address}
        contacts.append(contact)
        update_contact_list()
        clear_entries()
    else:
        messagebox.showwarning("Warning", "Please enter name and phone number.")

def update_contact_list():
    contact_listbox.delete(0, tk.END)
    for contact in contacts:
        contact_listbox.insert(tk.END, contact['Name'] + ' - ' + contact['Phone'])

def clear_entries():
    name_var.set('')
    phone_var.set('')
    email_var.set('')
    address_text.delete("1.0", tk.END)

def view_contact():
    try:
        selected_contact_index = contact_listbox.curselection()[0]
        contact_details = contacts[selected_contact_index]
        messagebox.showinfo("Contact Details", f"Name: {contact_details['Name']}\nPhone: {contact_details['Phone']}\nEmail: {contact_details['Email']}\nAddress: {contact_details['Address']}")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a contact.")

def search_contact():
    search_text = search_var.get().lower()
    if search_text:
        search_result = [contact for contact in contacts if search_text in contact['Name'].lower() or search_text in contact['Phone'].lower()]
        if search_result:
            contact_listbox.delete(0, tk.END)
            for contact in search_result:
                contact_listbox.insert(tk.END, contact['Name'] + ' - ' + contact['Phone'])
        else:
            messagebox.showinfo("Search Result", "No matching contacts found.")
    else:
        update_contact_list()

def delete_contact():
    try:
        selected_contact_index = contact_listbox.curselection()[0]
        del contacts[selected_contact_index]
        update_contact_list()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a contact to delete.")

def update_contact():
    try:
        selected_contact_index = contact_listbox.curselection()[0]
        contact = contacts[selected_contact_index]
        contact['Name'] = name_var.get()
        contact['Phone'] = phone_var.get()
        contact['Email'] = email_var.get()
        contact['Address'] = address_text.get("1.0", tk.END).strip()
        update_contact_list()
        clear_entries()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a contact to update.")

root = tk.Tk()
root.title("Contact Book")

# Variables
name_var = tk.StringVar()
phone_var = tk.StringVar()
email_var = tk.StringVar()
search_var = tk.StringVar()

# Frames
entry_frame = tk.Frame(root)
entry_frame.pack()

list_frame = tk.Frame(root)
list_frame.pack()

# Labels and Entries
tk.Label(entry_frame, text="Name:").grid(row=0, column=0)
tk.Entry(entry_frame, textvariable=name_var).grid(row=0, column=1)

tk.Label(entry_frame, text="Phone:").grid(row=1, column=0)
tk.Entry(entry_frame, textvariable=phone_var).grid(row=1, column=1)

tk.Label(entry_frame, text="Email:").grid(row=2, column=0)
tk.Entry(entry_frame, textvariable=email_var).grid(row=2, column=1)

tk.Label(entry_frame, text="Address:").grid(row=3, column=0)
address_text = tk.Text(entry_frame, height=4, width=20)
address_text.grid(row=3, column=1)

# Buttons
tk.Button(entry_frame, text="Add Contact", command=add_contact).grid(row=4, columnspan=2)
tk.Button(entry_frame, text="View Contact", command=view_contact).grid(row=5, columnspan=2)
tk.Button(entry_frame, text="Search Contact", command=search_contact).grid(row=6, columnspan=2)
tk.Button(entry_frame, text="Delete Contact", command=delete_contact).grid(row=7, columnspan=2)
tk.Button(entry_frame, text="Update Contact", command=update_contact).grid(row=8, columnspan=2)

# Search Entry
tk.Entry(entry_frame, textvariable=search_var).grid(row=9, columnspan=2)
tk.Label(entry_frame, text="Search by Name/Phone:").grid(row=10, columnspan=2)

# Contact List
contact_listbox = tk.Listbox(list_frame, width=50, height=15)
contact_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scroll_bar = tk.Scrollbar(list_frame)
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
contact_listbox.config(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=contact_listbox.yview)

root.mainloop()
