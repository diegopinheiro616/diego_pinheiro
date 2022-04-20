""" Day 27 Graphical User Interfaces with Tkinter and Function Arguments"""

# ######## History of GUI and Introduction to Tkinter ##########
"""
import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)


# label

my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "italic"))
my_label.pack(side="left")  # <---- Sem essa linha de código, o Label não aparece.
# my_label.pack(expand=True)
# my_label.pack(side="bottom")

# docs.python.org/3/library/tkinter.html

import turtle

tim = turtle.Turtle()
tim.write("I am a Label", font=("Times New Roman", 80, "bold"))

window.mainloop()
"""
# ######## Default Values Quiz ##########
"""
Question 1:
What is the output of this code? 

def foo(a, b=4, c=6): 
    print(a, b, c)
 
foo(1)

Answer: 1 4 6 <---- Correct. Defaults are used for b and c.

Question 2:
What is the output of this code?

def foo(a, b=4, c=6): 
    print(a, b, c)
 
foo(4, 9)

Answer: 4 9 6 <---- Correct. Only c get's a default value.

Question 3:
What is the output of this code?

def foo(a, b=4, c=6): 
    print(a, b, c)
 
foo(1, 7, 9)

Answer: 179 <---- Correct. No default values are used.

Question 4:
What is the output of this code?

def foo(a, b=4, c=6):
    print(a, b, c)
 
foo(20, c=6)

Answer: 20 4 6 <---- Correct. It skips over the argument with a default.
"""
# ######## Many Positional Arguments -  *args ##########
"""
# def add(*args):
# for n in args:
#    print(n)

def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(3, 5, 6, 2, 1))
"""
# ######## Many keyword Arguments -  **kwargs ##########
"""
def calculate(n, **kwargs):
    print(kwargs)  # <---- {'add': 3, 'multiply': 5}
    #for key, value in kwargs.items():
    #    print(key)
    #    print(value)
    n += kwargs["add"]
    n += kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)
"""
# ######## Optional Arguments, *args and **kwargs Quiz ##########
"""
Question 1:
What is the output of this code?

def bar(spam, eggs, toast='yes please!', ham=0):
    print(spam, eggs, toast, ham)
 
bar(1, 2)

Answer: 1 2 'yes please!' 0 <---- The optional arguments, toast and ham, get assigned their default values.

Question 2:
What is the output of this code?

def bar(spam, eggs, toast='yes please!', ham=0):
    print(spam, eggs, toast, ham)
 
bar(toast='nah', spam=4, eggs=2)

Answer: 4 2 'nah' 0 <---- Correct. When keywords are used the order of the arguments listed does not matter. 
                          Python matches by name not position.
                          
Question 3:
def test(*args):
    print(args)
 
test(1,2,3,5)
What is the data type of args?

Answer: Tuple

Question 4:
def test(*args):
    print(args)
 
test(1,2,3,5)

What is the output of the code above?

Answer: (1, 2, 3, 5)

Question 5:
def all_aboard(a, *args, **kw): 
    print(a, args, kw)
 
all_aboard(4, 7, 3, 0, x=10, y=64)


What is the output of the code above? 

Answer: 4 (7, 3, 0) {'x': 10, 'y': 64}
"""
# ######## Buttons, Entry, and Setting Components Options ##########
"""
from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)


# label

my_label = Label(text="I am a Label", font=("Arial", 24, "italic"))
my_label.pack()  # <---- .pack: posição na tela, layout

my_label["text"] = "New Text"
my_label.config(text="Do you want to be rich?")

# Botton

def button_clicked():
    print("Your account have been hack! You lost all your money! Bua.")
    new_text = input.get()
    my_label.config(text=new_text)

button = Button(text="Free Gold", command=button_clicked)
button.pack()

# Entry

input = Entry(width=10)
input.pack()
print(input.get())  # <---- pega o que foi escrito no entry como uma a string.

window.mainloop()
"""
# ######## Other Tkinter Widgets: Radiobuttons, Scales, Checkbuttons and more ##########
"""
from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

#Labels
label = Label(text="This is old text")
label.config(text="This is new text")
label.pack()

#Buttons
def action():
    print("Do something")

#calls action() when pressed
button = Button(text="Click Me", command=action)
button.pack()

#Entries
entry = Entry(width=30)
#Add some text to begin with
entry.insert(END, string="Some text to begin with.")
#Gets text in entry
print(entry.get())
entry.pack()

#Text
text = Text(height=5, width=30)  # <---- Cria um quadro com 5 linhas de texto com largura de 30 caracteres
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")   # <----- Dessa maneira o texto pré-existente se mantem.
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))  # <---- Texto começa da linha um, caractere "0"
text.pack()

#Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
window.mainloop()
"""
# ######## Tkinter Layout Managers: pack(), place() and grid() ##########
"""
from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)  # <---- Adiciona Margems.

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

# label

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New text")
my_label.place(x=0, y=0)

# Botton
button = Button(text="Click me", command=button_clicked)
# button.pack()

button2 = Button(text="New button")
button2.grid(column=2, row=0)

# Entry
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)  # <---- Não pode misturar com o ".pack()"

window.mainloop()
"""
# ######## Mile to Kilometers Converter Project ##########
"""
from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometer_result_label.config(text=f"{km}")

window = Tk()
window.title("Miles to  Kilometer Converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
"""