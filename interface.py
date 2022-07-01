from tkinter import *


ws = Tk()
ws.title('PythonGuides')
ws.config(bg='#0B5A81')

f = ('Times', 14)
var = StringVar()
var.set('male')

right_frame = Frame(
    ws,
    bd=2,
    bg='#CCCCCC',
    relief=SOLID,
    padx=10,
    pady=10
)

Label(
    right_frame,
    text="Enter Name",
    bg='#CCCCCC',
    font=f
).grid(row=0, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="Enter Password",
    bg='#CCCCCC',
    font=f
).grid(row=5, column=0, sticky=W, pady=10)

register_name = Entry(
    right_frame,
    font=f
)

register_pwd = Entry(
    right_frame,
    font=f,
    show='*'
)

register_btn = Button(
    right_frame,
    width=15,
    text='Register',
    font=f,
    relief=SOLID,
    cursor='hand2',
    command=lambda: callback_function())


login_btn = Button(
    right_frame,
    width=15,
    text='Login',
    font=f,
    relief=SOLID,
    cursor='hand2',
    command=lambda: callback_function2())


def callback_function():
    print("register")
    import credsavig
    # do something


def callback_function2():
    print("login")
    # do something


register_name.grid(row=0, column=1, pady=10, padx=20)


register_pwd.grid(row=5, column=1, pady=10, padx=20)


login_btn.grid(row=7, column=0, pady=10, padx=20)
register_btn.grid(row=7, column=1, pady=10, padx=20)
right_frame.pack()
ws.mainloop()
