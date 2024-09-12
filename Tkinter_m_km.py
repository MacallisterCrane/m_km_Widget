from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)

# #Labels
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=1)
miles_label.config(padx=5, pady=5)

equal_to_label = Label(text="is equal to")
equal_to_label.grid(column=0, row=2)
equal_to_label.config(padx=5, pady=5)

number_label = Label(text="0")
number_label.grid(column=1, row=2)

km_label = Label(text="Km")
km_label.grid(column=2, row=2)


def calculate():
    retrieve = (entry.get())
    km = int(retrieve) * 1.609
    number_label.config(text=km)

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=3)

entry = Entry(width=30)
entry.insert(END, "0")
entry.grid(column=1, row=1)
entry.focus()

window.mainloop()
