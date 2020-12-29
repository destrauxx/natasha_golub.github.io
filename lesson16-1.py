from tkinter import *

root = Tk()
root.title('леха')
# my_label_1 = Label(root, text='Hello World')
# my_label_2 = Label(root, text='My name is Mike')


# my_label_1.grid(row=0, column=0)
# my_label_2.grid(row=1, column=1)

# btn = Button(root, text='You not a haha', padx='100', pady='40', bg='orange', fg='black', bd='5')

# def click_handler():
#     my_label = Label(root, text='Button clicked!')
#     my_label.pack()

# btn = Button(root, text='Click me!', command=click_handler)
# btn.pack()
# entry_field = Entry(root)
# entry_field.pack()

# btn = Button(root, text='click button')
# btn.pack()

# entry_field = Entry(root)
# entry_field.pack()
# def click_handler():
#     entry_text = entry_field.get()
#     my_label = Label(text=f'{entry_text} - your input')
#     my_label.pack()

# btn = Button(root, text='click me', command=click_handler)
# btn.pack()


entry_field = Entry(root, width=40, borderwidth=5)
entry_field.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def click_event(num):
    print('clicked')
    entry_field.insert(50, num)
f_num = None
s_num = None
operand = None

def clear_event():
    global f_num
    global s_num
    global operand
    operand = None
    f_num = None
    s_num = None
    entry_field.delete(0, END)

def add_event():
    global f_num
    global s_num
    global operand
    try:
        if not s_num and isinstance(f_num, int):
            s_num = int(entry_field.get())
        if not f_num:
            f_num = int(entry_field.get()) 
        entry_field.delete(0, END)
    except:
        pass
    operand = '+'

def minus_event():
    global f_num
    global s_num
    global operand
    try:
        if not s_num and isinstance(f_num, int):
            s_num = int(entry_field.get())
        if not f_num:
            f_num = int(entry_field.get()) 
        entry_field.delete(0, END)
    except:
        pass
    operand = '-'
def mult_event():
    global f_num
    global s_num
    global operand
    try:
        if not s_num and isinstance(f_num, int):
            s_num = int(entry_field.get())
        if not f_num:
            f_num = int(entry_field.get()) 
        entry_field.delete(0, END)
    except:
        pass
    operand = '*'

def div_event():
    global f_num
    global s_num
    global operand
    try:
        if not s_num and isinstance(f_num, int):
            s_num = int(entry_field.get())
        if not f_num:
            f_num = int(entry_field.get()) 
        entry_field.delete(0, END)
    except:
        pass
    operand = '/'
def eq_event():
    global f_num
    global s_num
    global operand
    try:
        if not s_num and isinstance(f_num, int):
            s_num = int(entry_field.get())
        entry_field.delete(0, END)
    except:
        pass
    if operand == '+':
        f_num = f_num + s_num
        entry_field.insert(0, f_num)
    elif operand == '-':
        f_num = f_num - s_num
        entry_field.insert(0, f_num)
    elif operand == '*':
        f_num = f_num * s_num
        entry_field.insert(0, f_num)
    elif operand == '/':
        f_num = f_num / s_num
        entry_field.insert(0, f_num)

button_1 = Button(root, text='1', padx=40, pady=20, command=lambda: click_event(1))
button_2 = Button(root, text='2', padx=40, pady=20, command=lambda: click_event(2))
button_3 = Button(root, text='3', padx=40, pady=20, command=lambda: click_event(3))
button_4 = Button(root, text='4', padx=40, pady=20, command=lambda: click_event(4))
button_5 = Button(root, text='5', padx=40, pady=20, command=lambda: click_event(5))
button_6 = Button(root, text='6', padx=40, pady=20, command=lambda: click_event(6))
button_7 = Button(root, text='7', padx=40, pady=20, command=lambda: click_event(7))
button_8 = Button(root, text='8', padx=40, pady=20, command=lambda: click_event(8))
button_9 = Button(root, text='9', padx=40, pady=20, command=lambda: click_event(9))
button_0 = Button(root, text='0', padx=40, pady=20, command=lambda: click_event(0))

def click_handler(event=None):
    assert type(event) == int
    current = entry_field.get()
    entry_field.delete(0, END)
    entry_field.insert(0, str(current) + str(event))

button_add = Button(root, text='+', padx=40, pady=20, command=add_event)
button_minus = Button(root, text='-', padx=40, pady=20, command=minus_event)
button_mult = Button(root, text='*', padx=40, pady=20, command=mult_event)
button_div = Button(root, text='/', padx=40, pady=20, command=div_event)
button_equal = Button(root, text='=', padx=40, pady=20, command=eq_event)
button_clear = Button(root, text='Clear', padx=40, pady=20, command=clear_event)

button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2, sticky='we')
button_equal.grid(row=5, column=1, columnspan=2, sticky='we')
button_add.grid(row=5, column=0)
button_minus.grid(row=6, column=1)
button_mult.grid(row=6, column=0)
button_div.grid(row=6, column=2)


root.mainloop()