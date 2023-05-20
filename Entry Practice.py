from tkinter import *
from PIL import Image,ImageTk


window = Tk()

def search():
    print("Searching for channel name " + entry.get() + "...")

def dlt():
    entry.delete(0,END)
    print("Deleted Input.")

def back():
    entry.delete(len(entry.get())-1,END)

logo = ImageTk.PhotoImage(Image.open("ytlogo.png"))
label = Label(window,image=logo)
label.pack(side=LEFT)

icon = PhotoImage(file="ytlogo.png")
search_icon = PhotoImage(file="search.png")
window.iconphoto(True,icon)
window.title("Youtube Search")
window.config(bg="red")

entry = Entry(window,
              font=("Ariel",50,"italic","bold"),
              bg="red",
              relief=SUNKEN,
              bd=20)
entry.insert(0,"Search")
entry.pack(side=LEFT)

search_button = Button(window,
                       image=search_icon,
                       font=("Ariel",20,"italic"),
                       bg="gray",
                       activebackground="gray",
                       command=search)
search_button.pack(side=RIGHT)

delete_button = Button(window,
                       text="DELETE",
                       font=("Ariel",20,"italic"),
                       bg="gray",
                       activebackground="gray",
                       command=dlt)
delete_button.pack(side=RIGHT)

backspace_button = Button(window,
                       text="BACKSPACE",
                       font=("Ariel",20,"italic"),
                       bg="gray",
                       activebackground="gray",
                       command=back)
backspace_button.pack(side=RIGHT)

window.mainloop()