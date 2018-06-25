from tkinter import  *
from tkinter import messagebox, ttk
from datetime import datetime as dt
import time as t
from backend import Database

db = Database("books.db")

def showClock():
    date = "Date: " + str(dt.today().day) + "/" + str(dt.today().month) + "/" + str(dt.today().year)
    dateLabel.configure(text = date)

    time = "Time:" + t.strftime('%H:%M:%S')
    timeLabel.configure(text = time)

    window.after(1, showClock)

def getSelectedRow(event):
    global selectedRow
    index = listBox.curselection()[0]
    selectedRow = listBox.get(index)

    titleEntry.delete(0, END)
    authorEntry.delete(0, END)
    yearEntry.delete(0, END)
    isbnEntry.delete(0, END)

    titleEntry.insert(END, selectedRow[1])
    authorEntry.insert(END, selectedRow[2])
    yearEntry.insert(END, selectedRow[3])
    isbnEntry.insert(END, selectedRow[4])

def view():
    listBox.delete(0, END)
    for row in db.viewData():
        listBox.insert(END, row)

def search():
    listBox.delete(0, END)
    for row in db.searchData(title.get(), author.get(), year.get(), isbn.get()):
        listBox.insert(END, row)

def insert():
    db.insertData(title.get(), author.get(), year.get(), isbn.get())
    view()

def delete():
    db.deleteData(selectedRow[0])
    titleEntry.delete(0, END)
    authorEntry.delete(0, END)
    yearEntry.delete(0, END)
    isbnEntry.delete(0, END)
    view()

def update():
    db.updateData(selectedRow[0], title.get(), author.get(), year.get(), isbn.get())
    view()

if __name__=='__main__':

    window = Tk()
    window.title("Book Records")
    window.geometry(newGeometry = "600x425+650+200")

    titleLabel = Label(window, text = "Title")
    titleLabel.place(x=35, y=25)

    title = StringVar()
    titleEntry = Entry(window, textvariable=title)
    titleEntry.place(x=90, y=25)
    
    authorLabel = Label(window, text = "Author")
    authorLabel.place(x=260, y=25)

    author = StringVar()
    authorEntry = Entry(window, textvariable=author)
    authorEntry.place(x=325, y=25)
    
    yearLabel = Label(window, text = "Year")
    yearLabel.place(x=35, y=75)

    year = StringVar()
    yearEntry = Entry(window, textvariable=year)
    yearEntry.place(x=90, y=75)
    
    isbnLabel = Label(window, text = "ISBN")
    isbnLabel.place(x=260, y=75)

    isbn = StringVar()
    isbnEntry = Entry(window, textvariable=isbn)
    isbnEntry.place(x=325, y=75)

#======================================================Date & Time Label========================================================

    dateLabel = Label(window)
    dateLabel.place(x=475, y=25)

    timeLabel = Label(window)
    timeLabel.place(x=475, y=75)

#===========================================================Separators===========================================================
    
    hseparator = ttk.Separator(window, orient = 'horizontal')
    hseparator.place(x=0, y=125, width=450)

    vseparator = ttk.Separator(window, orient = 'vertical')
    vseparator.place(x=450, y=125, height=325)

#=========================================Adding Buttons to the UI===============================================#
    viewAllBtn = Button(window, text="View All Books", command=view)
    viewAllBtn.place(x=475, y=125, width=100)

    searchBtn = Button(window, text="Search Book", command=search)
    searchBtn.place(x=475, y=175, width=100)

    insertBtn = Button(window, text="Add Book", command=insert)
    insertBtn.place(x=475, y=225, width=100)

    updateBtn = Button(window, text="Update Book", command=update)
    updateBtn.place(x=475, y=275, width=100)

    deleteBtn = Button(window, text="Delete Book", command=delete)
    deleteBtn.place(x=475, y=325, width=100)

    closeBtn = Button(window, text="Close Program", command=window.destroy)
    closeBtn.place(x=475, y=375, width=100)

#=======================================================List Box==================================================
    listBox = Listbox(window, height = 18, width = 70)
    listBox.place(x=6, y=130)

    scrollbar = Scrollbar(window)
    scrollbar.place(x=430, y=130)

    listBox.configure(yscrollcommand = scrollbar.set)
    scrollbar.configure(command=listBox.yview)

    listBox.bind('<<ListboxSelect>>', getSelectedRow)

    window.after(0, showClock)
    window.mainloop()