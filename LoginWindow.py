from tkinter import *
from tkinter import ttk
from tkinter import simpledialog
from PIL import Image, ImageTk      # Importing PIL for image handling
from tkinter import messagebox
import csv


class LoginWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Login")
        self.master.geometry("1300x1150")
        self.bg=ImageTk.PhotoImage(file="Criminal Management/bg.webp")  # Load the background image
        lbl_bg=Label(self.master,image=self.bg)  # Create a label to hold the background image
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)  # Place the label to cover the entire window

        # Create a frame for the login form
        frame = Frame(self.master, bg="sky blue")
        frame.place(x=400, y=100, width=500, height=500)

        # Load and display the login image
        img1=ImageTk.PhotoImage(file="Criminal Management/logo1.png")    # Load the login image
        img1 = img1.resize((100, 100), Image.LANCZOS)  # LANCZOS is a high-quality downsampling filter
        self.logo = ImageTk.PhotoImage(img1)  # Convert to PhotoImage
        logo_label = Label(frame, image=self.logo, bg="sky blue")   # Create a label to hold the login image
        logo_label.pack(pady=10)

        get_str=Label(frame, text="Database Login", font=("times new roman", 20, "bold"), bg="sky blue", fg="yellow")  # Create a label for "Get Started"
        get_str.pack(pady=10)

        username=Label(frame, text="Username", font=("times new roman", 15, "bold"), bg="sky blue", fg="black")  # Create a label for "Username"
        username.place(x=130, y=170)
        self.txtuser=ttk.Entry(frame, font=("times new roman", 15))  # Create an entry for username input
        self.txtuser.place(x=120, y=200, width=250)

        password=Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="sky blue", fg="black")  # Create a label for "Password"
        password.place(x=130, y=250)
        self.txtpass=ttk.Entry(frame, font=("times new roman", 15), show="*")  # Create an entry for password input
        self.txtpass.place(x=120, y=280, width=250)

        # Icons for the username and password fields
        img2 = Image.open("username_icon.jpg")  # Load the username icon image
        img2 = img2.resize((25, 25), Image.LANCZOS)     # Resize the image to fit the entry field
        self.user_icon = ImageTk.PhotoImage(img2)     # Convert the image to a PhotoImage object for use in Tkinter
        user_icon_label = Label(frame, image=self.user_icon, bg="sky blue") # Create a label to hold image and set it's parameters
        user_icon_label.place(x=100, y=170)

        # Display the password icon next to the password entry
        img3 = Image.open("password_icon.png")
        img3 = img3.resize((25, 25), Image.LANCZOS)
        self.password_icon = ImageTk.PhotoImage(img3)
        password_icon_label = Label(frame, image=self.password_icon, bg="sky blue")
        password_icon_label.place(x=100, y=250)

        # Button for login
        login_btn = Button(frame, text="Login", font=("times new roman", 15, "bold"), bg="black", fg="gold", relief=RIDGE, command=self.login)
        login_btn.place(x=120, y=320, width=200)

        # Register new user button
        register_btn = Button(frame, text="Register New User", font=("times new roman", 15, "bold"), bg="gold", fg="red", relief=RIDGE, command=self.register)
        register_btn.place(x=120, y=370, width=200)

        # Forgot password button
        forgot_btn = Button(frame, text="Forgot Password?", font=("times new roman", 10, "bold"), bg="sky blue", activebackground="sky blue", fg="blue", activeforeground="blue", relief=FLAT, command=self.forgot_password)
        forgot_btn.place(x=120, y=420)

    # Function to handle login button click
    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields are required")
            return
        try:
            found = False
            with open("users.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0].strip() == self.txtuser.get().strip() and row[1].strip() == self.txtpass.get().strip():
                        found = True
                        break
            if found:
                self.master.destroy()        # Close login window first
                import main
                root2 = Tk()                 # Create a new window
                obj = main.Criminal(root2)   # Pass new window to Criminal
                root2.mainloop()             # Start the new window's loop
            else:
                messagebox.showerror("Error", "Invalid username or password")
        except FileNotFoundError:
            messagebox.showerror("Error", "No users registered yet")

    # Function to handle register new user button click
    def register(self):
        register_window = Toplevel(self.master)
        register_window.title("Register New User")
        register_window.geometry("400x400")
        Label(register_window, text="Enter Username", font=("times new roman", 15, "bold")).place(x=50, y=50)
        txtuser = ttk.Entry(register_window, font=("times new roman", 15))
        txtuser.place(x=50, y=80)
        Label(register_window, text="Enter Password", font=("times new roman", 15, "bold")).place(x=50, y=110)
        txtpass = ttk.Entry(register_window, font=("times new roman", 15), show="*")
        txtpass.place(x=50, y=140)
        security_ques=Label(register_window, text="Security Question", font=("times new roman", 10, "bold")).place(x=50, y=170)
        box=ttk.Combobox(register_window, font=("times new roman", 10), state="readonly")
        box["values"]=("Select","What is your pet's name?","What is your favorite color?","What is your favorite food?")
        box.current(0)
        box.place(x=50, y=200)
        Label(register_window, text="Enter Answer", font=("times new roman", 15, "bold")).place(x=50, y=230)
        txtanswer = ttk.Entry(register_window, font=("times new roman", 15))
        txtanswer.place(x=50, y=260)

        def save_user():
            if txtuser.get() == "" or txtpass.get() == "" or txtanswer.get() == "":
                messagebox.showerror("Error", "All fields are required")
                return
            with open("users.csv", "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([txtuser.get().strip(), txtpass.get().strip(), txtanswer.get().strip()])
            messagebox.showinfo("Success", "User registered successfully")
            register_window.destroy()
        Button(register_window, text="Register", font=("times new roman", 15, "bold"), bg="red", fg="yellow", relief=RIDGE, command=save_user).place(x=50, y=290)

    # Function to handle forgot password button click
    def forgot_password(self):
        if self.txtuser.get() == "":
            messagebox.showerror("Error", "Please enter your username to reset password")
            return
        try:
            found = False
            with open("users.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0].strip() == self.txtuser.get().strip():
                        found = True
                        break
            if found:
                answer = simpledialog.askstring("Security Question", "What is your answer to the security question?")
                if answer and answer.strip() == row[2].strip():
                    new_password = simpledialog.askstring("Reset P/W", "Enter your new password:", show="*")
                    if new_password:
                        users = []
                        with open("users.csv", "r") as file:
                            reader = csv.reader(file)
                            for user in reader:
                                if user[0].strip() == self.txtuser.get().strip():
                                    users.append([user[0].strip(), new_password.strip(), user[2].strip()])
                                else:
                                    users.append(user)
                        with open("users.csv", "w", newline="") as file:
                            writer = csv.writer(file)
                            writer.writerows(users)
                        messagebox.showinfo("Success", "Password reset successfully")
                    else:
                        messagebox.showerror("Error", "Password cannot be empty")
                else:
                    messagebox.showerror("Error", "Incorrect answer to security question")
            else:
                messagebox.showerror("Error", "Username not found")
        except FileNotFoundError:
            messagebox.showerror("Error", "No users registered yet")



if __name__ == "__main__":
    root = Tk()
    app = LoginWindow(root)
    root.mainloop()