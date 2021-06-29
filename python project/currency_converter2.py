import requests as requests
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title('Currency converter app')

root.geometry("600x600")

# create tabs
my_notebook = ttk.Notebook(root)
my_notebook.pack(pady=5)   #padding

# create frames
currency_frame = Frame(my_notebook, width=580, height=580)
conversion_frame = Frame(my_notebook, width=580, height=580)

currency_frame.pack(fill="both",expand=1 )
conversion_frame.pack(fill="both",expand=1 )

# add tabs
my_notebook.add(currency_frame,text='currencies')
my_notebook.add(conversion_frame,text='conversion')

# disable 2nd tab

my_notebook.tab(1,state = "disabled")

####################################
# currency staff
##############################
# define lock and unlock

def lock():
    if not home_entry.get() or not conversion_entry.get() or not rate_entry.get():
        messagebox.showwarning('WARNING','You did not fill out all the fields')
    else:    
        # disable entry box
        home_entry.config(state='disabled')
        conversion_entry.config(state='disabled')
        rate_entry.config(state='disabled')
        # enable 2nd tab
        my_notebook.tab(1,state = "normal")

        # change tab fields
        amount_label.config(text=f'Amount of {home_entry.get()} To convert to {conversion_entry.get()}')
        converted_label.config(text=f'Equals this many {conversion_entry.get()}')
        convert_button.config(text=f'Convert from {home_entry.get()} to {conversion_entry.get()}')
    

def unlock():
# enable entry box
    home_entry.config(state='normal')
    conversion_entry.config(state='normal')
    rate_entry.config(state='normal')
    # disable 2nd tab
    my_notebook.tab(1,state = "disabled")

home = LabelFrame(currency_frame, text='Your home currency')
home.pack(pady=20)

# home currency entry box
home_entry = Entry(home,font=('Helvetica',24))
home_entry.pack(pady=10, padx=10)


# conversion currency frame
conversion = LabelFrame(currency_frame,text='conversion currency')
conversion.pack(pady=20)

# convert to label
conversion_label = Label(conversion,text='Currency to convert to...')
conversion_label.pack(pady=10)

# convert to entry
conversion_entry = Entry(conversion,font=('Helvetica',24))
conversion_entry.pack(pady=10,padx=10)

# rate label
rate_label = Label(conversion,text='Current conversion rate...')
rate_label.pack(pady=10)

# rate entry
rate_entry = Entry(conversion,font=('Helvetica',24))
rate_entry.pack(pady=10,padx=10)

# Button frame
button_frame = Frame(currency_frame)
button_frame.pack(pady=20)


# create buttons
lock_button = Button(button_frame,text='Lock',command=lock)
lock_button.grid(row=0, column=0,padx=10)

unlock_button = Button(button_frame,text='UnLock',command=unlock)
unlock_button.grid(row=0, column=1,padx=10)


#########################
#conversion staff
##############

def convert():
    # clear converted box
    converted_entry.delete(0,END)

    # convert
    conversion = float(rate_entry.get()) * float(amount_entry.get())
    # convert to two dps
    conversion = round(conversion,2)
    # add comas to the value
    conversion = '{:,}'.format(conversion)
    # update converted_entry box
    converted_entry.insert(0,conversion)
def clear():
    amount_entry.delete(0, END)
    converted_entry.delete(0, END)


amount_label = LabelFrame(conversion_frame, text='Amount to convert..')
amount_label.pack(pady=20)

# entry box for amount
amount_entry = Entry(amount_label,font=('Helvetica',24))
amount_entry.pack(pady=10,padx=10)


# convert button
convert_button = Button(amount_label,text='Convert',command=convert)
convert_button.pack(pady=20)

# equals frame
converted_label = LabelFrame(conversion_frame, text='Converted currency')
converted_label.pack(pady=20)

# converted entry
converted_entry = Entry(converted_label,font=('Helvetica',24),bd=0,background='grey')
converted_entry.pack(pady=10,padx=10)

# clear button
clear_button = Button(conversion_frame,text='Clear',command=clear)
clear_button.pack(pady=20)


# fake label for spacing
spacer = Label(conversion_frame,text='',width=68)
spacer.pack()








root.mainloop()
