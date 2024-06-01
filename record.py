from tkinter import *
from db import Database
from tkinter import messagebox
import time

db = Database('deposit.db')

window = Tk()



def populate():
    records.delete(0, END)
    for row in db.fetch():
        records.insert(END, row)


def select_items(event):
    try:

        global selected_item
        index = records.curselection()[0]
        selected_item = records.get(index)

        acc_no_entry.delete(0, END)
        acc_no_entry.insert(END, selected_item[1])

        acc_name_entry.delete(0, END)
        acc_name_entry.insert(END, selected_item[2])

        bank_name_entry.delete(0, END)
        bank_name_entry.insert(END, selected_item[3])

        price_entry.delete(0, END)
        price_entry.insert(END, selected_item[4])

        from_entry.delete(0, END)
        from_entry.insert(END, selected_item[5])

        status_entry.delete(0, END)
        status_entry.insert(END, selected_item[6])

    except IndexError:
        pass


def add_records():
    if acc_no_text.get() == '' or acc_name_text.get() == '' or bank_name_text.get() == '':
        messagebox.showerror('Field Required', 'Fill in the blank space!')
        return

    formatted_price = f'{int(price_text.get()):,}'

    db.insert(acc_no_text.get(), acc_name_text.get(), bank_name_text.get(), formatted_price, from_text.get(),
              time.ctime())
    records.delete(0, END)
    records.insert(END, acc_no_text.get(), acc_name_text.get(), bank_name_text.get(), price_text.get(), from_text.get())

    clear()
    populate()


def remove_records():
    try:

        db.remove(selected_item[0])
        clear()
        populate()

    except NameError:
        messagebox.showerror('Invalid', 'Select an item to be removed!')


def update_records():
    try:

        db.update(selected_item[0], acc_no_text.get(), acc_name_text.get(), bank_name_text.get(), price_text.get(),
                  from_text.get())
        clear()
        populate()

    except NameError:
        messagebox.showerror('Invalid', 'Select an item to be updated!')


def approve_records():
    if from_text.get() == '':
        messagebox.showerror('Invalid', 'specify the bank approving from !')
        return

    try:

        db.approve(selected_item[0], from_text.get())
        clear()
        populate()

    except NameError:
        messagebox.showerror('Invalid', 'Select an item to be approved!')


def clear():
    acc_no_entry.delete(0, END)
    acc_name_entry.delete(0, END)
    bank_name_entry.delete(0, END)
    price_entry.delete(0, END)
    from_entry.delete(0, END)
    status_entry.delete(0, END)



acc_no_text = StringVar()
acc_no_label = Label(window, text='ACCOUNT NO.', font=('blod', 13), fg='#323')
acc_no_label.grid(row=1, column=0, pady=20, sticky=W)
acc_no_entry = Entry(window, textvariable=acc_no_text, border=0)
acc_no_entry.focus()
acc_no_entry.grid(row=1, column=1, padx=10)

acc_name_text = StringVar()
acc_name_label = Label(window, text='ACCOUNT NAME', font=('blod', 13))
acc_name_label.grid(row=1, column=2, sticky=W)
acc_name_entry = Entry(window, textvariable=acc_name_text, border=0)
acc_name_entry.grid(row=1, column=3)

bank_name_text = StringVar()
bank_name_label = Label(window, text='BANK NAME.', font=('blod', 13))
bank_name_label.grid(row=1, column=4, sticky=W)
bank_name_entry = Entry(window, textvariable=bank_name_text, border=0)
bank_name_entry.grid(row=1, column=5)

price_text = StringVar()
price_label = Label(window, text='AMOUNT', font=('blod', 13))
price_label.grid(row=2, column=0, sticky=W)
price_entry = Entry(window, textvariable=price_text, border=0)
price_entry.grid(row=2, column=1)

from_text = StringVar()
from_label = Label(window, text='VIA', font=('blod', 13))
from_label.grid(row=2, column=2, sticky=W)
from_entry = Entry(window, textvariable=from_text, border=0)
from_entry.grid(row=2, column=3)

status_text = StringVar()
status_label = Label(window, text='STATUS', font=('blod', 13))
status_label.grid(row=2, column=4, sticky=W)
status_entry = Entry(window, textvariable=status_text, border=0)
status_entry.grid(row=2, column=5)

records = Listbox(window, width=130, height=25, border=0, bg='#232', fg='white', font=('bold', 11))
records.grid(row=4, column=0, columnspan=5, rowspan=8, pady=60, padx=30)
records.bind('<<ListboxSelect>>', select_items)

scrollbar = Scrollbar(window)
scrollbar.grid(row=5, column=4)

records.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=records.yview)

add_btn = Button(window, text='ADD', width=14, command=add_records, border=-1, bg='#bbb', fg='green', font=('bold', 11))
add_btn.grid(row=4, column=1, sticky=W)

remove_btn = Button(window, text='REMOVE', width=14, command=remove_records, border=-1, bg='#bbb', fg='red', font=('bold', 11))
remove_btn.grid(row=4, column=2, sticky=W)

update_btn = Button(window, text='UPDATE', width=14, command=update_records, border=-1, bg='#bbb', fg='#333', font=('bold', 11))
update_btn.grid(row=4, column=3, sticky=W)

approve_btn = Button(window, text='APPROVE', width=14, command=approve_records, border=-1, bg='#bbb', fg='#191', font=('bold', 11))
approve_btn.grid(row=4, column=4, sticky=W)

window.title('DEPOSITING RECORD')
window.geometry('1366x768')

populate()

window.mainloop()

