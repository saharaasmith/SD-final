'''
This program is for bookstores so that customers are able to borrow or purchase books. They are allowed to see their profile and
see information about the books.
'''
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random         # imports random books
bookList = ("The Giver", "Cat in the Hat", "Animal Farm")   # Books that are imported

# Picture
book_image = Image.open("book.png")
book_image = book_image.resize(50, 50)
book_photo = ImageTk.PhotoImage(book_image)

profile_image = Image.open("profile.png")
profile_image = profile_image.resize(50, 50)
profile_photo = ImageTk.PhotoImage(profile_image)

root = tk.Tk()
root.title("Flip and Find")
root.geometry("800x600")

entry = tk.Entry(root)
entry.pack(pady=5)

def book_Navigation():
    tk.Label(root, text="Search for books using search bar. Click 'Order Here' to place an order. Click 'Profile' to update your information.").pack(pady=5)
navigation_button = tk.Button(root, text="Navigation", command=book_Navigation)
navigation_button.pack(pady=20)

def book_Search():
    searchBar = entry.get()
    bookList = ("The Giver", "Cat in the Hat", "Animal Farm")       # Book List
    if searchBar in bookList:
        messagebox.showinfo("Search Result", f"Book: {searchBar}")
    else:
        messagebox.showinfo("Search Error: Book not found.")
    
entry = tk.Entry(root).pack(pady=5)
search_button = tk.Button(root, text="Search", command=book_Search)
search_button.pack(pady=5)


def book_Ordering():
# Payment and shipping
    name = name_entry.get()
    address = address_entry.get()

    if name and address:
        messagebox.showinfo("Order was Successful")
    else:
        messagebox.showerror("Order Unsuccessful")

name_label = tk.Label(root, text="Enter Name: ").pack(pady=5)
name_entry = tk.Entry(root)

address_label = tk.Label(root, text="Enter Address: ").pack(pady=5)
address_entry = tk.Entry(root)

order_button = tk.Button(root, text="Order", command=book_Ordering)
order_button.pack(pady=5)


def book_Customer():
    profile_window = tk.Toplevel(root)      # Second Window
    profile_window.title("Customer Profile")
    profile_window.geometry("400x300")

    # Labels
    tk.Label(profile_window, text="Enter your First and Last Name: ").pack(pady=5)
    name_entry = tk.Entry(profile_window)
    name_entry.pack(pady=5)

    tk.Label(profile_window, text="Enter your address: ").pack(pady=5)
    address_entry = tk.Entry(profile_window)
    address_entry.pack(pady=5)

    def save_profile():
        name = name_entry.get()
        address = address_entry.get()
        if not name or not address:
            messagebox.showerror("ERROR: Please fill all feilds.")
        else:
            messagebox.info("Saved")
    save_profile_button = tk.Button(profile_window, text="Save", command=save_profile)
    save_profile_button.pack(pady=5)
    # Save Exit Button
    exit_button = tk.Button(profile_window, text="Exit", command=profile_window.destroy)
    exit_button.pack(pady=5)

button_frame = tk.Frame(root)
button_frame.pack(pady=5)

# add all buttons
book_Navigation_button = tk.Button(button_frame, text="Navigation", command=book_Navigation)
book_Navigation_button.pack(pady=5)

book_Ordering_button = tk.Button(button_frame, text="Order Here", command=book_Ordering)
book_Ordering_button.pack(pady=5)

book_Customer_button = tk.Button(button_frame, text="Profile", command=book_Customer)
book_Customer_button.pack(pady=5)


root.mainloop()