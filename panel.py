import tkinter as tk
from tkinter import messagebox
from helpers import *

def panel(root, s_id):
    data = read_json("./data/students.json")
    student_courses = data[s_id]["courses"]

    if s_id not in data.keys():
        root.deiconify()
        return

    root.withdraw()
    win = tk.Toplevel(root)
    win.title("Panel")
    win.geometry("500x300")
    form = tk.Frame(win)

    tk.Label(win, text=f'Hello, {data[s_id]["name"]}', font=("Arial", 16)).pack(pady=10)
    form.pack(expand=True)

    tk.Label(form, text="Available Courses:").grid(row=0, column=0, padx=10)
    course_list = tk.Listbox(form)
    course_list.insert(1, "math")
    course_list.insert(2, "english")
    course_list.insert(3, "physics")
    course_list.insert(4, "chemistry")
    course_list.grid(row=1, column=0, padx=10, pady=10)

    tk.Label(form, text="Selected Courses:").grid(row=0, column=1, padx=10)
    selected_courses_list = tk.Listbox(form)
    for i in range(len(student_courses)):
        selected_courses_list.insert(i, student_courses[i])

    selected_courses_list.grid(row=1, column=1, padx=10, pady=10)

    addbtn = tk.Button(form, text="Add", command=lambda: addcourse(course_list.get(course_list.curselection())))
    addbtn.grid(row=2, column=0, padx=10, pady=10)

    deletebtn = tk.Button(form, text="Delete", command=lambda: deletecourse(selected_courses_list.curselection()))
    deletebtn.grid(row=2, column=1, padx=10, pady=10)

    def addcourse(course):
        if course in student_courses:
            tk.messagebox.showerror("Error", "Course already selected")
            return
        print(course)
        student_courses.append(course)
        write_json("./data/students.json", data)
        selected_courses_list.insert(len(student_courses), course)

    def deletecourse(course_index):
        student_courses.remove(selected_courses_list.get(course_index))

        write_json("./data/students.json", data)
        selected_courses_list.delete(course_index)
        
    win.protocol(
        "WM_DELETE_WINDOW",
        lambda: (win.destroy(), root.deiconify()) 
    )