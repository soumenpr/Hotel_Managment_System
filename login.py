from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        # Title
        bg_img = Image.open("IMAGE/taj.jpg")
        bg_img = bg_img.resize((1250, 500), Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(bg_img)
        lblbg = Label(self.root, image=self.bg)
        lblbg.place(x=0, y=0, relwidth=1, relheight=1)

        # Username
        self.username_label = ttk.Label(self.root, text="Username:")
        self.username_label.pack(pady=(50, 0))
        self.username_entry = ttk.Entry(self.root, width=30)
        self.username_entry.pack()
        self.username_entry.focus()

        # Password
        self.password_label = ttk.Label(self.root, text="Password:")
        self.password_label.pack(pady=(10, 0))
        self.password_entry = ttk.Entry(self.root, width=30, show="*")
        self.password_entry.pack()

        # Login button
        self.login_button = ttk.Button(self.root, text="Login", command=self.authenticate)
        self.login_button.pack(pady=20)

        # Register link
        self.register_label = ttk.Label(self.root, text="Don't have an account? Register", foreground="blue", cursor="hand2")
        self.register_label.pack()
        self.register_label.bind("<Button-1>", self.register)

        # User database (for demo)
        self.users = {
            "user": "user123",
            "admin": "admin123"
        }

    def authenticate(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if not username or not password:
            messagebox.showwarning("Input Error", "Please enter both username and password")
            return
        if username in self.users and self.users[username] == password:
            messagebox.showinfo("Login Success", f"Welcome, {username}!")
            self.open_dashboard(username)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")
            self.password_entry.delete(0, END)

    def register(self, event):
        register_window = Toplevel(self.root)
        register_window.title("Register")
        register_window.geometry("300x250")

        ttk.Label(register_window, text="Register New Account", font=('Arial', 14, 'bold')).pack(pady=10)
        ttk.Label(register_window, text="Username:").pack()
        new_username = ttk.Entry(register_window, width=25)
        new_username.pack()
        ttk.Label(register_window, text="Password:").pack()
        new_password = ttk.Entry(register_window, width=25, show="*")
        new_password.pack()
        ttk.Label(register_window, text="Confirm Password:").pack()
        confirm_password = ttk.Entry(register_window, width=25, show="*")
        confirm_password.pack()

        def submit_registration():
            username = new_username.get()
            pwd = new_password.get()
            confirm_pwd = confirm_password.get()
            if not username or not pwd or not confirm_pwd:
                messagebox.showwarning("Input Error", "All fields are required")
                return
            if pwd != confirm_pwd:
                messagebox.showerror("Error", "Passwords don't match")
                return
            if username in self.users:
                messagebox.showerror("Error", "Username already exists")
                return
            self.users[username] = pwd
            messagebox.showinfo("Success", "Registration successful!")
            register_window.destroy()

        ttk.Button(register_window, text="Register", command=submit_registration).pack(pady=15)

    def open_dashboard(self, username):
        self.root.withdraw()
        try:
            from hotel import HotelManagementSystem
            hotel_window = Toplevel(self.root)
            app = HotelManagementSystem(hotel_window)
        except ImportError:
            messagebox.showerror("Error", "Hotel system not found.")
            self.root.deiconify()

    def on_close(self, window):
        window.destroy()
        self.root.deiconify()

if __name__ == "__main__":
    root = Tk()
    obj = LoginWindow(root)
    root.mainloop()