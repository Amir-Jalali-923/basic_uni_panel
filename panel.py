import tkinter as tk
from helpers import *


def panel(root, s_id):
    # Load all students data and extract current student's courses
    data = read_json("./data/students.json")
    student_courses = data[s_id]["courses"]

    # Safety check: return to home if student ID is invalid
    if s_id not in data:
        root.deiconify()
        return

    # Hide home window and open panel window
    root.withdraw()
    win = tk.Toplevel(root)
    win.title("Panel")
    win.geometry("500x300")

    # Greeting using student's name
    tk.Label(
        win,
        text=f'Hello, {data[s_id]["name"]}',
        font=("Arial", 16)
    ).pack(pady=10)

    form = tk.Frame(win)
    form.pack(expand=True)

    # Available courses list
    tk.Label(form, text="Available Courses:").grid(row=0, column=0, padx=10)
    course_list = tk.Listbox(form)
    course_list.insert(1, "math")
    course_list.insert(2, "english")
    course_list.insert(3, "physics")
    course_list.insert(4, "chemistry")
    course_list.grid(row=1, column=0, padx=10, pady=10)

    # Selected courses list (loaded from saved data)
    tk.Label(form, text="Selected Courses:").grid(row=0, column=1, padx=10)
    selected_courses_list = tk.Listbox(form)

    for i, course in enumerate(student_courses):
        selected_courses_list.insert(i, course)

    selected_courses_list.grid(row=1, column=1, padx=10, pady=10)

    def addcourse(course):
        # Prevent duplicate course selection
        if course in student_courses:
            tk.messagebox.showerror("Error", "Course already selected")
            return

        # Update in-memory data and persist to JSON
        student_courses.append(course)
        write_json("./data/students.json", data)

        # Reflect change immediately in UI
        selected_courses_list.insert(len(student_courses), course)

    def deletecourse(course_index):
        # Remove course from student data
        student_courses.remove(selected_courses_list.get(course_index))

        # Persist changes and update UI
        write_json("./data/students.json", data)
        selected_courses_list.delete(course_index)

    # Action buttons
    tk.Button(
        form,
        text="Add",
        command=lambda: addcourse(course_list.get(course_list.curselection()))
    ).grid(row=2, column=0, padx=10, pady=10)

    tk.Button(
        form,
        text="Delete",
        command=lambda: deletecourse(selected_courses_list.curselection())
    ).grid(row=2, column=1, padx=10, pady=10)

    # Restore home window when panel is closed
    win.protocol(
        "WM_DELETE_WINDOW",
        lambda: (win.destroy(), root.deiconify())
    )
