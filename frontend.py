import tkinter as t
import backend as db

window = t.Tk()


# *******************
#   Functions
# *******************

def clear_entries():
    in_title.delete(0, t.END)
    in_author.delete(0, t.END)
    in_year.delete(0, t.END)
    in_isbn.delete(0, t.END)


def get_selected_row(event):
    global selected_book

    index = booklist.curselection()[0]
    selected_book = booklist.get(index)

    clear_entries()
    in_title.insert(t.END, selected_book[1])
    in_author.insert(t.END, selected_book[2])
    in_year.insert(t.END, selected_book[3])
    in_isbn.insert(t.END, selected_book[4])


def view_command():
    booklist.delete(0, t.END)
    clear_entries()
    for book in db.view():
        booklist.insert(t.END, book)


def search_command():
    booklist.delete(0, t.END)
    for book in db.search(title.get(), author.get(), year.get(), isbn.get()):
        booklist.insert(t.END, book)


def add_command():
    db.insert(title.get(), author.get(), year.get(), isbn.get())
    clear_entries()
    view_command()


def delete_command():
    db.delete(selected_book[0])
    booklist.delete(0, t.END)
    clear_entries()
    view_command()


def update_command():
    db.update(selected_book[0], title.get(),
              author.get(), year.get(), isbn.get())
    clear_entries()
    view_command()


def close_command():
    window.destroy()
    print("QUITAPP\n")

# *******************
#   Ladbls
# *******************


lab_title = t.Label(text="Title")
lab_author = t.Label(text="Author")
lab_year = t.Label(text="Year")
lab_isbn = t.Label(text="ISBN")

lab_title.grid(row=0, column=0)
lab_author.grid(row=0, column=2)
lab_year.grid(row=1, column=0)
lab_isbn.grid(row=1, column=2)

# ***********************
#   Input Variables
# ***********************

title = t.StringVar()
author = t.StringVar()
year = t.StringVar()
isbn = t.StringVar()

in_title = t.Entry(window, textvariable=title)
in_author = t.Entry(window, textvariable=author)
in_year = t.Entry(window, textvariable=year)
in_isbn = t.Entry(window, textvariable=isbn)

in_title.grid(row=0, column=1)
in_author.grid(row=0, column=3)
in_year.grid(row=1, column=1)
in_isbn.grid(row=1, column=3)

# *******************
#   Listbox
# *******************

booklist = t.Listbox(window, selectmode=1, height=6, width=35)
booklist.grid(row=3, column=0, columnspan=2, rowspan=6)

# Scroll bar

scroll1 = t.Scrollbar(window)
scroll1.grid(row=3, column=2, rowspan=6)

booklist.configure(yscrollcommand=scroll1.set)
scroll1.configure(command=booklist.yview)

booklist.bind('<<ListboxSelect>>', get_selected_row)

# *******************
#   Buttons
# *******************


btn_view = t.Button(window, text="View All", width=12, command=view_command)
btn_view.grid(row=3, column=3)

btn_search = t.Button(window, text="Search Entry",
                      width=12, command=search_command)
btn_search.grid(row=4, column=3)

btn_add = t.Button(window, text="Add Entry", width=12, command=add_command)
btn_add.grid(row=5, column=3)

btn_update = t.Button(window, text="Update", width=12, command=update_command)
btn_update.grid(row=6, column=3)

btn_delete = t.Button(window, text="Delete", width=12, command=delete_command)
btn_delete.grid(row=7, column=3)

btn_close = t.Button(window, text="Close", width=12, command=close_command)
btn_close.grid(row=8, column=3)

btn_close = t.Button(window, text="Clear Fields",
                     width=12, command=clear_entries)
btn_close.grid(row=2, column=2, columnspan=2)


# *******************
view_command()
window.protocol("WM_DELETE_WINDOW", close_command)
window.mainloop()
