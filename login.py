
"""User login window"""

import tkinter as tk
from tkinter import messagebox
from user_manager import UserManager
from main_menu import MainMenuWindow


class LoginWindow:
    def __init__(self):
        self.um = UserManager()
        self.root = tk.Tk()
        self.root.title("Statistics Quiz - Login")

        tk.Label(self.root, text="Username:").pack(padx=20, pady=10)
        self.entry = tk.Entry(self.root, width=25)
        self.entry.pack(padx=20, pady=5)
        tk.Button(self.root, text="Log In", command=self._login).pack(pady=15)

        self.root.mainloop()

    def _login(self):
        username = self.entry.get().strip()
        if not username:
            messagebox.showerror("Error", "Username cannot be empty")
            return
        self.um.login(username)
        messagebox.showinfo("Welcome", f"Hello, {username}!")
        self.root.destroy()
        MainMenuWindow(self.um)
