from tkinter import *
from tkinter import ttk
import mysql.connector
from PIL import Image, ImageTk
from tkinter import messagebox


def create_db():
    try:
        conn = mysql.connector.connect(host="localhost", user="root", password="Mayank13579pro")    # Connect to MySQL server (without specifying a database)
        my_cursor = conn.cursor()
        my_cursor.execute("CREATE DATABASE IF NOT EXISTS criminal_management")    # Create the database if it doesn't exist
        my_cursor.execute("USE criminal_management")      # Switch to the newly created database
        my_cursor.execute("""
            CREATE TABLE IF NOT EXISTS criminal (
                case_id       VARCHAR(20),
                criminal_no   VARCHAR(20),
                criminal_name VARCHAR(50),
                punishment    VARCHAR(100),
                arrest_date   VARCHAR(20),
                date_of_crime VARCHAR(20),
                address       VARCHAR(100),
                age           VARCHAR(5),
                occupation    VARCHAR(50),
                birth_mark    VARCHAR(50),
                crime_type    VARCHAR(50),
                father_name   VARCHAR(50),
                gender        VARCHAR(10),
                wanted_status VARCHAR(5)
            )
        """)        # Create the 'criminal' table if it doesn't exist and define its schema
        conn.commit()
        conn.close()
    except Exception as e:
        messagebox.showerror("DB Setup Error", str(e))


