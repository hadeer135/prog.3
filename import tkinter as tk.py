import tkinter as tk
from tkinter import messagebox

def login_action():
    # Here you would add the logic to verify login credentials
    username = entry_username.get()
    password = entry_password.get()
    remember_me = chk_remember_me_var.get()
    # For now, we'll just print the credentials to the console
    print(f"Username: {username}, Password: {password}, Remember Me: {remember_me}")

# Create the main window
root = tk.Tk()
root.title("Database Login")

# Create a frame for the login form
login_frame = tk.Frame(root)
login_frame.pack(pady=20)

# Add a username label and entry
lbl_username = tk.Label(login_frame, text="Username")
lbl_username.grid(row=0, column=0, sticky='e', padx=5, pady=5)
entry_username = tk.Entry(login_frame)
entry_username.grid(row=0, column=1, padx=5, pady=5)

# Add a password label and entry
lbl_password = tk.Label(login_frame, text="Password")
lbl_password.grid(row=1, column=0, sticky='e', padx=5, pady=5)
entry_password = tk.Entry(login_frame, show="*")
entry_password.grid(row=1, column=1, padx=5, pady=5)

# Add a "Remember Me" checkbox
chk_remember_me_var = tk.IntVar()
chk_remember_me = tk.Checkbutton(login_frame, text="Remember Me", variable=chk_remember_me_var)
chk_remember_me.grid(row=2, column=1, sticky='w', padx=5, pady=5)

# Add a login button
btn_login = tk.Button(login_frame, text="Login", command=login_action)
btn_login.grid(row=3, column=1, pady=10)

# Start the main loop
root.mainloop()
