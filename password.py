import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Meine Website")
root.geometry("300x300")

def registration():
    global root1
    root1 = tk.Toplevel(root)
    root1.title("Regestrierung")
    root1.geometry("300x250")

    global username, password
    username = tk.StringVar()
    password = tk.StringVar()

    #username schaltfläche
    tk.Label(root1, text="Registrieren", bg="grey", fg="black", font="bold", width=300).pack()
    tk.Label(root1, text="").pack()
    tk.Label(root1, text="Benutzername :", font="bold").pack()
    username_entry = tk.Entry(root1, textvariable=username).pack()

    #passwort schaltfläche
    tk.Label(root1, text="").pack()
    tk.Label(root1, text="Passwort :", font="bold").pack()
    pssword_entry = tk.Entry(root1, textvariable=password).pack()

    #Register Button
    tk.Label(root1, text="").pack()
    tk.Button(root1, text="Regestrieren", bg="red", command=register_user).pack() 

def register_user():
    username_info = username.get()
    password_info = password.get()

    if username_info == "" or password_info == "":
        messagebox.showerror("Fehler", "Bitte füllen Sie alle Felder aus.")
        return
    db = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="your_database"
    )
    mycur = db.cursor()
    sql = "INSERT INTO login (user, password) VALUES (%s, %s)"
    t = (username_info, password_info)
    mycur.execute(sql, t)
    db.commit()
    db.close()

    messagebox.showinfo("Erfolg", "Regestrierung erfolgreich!")
    root1.destroy()

registration()

root.mainloop()
