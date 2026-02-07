from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_text = website_entry.get()
    email_text = email_entry.get()
    password_text = password_entry.get()

    if website_text == "" or password_text == "":
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_okay = messagebox.askokcancel(title=website_text, message=f"These are the details entered: \nEmail: {email_text}"
                                                       f"\nPassword: {password_text} \nClick OK to save or Cancel to cancel")

        if is_okay:
            with open("data.txt", "a") as file:
                file.write(f"{website_text} | {email_text} | {password_text}\n")

            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

# Display logo.png onto the canvas in tkinter
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Display all labels
website_title = Label(text="Website:", bg="white")
website_title.grid(column=0, row=1)

email_username = Label(text="Email/Username:", bg="white")
email_username.grid(column=0, row=2)

password_title = Label(text="Password:", bg="white")
password_title.grid(column=0, row=3)

# Display the entry fields
website_entry = Entry(width=60)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=60)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "yuna@email.com")

password_entry = Entry(width=41)
password_entry.grid(column=1, row=3)

# Display the buttons
password_button = Button(text="Generate Password")
password_button.grid(column=2, row=3)

add_button =Button(text="Add", width=50, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()