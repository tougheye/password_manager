from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pw_letter = [choice(letters) for i in range(randint(8, 10))]
    pw_number = [choice(numbers) for i in range(randint(4, 6))]
    pw_symbol = [choice(symbols) for i in range(randint(2, 4))]

    password_list = pw_letter + pw_number + pw_symbol
    shuffle(password_list)

    # pw = ""
    # for i in password_list:
    #     pw += i
    pw = "".join(password_list)
    pw_box.insert(0, pw)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_passwd():
    website = web_box.get()
    email = email_box.get()
    passwd = pw_box.get()

    if len(website) == 0 or len(email) == 0 or len(passwd) == 0:
        messagebox.showerror(title="Ooops", message="Please don't leave any field empty")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\n"
                                                              f"Email: {email}\nPassword:{passwd}\nIs it okay to save?")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"\n{website} | {email} | {passwd}")
                web_box.delete(0, END)
                pw_box.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

web_label = Label(text="Website:")
web_label.grid(column=0, row=1)

web_box = Entry(width=36)
web_box.grid(columnspan=2, column=1, row=1)
web_box.focus()

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_box = Entry(width=36)
email_box.grid(columnspan=2, column=1, row=2)
email_box.insert(0, "mkamin.6696@gmail.com")

pw_label = Label(text="Password:")
pw_label.grid(column=0, row=3)

pw_box = Entry(width=21)
pw_box.grid(column=1, row=3)

gpw_button = Button(text="Generate Password", command=password_generator)
gpw_button.grid(column=2, row=3)

add_button = Button(text="Add", width=35, command=save_passwd)
add_button.grid(column=1, columnspan=2, row=4)

window.mainloop()