class Criminal:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1400x700+0+0")      # Set the window size and position
        self.root.title("Criminal Management System")

        # Variables
        self.case_id_var      = StringVar()
        self.criminal_no_var  = StringVar()
        self.criminal_name_var= StringVar()
        self.arrest_date_var  = StringVar()
        self.date_of_crime_var= StringVar()
        self.address_var      = StringVar()
        self.age_var          = StringVar()
        self.occupation_var   = StringVar()
        self.birth_mark_var   = StringVar()
        self.crime_type_var   = StringVar()
        self.father_name_var  = StringVar()
        self.punishment_var   = StringVar()
        self.gender_var       = StringVar()
        self.wanted_var       = StringVar()

        # Title
        lbl_title = Label(self.root, text="CRIMINAL DATABASE MANAGEMENT SYSTEM",font=("times new roman", 30, "bold"), bg="black", fg="gold")
        lbl_title.place(x=0, y=0, relwidth=1, height=50)

        # Main Frame
        main_frame = Frame(self.root, bd=2, bg="white")     # Creates a frame that holds widgets and components
        main_frame.place(x=20, y=60, width=1230, height=585)

        # Upper Frame
        upper_frame = LabelFrame(main_frame, bd=2, bg="white", relief=SUNKEN,text="Criminal Information",font=("times new roman", 12, "bold"), fg="red")    # Creates a labeled frame for input fields and buttons
        upper_frame.place(x=10, y=10, width=1200, height=300)

        # Case ID
        Label(upper_frame, text="Case ID:", font=("times new roman", 12, "bold"), bg="white").grid(row=0, column=0, padx=10, pady=5, sticky=W)  # Creates a label for Case ID
        ttk.Entry(upper_frame, font=("times new roman", 12, "bold"), textvariable=self.case_id_var).grid(row=0, column=1, padx=10, pady=5, sticky=W)    # sticky ==> Aligns the widget to the west of cell (left-aligned)

        # Criminal No
        Label(upper_frame, text="Criminal No:", font=("times new roman", 12, "bold"), bg="white").grid(row=0, column=2, padx=10, pady=5, sticky=W)
        ttk.Entry(upper_frame, font=("times new roman", 12, "bold"), textvariable=self.criminal_no_var).grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Criminal Name
        Label(upper_frame, text="Criminal Name:", font=("times new roman", 12, "bold"), bg="white").grid(row=1, column=0, padx=10, pady=5, sticky=W)
        ttk.Entry(upper_frame, font=("times new roman", 12, "bold"), textvariable=self.criminal_name_var).grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Arrest Date
        Label(upper_frame, text="Arrest Date:", font=("times new roman", 12, "bold"), bg="white").grid(row=1, column=2, padx=10, pady=5, sticky=W)
        ttk.Entry(upper_frame, font=("times new roman", 12, "bold"), textvariable=self.arrest_date_var).grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Date Of Crime
        Label(upper_frame, text="Date Of Crime:", font=("times new roman", 12, "bold"), bg="white").grid(row=2, column=0, padx=10, pady=5, sticky=W)
        ttk.Entry(upper_frame, font=("times new roman", 12, "bold"), textvariable=self.date_of_crime_var).grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # Address
        Label(upper_frame, text="Address:", font=("times new roman", 12, "bold"), bg="white").grid(row=2, column=2, padx=10, pady=5, sticky=W)
        ttk.Entry(upper_frame, font=("times new roman", 12, "bold"), textvariable=self.address_var).grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Age
        Label(upper_frame, text="Age:", font=("times new roman", 12, "bold"), bg="white").grid(row=3, column=0, padx=10, pady=5, sticky=W)
        ttk.Entry(upper_frame, font=("times new roman", 12, "bold"), textvariable=self.age_var).grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Occupation
        Label(upper_frame, text="Occupation:", font=("times new roman", 12, "bold"), bg="white").grid(row=3, column=2, padx=10, pady=5, sticky=W)
        ttk.Entry(upper_frame, font=("times new roman", 12, "bold"), textvariable=self.occupation_var).grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # Birth Mark
        Label(upper_frame, text="Birth Mark:", font=("times new roman", 12, "bold"), bg="white").grid(row=4, column=0, padx=10, pady=5, sticky=W)
        ttk.Entry(upper_frame, font=("times new roman", 12, "bold"), textvariable=self.birth_mark_var).grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # Crime Type
        Label(upper_frame, text="Crime Type:", font=("times new roman", 12, "bold"), bg="white").grid(row=4, column=2, padx=10, pady=5, sticky=W)
        ttk.Entry(upper_frame, font=("times new roman", 12, "bold"), textvariable=self.crime_type_var).grid(row=4, column=3, padx=10, pady=5, sticky=W)

        # Father Name
        Label(upper_frame, text="Father Name:", font=("times new roman", 12, "bold"), bg="white").grid(row=5, column=0, padx=10, pady=5, sticky=W)
        ttk.Entry(upper_frame, font=("times new roman", 12, "bold"), textvariable=self.father_name_var).grid(row=5, column=1, padx=10, pady=5, sticky=W)

        # Gender Label
        Label(upper_frame, text="Gender:", font=("times new roman", 12, "bold"), bg="white").grid(row=0, column=5, padx=10, pady=5, sticky=W)

        # Punishment
        Label(upper_frame, text="Punishment:", font=("times new roman", 12, "bold"), bg="white").grid(row=4, column=5, padx=10, pady=5, sticky=W)
        ttk.Entry(upper_frame, font=("times new roman", 12, "bold"), textvariable=self.punishment_var).grid(row=4, column=6, padx=10, pady=5)

        # Wanted Status Label
        Label(upper_frame, text="Wanted Status:", font=("times new roman", 12, "bold"), bg="white").grid(row=2, column=5, padx=10, pady=5, sticky=W)

        # Radio Buttons - Gender
        radio_frame_gender = Frame(upper_frame, bd=2, relief=RIDGE, bg="white")
        radio_frame_gender.place(x=700, y=0, width=200, height=40)
        Radiobutton(radio_frame_gender, text="Male", variable=self.gender_var, value="Male",
                    bg="white", font=("times new roman", 12, "bold")).grid(row=0, column=0, padx=10, pady=5, sticky=W)    # Creates a radio button
        Radiobutton(radio_frame_gender, text="Female", variable=self.gender_var, value="Female",
                    bg="white", font=("times new roman", 12, "bold")).grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Radio Buttons - Wanted Status
        radio_frame_wanted = Frame(upper_frame, bd=2, relief=RIDGE, bg="white")
        radio_frame_wanted.place(x=735, y=70, width=200, height=40)
        Radiobutton(radio_frame_wanted, text="Yes", variable=self.wanted_var, value="Yes",
                    bg="white", font=("times new roman", 12, "bold")).grid(row=0, column=0, padx=10, pady=5, sticky=W)
        Radiobutton(radio_frame_wanted, text="No", variable=self.wanted_var, value="No",
                    bg="white", font=("times new roman", 12, "bold")).grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Button Frame
        button_frame = Frame(upper_frame, bd=2, relief=SUNKEN, bg="white")
        button_frame.place(x=7.5, y=220, width=680, height=55)
        Button(button_frame, text="Add Record",    font=("times new roman", 12, "bold"), command=self.add_data,    bg="red", fg="gold", width=15).grid(row=0, column=0, padx=10, pady=5)
        Button(button_frame, text="Update Record", font=("times new roman", 12, "bold"), command=self.update_data, bg="red", fg="gold", width=15).grid(row=0, column=1, padx=10, pady=5)
        Button(button_frame, text="Delete Record", font=("times new roman", 12, "bold"), command=self.delete_data, bg="red", fg="gold", width=15).grid(row=0, column=2, padx=10, pady=5)
        Button(button_frame, text="Clear Record",  font=("times new roman", 12, "bold"), command=self.clear_data,  bg="red", fg="gold", width=15).grid(row=0, column=3, padx=10, pady=5)

        # Down Frame
        down_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                text="Criminal Details",
                                font=("times new roman", 12, "bold"), fg="red")
        down_frame.place(x=10, y=320, width=1200, height=250)

        # Search Frame
        search_frame = LabelFrame(down_frame, bd=2, bg="white", relief=RIDGE,
                                text="Search Criminal",font=("times new roman", 12, "bold"), fg="red")
        search_frame.place(x=7.5, y=5, width=1180, height=70)

        Label(search_frame, text="Search By:", font=("times new roman", 12, "bold"), bg="red", fg="gold").grid(row=0, column=0, padx=10, sticky=W)

        self.combo_search = ttk.Combobox(search_frame, font=("times new roman", 12, "bold"), state="readonly", width=15)
        self.combo_search["values"] = ("Select Option", "Case ID", "Criminal No", "Name")
        self.combo_search.current(0)
        self.combo_search.grid(row=0, column=1, padx=10, sticky=W)

        self.search_txt = ttk.Entry(search_frame, font=("times new roman", 12, "bold"))
        self.search_txt.grid(row=0, column=2, padx=10, sticky=W)

        Button(search_frame, text="Search Record",   font=("times new roman", 12, "bold"), command=self.search_data,   bg="red", fg="gold", width=15).grid(row=0, column=3, padx=10, pady=5)
        Button(search_frame, text="Show All Records", font=("times new roman", 12, "bold"), command=self.fetch_data,   bg="red", fg="gold", width=15).grid(row=0, column=4, padx=10, pady=5)

        # Table Frame
        table_frame = Frame(down_frame, bd=2, relief=RIDGE)
        table_frame.place(x=7.5, y=75, width=1180, height=145)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.criminal_table = ttk.Treeview(table_frame,
            columns=("1","2","3","4","5","6","7","8","9","10","11","12","13","14"),
            xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT,  fill=Y)
        scroll_x.config(command=self.criminal_table.xview)
        scroll_y.config(command=self.criminal_table.yview)

        self.criminal_table.heading("1",  text="Case ID")
        self.criminal_table.heading("2",  text="Criminal No")
        self.criminal_table.heading("3",  text="Name")
        self.criminal_table.heading("4",  text="Punishment")
        self.criminal_table.heading("5",  text="Arrest Date")
        self.criminal_table.heading("6",  text="Date Of Crime")
        self.criminal_table.heading("7",  text="Address")
        self.criminal_table.heading("8",  text="Age")
        self.criminal_table.heading("9",  text="Occupation")
        self.criminal_table.heading("10", text="Birth Mark")
        self.criminal_table.heading("11", text="Crime Type")
        self.criminal_table.heading("12", text="Father Name")
        self.criminal_table.heading("13", text="Gender")
        self.criminal_table.heading("14", text="Wanted Status")

        self.criminal_table["show"] = "headings"

        for col in ("1","2","3","4","5","6","7","8","9","10","11","12","13","14"):
            self.criminal_table.column(col, width=100)

        self.criminal_table.pack(fill=BOTH, expand=1)
        self.criminal_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_data()

    # ── DB helper ────────────────────────────────────────────────
    def get_conn(self):
        return mysql.connector.connect(
            host="localhost", user="root",
            password="Mayank13579pro",
            database="criminal_management"
        )

    # ── CRUD ─────────────────────────────────────────────────────
    def add_data(self):
        if self.case_id_var.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
            return
        try:
            conn = self.get_conn()
            cur  = conn.cursor()
            cur.execute(
                "INSERT INTO criminal VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (
                    self.case_id_var.get(),
                    self.criminal_no_var.get(),
                    self.criminal_name_var.get(),
                    self.punishment_var.get(),
                    self.arrest_date_var.get(),
                    self.date_of_crime_var.get(),
                    self.address_var.get(),
                    self.age_var.get(),
                    self.occupation_var.get(),
                    self.birth_mark_var.get(),
                    self.crime_type_var.get(),
                    self.father_name_var.get(),
                    self.gender_var.get(),
                    self.wanted_var.get(),
                )
            )
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Record added successfully", parent=self.root)
            self.fetch_data()
        except Exception as e:
            messagebox.showerror("Error", f"Error inserting data: {e}", parent=self.root)

    def fetch_data(self):
        try:
            conn = self.get_conn()
            cur  = conn.cursor()
            cur.execute("SELECT * FROM criminal")
            rows = cur.fetchall()
            conn.close()
            self.criminal_table.delete(*self.criminal_table.get_children())
            for row in rows:
                self.criminal_table.insert("", END, values=row)
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching data: {e}", parent=self.root)

    def get_cursor(self, event):
        cursor_row = self.criminal_table.focus()
        content    = self.criminal_table.item(cursor_row)
        row        = content["values"]
        if row:
            self.case_id_var.set(row[0])
            self.criminal_no_var.set(row[1])
            self.criminal_name_var.set(row[2])
            self.punishment_var.set(row[3])
            self.arrest_date_var.set(row[4])
            self.date_of_crime_var.set(row[5])
            self.address_var.set(row[6])
            self.age_var.set(row[7])
            self.occupation_var.set(row[8])
            self.birth_mark_var.set(row[9])
            self.crime_type_var.set(row[10])
            self.father_name_var.set(row[11])
            self.gender_var.set(row[12])
            self.wanted_var.set(row[13])

    def update_data(self):
        if self.case_id_var.get() == "":
            messagebox.showerror("Error", "Select a record to update", parent=self.root)
            return
        try:
            conn = self.get_conn()
            cur  = conn.cursor()
            cur.execute("""
                UPDATE criminal SET
                    criminal_no=%s, criminal_name=%s, punishment=%s,
                    arrest_date=%s, date_of_crime=%s, address=%s,
                    age=%s, occupation=%s, birth_mark=%s,
                    crime_type=%s, father_name=%s, gender=%s, wanted_status=%s
                WHERE case_id=%s
            """, (
                self.criminal_no_var.get(),
                self.criminal_name_var.get(),
                self.punishment_var.get(),
                self.arrest_date_var.get(),
                self.date_of_crime_var.get(),
                self.address_var.get(),
                self.age_var.get(),
                self.occupation_var.get(),
                self.birth_mark_var.get(),
                self.crime_type_var.get(),
                self.father_name_var.get(),
                self.gender_var.get(),
                self.wanted_var.get(),
                self.case_id_var.get(),
            ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Record updated successfully", parent=self.root)
            self.fetch_data()
        except Exception as e:
            messagebox.showerror("Error", f"Error updating data: {e}", parent=self.root)

    def delete_data(self):
        if self.case_id_var.get() == "":
            messagebox.showerror("Error", "Select a record to delete", parent=self.root)
            return
        try:
            conn = self.get_conn()
            cur  = conn.cursor()
            cur.execute("DELETE FROM criminal WHERE case_id=%s", (self.case_id_var.get(),))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Record deleted successfully", parent=self.root)
            self.clear_data()
            self.fetch_data()
        except Exception as e:
            messagebox.showerror("Error", f"Error deleting data: {e}", parent=self.root)

    def clear_data(self):
        self.case_id_var.set("")
        self.criminal_no_var.set("")
        self.criminal_name_var.set("")
        self.punishment_var.set("")
        self.arrest_date_var.set("")
        self.date_of_crime_var.set("")
        self.address_var.set("")
        self.age_var.set("")
        self.occupation_var.set("")
        self.birth_mark_var.set("")
        self.crime_type_var.set("")
        self.father_name_var.set("")
        self.gender_var.set("")
        self.wanted_var.set("")

    def search_data(self):
        if self.combo_search.get() == "Select Option":
            messagebox.showerror("Error", "Select a search option", parent=self.root)
            return
        try:
            conn = self.get_conn()
            cur  = conn.cursor()
            col_map = {"Case ID": "case_id", "Criminal No": "criminal_no", "Name": "criminal_name"}
            col = col_map[self.combo_search.get()]
            cur.execute(f"SELECT * FROM criminal WHERE {col} LIKE %s", (f"%{self.search_txt.get()}%",))
            rows = cur.fetchall()
            conn.close()
            self.criminal_table.delete(*self.criminal_table.get_children())
            for row in rows:
                self.criminal_table.insert("", END, values=row)
        except Exception as e:
            messagebox.showerror("Error", f"Error searching data: {e}", parent=self.root)


if __name__ == "__main__":
    create_db()
    root = Tk()
    obj  = Criminal(root)
    root.mainloop()