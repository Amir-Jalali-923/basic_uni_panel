import tkinter as tk
from tkinter import messagebox
from helpers import *
from panel import panel

def login_form(root):
    root.withdraw()
    win = tk.Toplevel()
    win.title("Login")
    win.geometry("300x200")
    form = tk.Frame(win)
    form.pack(expand=True)

    tk.Label(form, text="ID:").grid(row=0, column=0, padx=10, pady=10)
    s_id = tk.Entry(form)
    s_id.grid(row=0, column=1)

    tk.Label(form, text="Password:").grid(row=1, column=0, padx=10, pady=10)
    password = tk.Entry(form, show="*")
    password.grid(row=1, column=1)

    tk.Button(win, text="Login", command=lambda: login(s_id.get(), password.get())).pack(pady=10)

    def login(s_id, password):
        data = read_json("./data/students.json")
        if s_id not in data.keys():
            tk.messagebox.showerror("Error", "Invalid ID or Password")
            return
        if data[s_id]["password"] == password:
            win.destroy()
            panel(root, s_id)
        else:
            tk.messagebox.showerror("Error", "Invalid ID or Password")

    win.protocol(
        "WM_DELETE_WINDOW",
        lambda: (win.destroy(), root.deiconify())
    )

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
            "password": password.get(),
            "courses": []
        }
        last_id = get_last_id()
        append_student(last_id, data)
        tk.messagebox.showinfo("Success", "Account created successfully\n---!note your ID!---\nID: " + str(last_id))
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