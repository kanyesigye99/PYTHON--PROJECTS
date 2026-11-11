import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk
import sqlite3


# ============================================================
# STUDENTS SPORTS REGISTRATION SYSTEM
# ============================================================

# ---------------- DATABASE ----------------

connection = sqlite3.connect("students_sports.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    gender TEXT NOT NULL,
    contact TEXT,
    index_number TEXT UNIQUE NOT NULL,
    date_of_birth TEXT,
    sport TEXT,
    parent_name TEXT,
    parent_contact TEXT,
    parent_address TEXT,
    photo TEXT
)
""")

connection.commit()


# ============================================================
# LOGIN
# ============================================================

def login():

    username = username_entry.get()
    password = password_entry.get()

    if username == "mrsafehands" and password == "123456789":

        login_window.destroy()
        open_dashboard()

    else:

        messagebox.showerror(
            "Login Failed",
            "Incorrect username or password."
        )


login_window = tk.Tk()

login_window.title(
    "Students Sports Registration System - Login"
)

login_window.geometry("450x350")

login_window.resizable(False, False)


# Login title

tk.Label(
    login_window,
    text="MR. SAFE HANDS ACADEMY REGISTRATION SYSTEM",
    font=("mistral", 16, "bold")
).pack(pady=30)


# Username

tk.Label(
    login_window,
    text="Username",
    font=("Arial", 20)
).pack()

username_entry = tk.Entry(
    login_window,
    width=30,
    font=("Arial", 20)
)

username_entry.pack(pady=5)


# Password

tk.Label(
    login_window,
    text="Password",
    font=("Arial", 20)
).pack(pady=(10, 0))

password_entry = tk.Entry(
    login_window,
    width=30,
    show="*",
    font=("Arial", 20)
)

password_entry.pack(pady=5)


# Login button

tk.Button(
    login_window,
    text="LOGIN",
    width=20,
    bg="green",
    fg="white",
    font=("Times New Roman", 18, "bold"),
    command=login
).pack(pady=25)


tk.Label(
    login_window,
    text="Username: *****    Password: *****",
    font=("Arial", 12)
).pack()


# ============================================================
# DASHBOARD
# ============================================================

def open_dashboard():

    dashboard = tk.Tk()

    dashboard.title(
        "Students Sports Registration System"
    )

    dashboard.geometry("1250x780")

    dashboard.configure(
        bg="#f2f2f2"
    )


    # ========================================================
    # HEADER
    # ========================================================

    header = tk.Frame(
        dashboard,
        bg="#0b3d2e",
        height=90
    )

    header.pack(
        fill="x"
    )


    tk.Label(
        header,
        text="ISAAC RAMS SPORTS REGISTRATION SYSTEM",
        bg="#0b3d2e",
        fg="white",
        font=("Arial", 24, "bold")
    ).pack(pady=15)


    tk.Label(
        header,
        text="Student Athlete Registration Portal",
        bg="#0b3d2e",
        fg="white",
        font=("Arial", 11)
    ).pack()


    # ========================================================
    # MAIN FRAME
    # ========================================================

    main_frame = tk.Frame(
        dashboard,
        bg="#f2f2f2"
    )

    main_frame.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=20
    )


    # ========================================================
    # STUDENT REGISTRATION
    # ========================================================

    details_frame = tk.LabelFrame(
        main_frame,
        text="Student Sports Registration",
        font=("Arial", 14, "bold"),
        padx=15,
        pady=15
    )

    details_frame.pack(
        fill="x"
    )


    # Variables

    full_name = tk.StringVar()
    gender = tk.StringVar()
    contact = tk.StringVar()
    index_number = tk.StringVar()
    date_of_birth = tk.StringVar()
    sport = tk.StringVar()

    parent_name = tk.StringVar()
    parent_contact = tk.StringVar()
    parent_address = tk.StringVar()

    photo_path = tk.StringVar()


    # ========================================================
    # STUDENT PHOTO
    # ========================================================

    photo_frame = tk.Frame(
        details_frame
    )

    photo_frame.grid(
        row=0,
        column=4,
        rowspan=6,
        padx=30
    )


    photo_label = tk.Label(
        photo_frame,
        text="STUDENT PHOTO",
        width=20,
        height=15,
        relief="solid"
    )

    photo_label.pack()


    def select_photo():

        filename = filedialog.askopenfilename(
            title="Select Student Photo",

            filetypes=[
                ("Image Files", "*.jpg *.jpeg *.png"),
                ("JPG Files", "*.jpg"),
                ("PNG Files", "*.png")
            ]
        )

        if filename:

            photo_path.set(filename)

            try:

                image = Image.open(filename)

                image.thumbnail(
                    (140, 140)
                )

                photo = ImageTk.PhotoImage(
                    image
                )

                photo_label.config(
                    image=photo,
                    text=""
                )

                photo_label.image = photo

            except:

                messagebox.showerror(
                    "Error",
                    "Unable to load the selected photo."
                )


    tk.Button(
        photo_frame,
        text="CHOOSE PHOTO",
        command=select_photo
    ).pack(
        pady=10
    )


    # ========================================================
    # STUDENT INFORMATION
    # ========================================================

    # Full Name

    tk.Label(
        details_frame,
        text="Full Names:"
    ).grid(
        row=0,
        column=0,
        sticky="w",
        pady=5
    )

    tk.Entry(
        details_frame,
        textvariable=full_name,
        width=30
    ).grid(
        row=0,
        column=1,
        padx=10
    )


    # Gender

    tk.Label(
        details_frame,
        text="Gender:"
    ).grid(
        row=0,
        column=2,
        sticky="w"
    )

    gender_box = ttk.Combobox(
        details_frame,
        textvariable=gender,
        values=[
            "Male",
            "Female"
        ],
        state="readonly",
        width=27
    )

    gender_box.grid(
        row=0,
        column=3,
        padx=10
    )


    # Contact

    tk.Label(
        details_frame,
        text="Student Contact:"
    ).grid(
        row=1,
        column=0,
        sticky="w",
        pady=5
    )

    tk.Entry(
        details_frame,
        textvariable=contact,
        width=30
    ).grid(
        row=1,
        column=1,
        padx=10
    )


    # Index Number

    tk.Label(
        details_frame,
        text="Index Number:"
    ).grid(
        row=1,
        column=2,
        sticky="w"
    )

    tk.Entry(
        details_frame,
        textvariable=index_number,
        width=30
    ).grid(
        row=1,
        column=3,
        padx=10
    )


    # Date of Birth

    tk.Label(
        details_frame,
        text="Date of Birth:"
    ).grid(
        row=2,
        column=0,
        sticky="w",
        pady=5
    )

    tk.Entry(
        details_frame,
        textvariable=date_of_birth,
        width=30
    ).grid(
        row=2,
        column=1,
        padx=10
    )


    # Sport

    tk.Label(
        details_frame,
        text="Sport:"
    ).grid(
        row=2,
        column=2,
        sticky="w"
    )


    sport_box = ttk.Combobox(
        details_frame,
        textvariable=sport,
        values=[
            "Football",
            "Netball",
            "Basketball",
            "Volleyball",
            "Athletics",
            "Rugby",
            "Handball",
            "Futsal",
            "Beach Soccer",
            "Chess",
            "Table Tennis",
            "Badminton",
            "Swimming",
            "Boxing",
            "Other"
        ],
        width=27
    )

    sport_box.grid(
        row=2,
        column=3,
        padx=10
    )


    # ========================================================
    # PARENT / GUARDIAN DETAILS
    # ========================================================

    tk.Label(
        details_frame,
        text="Parent/Guardian:"
    ).grid(
        row=3,
        column=0,
        sticky="w",
        pady=5
    )

    tk.Entry(
        details_frame,
        textvariable=parent_name,
        width=30
    ).grid(
        row=3,
        column=1,
        padx=10
    )


    tk.Label(
        details_frame,
        text="Parent Contact:"
    ).grid(
        row=3,
        column=2,
        sticky="w"
    )

    tk.Entry(
        details_frame,
        textvariable=parent_contact,
        width=30
    ).grid(
        row=3,
        column=3,
        padx=10
    )


    tk.Label(
        details_frame,
        text="Parent Address:"
    ).grid(
        row=4,
        column=0,
        sticky="w",
        pady=5
    )

    tk.Entry(
        details_frame,
        textvariable=parent_address,
        width=30
    ).grid(
        row=4,
        column=1,
        padx=10
    )


    # ========================================================
    # CLEAR FORM
    # ========================================================

    def clear_form():

        full_name.set("")
        gender.set("")
        contact.set("")
        index_number.set("")
        date_of_birth.set("")
        sport.set("")

        parent_name.set("")
        parent_contact.set("")
        parent_address.set("")

        photo_path.set("")

        photo_label.config(
            image="",
            text="STUDENT PHOTO"
        )

        photo_label.image = None


    # ========================================================
    # SAVE STUDENT
    # ========================================================

    def save_student():

        if full_name.get() == "":
            messagebox.showwarning(
                "Missing Information",
                "Please enter the student's full name."
            )
            return


        if gender.get() == "":
            messagebox.showwarning(
                "Missing Information",
                "Please select the student's gender."
            )
            return


        if index_number.get() == "":
            messagebox.showwarning(
                "Missing Information",
                "Please enter the student's index number."
            )
            return


        if sport.get() == "":
            messagebox.showwarning(
                "Missing Information",
                "Please select the sport."
            )
            return


        try:

            cursor.execute("""
            INSERT INTO students (
                full_name,
                gender,
                contact,
                index_number,
                date_of_birth,
                sport,
                parent_name,
                parent_contact,
                parent_address,
                photo
            )

            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (

                full_name.get(),
                gender.get(),
                contact.get(),
                index_number.get(),
                date_of_birth.get(),
                sport.get(),
                parent_name.get(),
                parent_contact.get(),
                parent_address.get(),
                photo_path.get()

            ))


            connection.commit()


            messagebox.showinfo(
                "Registration Successful",
                "Student has been successfully registered for sports."
            )


            clear_form()

            load_students()


        except sqlite3.IntegrityError:

            messagebox.showerror(
                "Registration Error",
                "This index number is already registered."
            )


    # ========================================================
    # BUTTONS
    # ========================================================

    button_frame = tk.Frame(
        main_frame,
        bg="#f2f2f2"
    )

    button_frame.pack(
        fill="x",
        pady=15
    )


    tk.Button(
        button_frame,
        text="REGISTER STUDENT",
        bg="green",
        fg="white",
        font=("Arial", 11, "bold"),
        width=20,
        command=save_student
    ).pack(
        side="left",
        padx=5
    )


    tk.Button(
        button_frame,
        text="CLEAR FORM",
        bg="orange",
        fg="white",
        font=("Arial", 11, "bold"),
        width=18,
        command=clear_form
    ).pack(
        side="left",
        padx=5
    )


    # ========================================================
    # REGISTERED STUDENTS
    # ========================================================

    records_frame = tk.LabelFrame(
        main_frame,
        text="Registered Student Athletes",
        font=("Arial", 14, "bold"),
        padx=10,
        pady=10
    )

    records_frame.pack(
        fill="both",
        expand=True
    )


    columns = (
        "ID",
        "Full Name",
        "Gender",
        "Contact",
        "Index Number",
        "Date of Birth",
        "Sport",
        "Parent",
        "Parent Contact"
    )


    student_table = ttk.Treeview(
        records_frame,
        columns=columns,
        show="headings"
    )


    for column in columns:

        student_table.heading(
            column,
            text=column
        )

        student_table.column(
            column,
            width=120
        )


    student_table.pack(
        fill="both",
        expand=True,
        side="left"
    )


    scrollbar = ttk.Scrollbar(
        records_frame,
        orient="vertical",
        command=student_table.yview
    )

    scrollbar.pack(
        side="right",
        fill="y"
    )


    student_table.configure(
        yscrollcommand=scrollbar.set
    )


    # ========================================================
    # LOAD STUDENTS
    # ========================================================

    def load_students():

        for item in student_table.get_children():

            student_table.delete(item)


        cursor.execute("""
        SELECT
            id,
            full_name,
            gender,
            contact,
            index_number,
            date_of_birth,
            sport,
            parent_name,
            parent_contact

        FROM students

        ORDER BY id DESC
        """)


        records = cursor.fetchall()


        for record in records:

            student_table.insert(
                "",
                "end",
                values=record
            )


    # ========================================================
    # SEARCH
    # ========================================================

    search_frame = tk.Frame(
        main_frame,
        bg="#f2f2f2"
    )

    search_frame.pack(
        fill="x",
        pady=8
    )


    search_text = tk.StringVar()


    tk.Label(
        search_frame,
        text="Search:"
    ).pack(
        side="left"
    )


    search_entry = tk.Entry(
        search_frame,
        textvariable=search_text,
        width=30
    )

    search_entry.pack(
        side="left",
        padx=10
    )


    def search_student():

        for item in student_table.get_children():

            student_table.delete(item)


        search_value = search_text.get()


        cursor.execute("""
        SELECT
            id,
            full_name,
            gender,
            contact,
            index_number,
            date_of_birth,
            sport,
            parent_name,
            parent_contact

        FROM students

        WHERE full_name LIKE ?
        OR index_number LIKE ?
        OR sport LIKE ?

        ORDER BY id DESC
        """, (

            "%" + search_value + "%",
            "%" + search_value + "%",
            "%" + search_value + "%"

        ))


        records = cursor.fetchall()


        for record in records:

            student_table.insert(
                "",
                "end",
                values=record
            )


    tk.Button(
        search_frame,
        text="SEARCH",
        bg="#1f5f8b",
        fg="white",
        command=search_student
    ).pack(
        side="left"
    )


    tk.Button(
        search_frame,
        text="SHOW ALL",
        command=load_students
    ).pack(
        side="left",
        padx=5
    )


    # ========================================================
    # DELETE STUDENT
    # ========================================================

    def delete_student():

        selected = student_table.selection()


        if not selected:

            messagebox.showwarning(
                "No Selection",
                "Please select a student."
            )

            return


        student = student_table.item(
            selected[0]
        )


        student_id = student["values"][0]


        confirm = messagebox.askyesno(
            "Confirm Delete",
            "Are you sure you want to delete this student?"
        )


        if confirm:

            cursor.execute(
                "DELETE FROM students WHERE id = ?",
                (student_id,)
            )

            connection.commit()

            load_students()


            messagebox.showinfo(
                "Deleted",
                "Student record deleted successfully."
            )


    tk.Button(
        button_frame,
        text="DELETE SELECTED",
        bg="red",
        fg="white",
        font=("Arial", 11, "bold"),
        width=18,
        command=delete_student
    ).pack(
        side="left",
        padx=5
    )


    # ========================================================
    # EXIT SYSTEM
    # ========================================================

    def close_system():

        connection.close()

        dashboard.destroy()


    tk.Button(
        dashboard,
        text="EXIT SYSTEM",
        command=close_system,
        bg="darkred",
        fg="white",
        font=("Arial", 11, "bold"),
        width=15
    ).pack(
        pady=10
    )


    # Load existing students

    load_students()


    dashboard.protocol(
        "WM_DELETE_WINDOW",
        close_system
    )


    dashboard.mainloop()


# ============================================================
# START SYSTEM
# ============================================================

login_window.mainloop()