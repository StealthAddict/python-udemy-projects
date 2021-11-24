# Setting up a GUI w/ widgets

from tkinter import *  #from tkinter import all

"""
window = Tk()
# create widgets inbetween ^ and window.mainloop()

def km_to_miles():
    miles = float(e1_value.get())*1.6
    t1.insert(END, miles)

# Button widget
b1 = Button(window, text="Execute", command= km_to_miles)
b1.grid(row=0, column=1, rowspan=2) # or b1.pack()

# Entry widget
e1_value = StringVar()
e1 = Entry(window, textvariable= e1_value)
e1.grid(row=0, column=0)

# Text widget
t1 = Text(window, height=1, width=15)
t1.grid(row=1, column= 0)

window.mainloop()
"""

# Practice GUI

converter = Tk()

def kg_to():
    grams = float(e_evalue.get()) * 1000
    text_1.delete("1.0", END)   # Deletes the content of the text box before new input
    text_1.insert(END, grams)

    pounds = float(e_evalue.get()) * 2.20462
    text_2.delete("1.0", END)
    text_2.insert(END, pounds)

    ounces = float(e_evalue.get()) * 35.274
    text_3.delete("1.0", END)
    text_3.insert(END, ounces)


# Convert button using kg_to function to distribute output
b_convert = Button(converter, text="Convert", command= kg_to)
b_convert.grid(row=0, column=2)

# Puts the label, "Kg"
e_label = Label(converter, text="Kg")
e_label.grid(row=0, column=0)

# Entry gets the input
e_evalue = StringVar()
e_entry = Entry(converter, textvariable= e_evalue)
e_entry.grid(row=0, column=1)

# To grams
text_1 = Text(converter, height=1, width=15)
text_1.grid(row=1, column=0)

# To pounds
text_2 = Text(converter, height=1, width=15)
text_2.grid(row=1, column=1)

# To ounces
text_3 = Text(converter, height=1, width=15)
text_3.grid(row=1, column=2)

converter.mainloop()