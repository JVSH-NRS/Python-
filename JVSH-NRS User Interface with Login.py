# CREATED BY JVSH-NRS ON GITHUB



import tkinter as tk

# Define function to handle login button click event
def handle_login():
    username = username_entry.get()
    password = password_entry.get()
    if username == "admin" and password == "password":
        status_label.config(text="Login successful!", fg="green")
    else:
        status_label.config(text="Invalid username or password", fg="red")
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("Login")

# Create username label and entry
username_label = tk.Label(root, text="Username:")
username_label.grid(row=0, column=0, padx=5, pady=5)
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=5, pady=5)

# Create password label and entry
password_label = tk.Label(root, text="Password:")
password_label.grid(row=1, column=0, padx=5, pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=5, pady=5)

# Create login button
login_button = tk.Button(root, text="Login", command=handle_login)
login_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Create status label
status_label = tk.Label(root, text="")
status_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Run main loop
root.mainloop()


# CREATED BY JVSH-NRS ON GITHUB
# CREATED BY JVSH-NRS ON GITHUB
#todo Write script for login + include an interface