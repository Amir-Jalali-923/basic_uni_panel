import tkinter as tk
from helpers import *

def login_form(root):
    root.withdraw()
    login_win = tk.Toplevel()
    login_win.title("Login")
    login_win.geometry("300x200")

    tk.Label(login_win, text="Login Window").pack(expand=True)

    login_win.protocol("WM_DELETE_WINDOW", lambda: get_root(login_win, root))

def register_form(root):
    root.withdraw()

    win = tk.Toplevel(root)
    win.title("Sign Up")
    win.geometry("300x260")
    form = tk.Frame(win)
    form.pack(expand=True)

    tk.Label(form, text="Full Name:").grid(row=0, column=0, padx=10, pady=10)
    name = tk.Entry(form)
    name.grid(row=0, column=1)

    tk.Label(form, text="Age:").grid(row=1, column=0, padx=10, pady=10)
    age = tk.Entry(form)
    age.grid(row=1, column=1)

    tk.Label(form, text="Phone:").grid(row=2, column=0, padx=10, pady=10)
    phone = tk.Entry(form)
    phone.grid(row=2, column=1)

    tk.Label(form, text="Password:").grid(row=3, column=0, padx=10, pady=10)
    password = tk.Entry(form, show="*")
    password.grid(row=3, column=1)

    def submit():
        data = {
            "name": name.get(),
            "age": int(age.get()),
            "phone": phone.get(),
            "password": password.get()
        }
        append_student(get_last_id(), data)
        win.destroy()
        root.deiconify()

    tk.Button(win, text="Create Account", command=submit).pack(pady=10)

    win.protocol(
        "WM_DELETE_WINDOW",
        lambda: (win.destroy(), root.deiconify())
    )

def get_root(window, root):
    window.destroy()
    root.deiconify()

def main():
    #initialize Home GUI
    home = tk.Tk()
    home.title("Home")
    home.geometry("500x300")
    
    form = tk.Frame(home)
    form.pack(expand=True)

    login_btn = tk.Button(form, text="Login", width=15, background="blue", foreground="white", font=("Arial", 12), command=lambda: login_form(home))
    register_btn = tk.Button(form, text="Register", width=15, background="blue", foreground="white", font=("Arial", 12), command=lambda: register_form(home))
    login_btn.grid(row=0, column=0, padx=20, pady=20)
    register_btn.grid(row=0, column=1, padx=20, pady=20)

    home.mainloop()

if __name__ == "__main__":
    main()