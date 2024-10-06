from tkinter import *

#https://docs.python.org/3/library/tkinter.html#setting-options
#https://tcl.tk/man/tcl8.6/TkCmd/contents.htm

window = Tk()
window.title("GUI program with Tkxinter")
window.minsize(width=500, height=300)
window.config(padx=20,pady=20) #padding per widget

#label
my_label = Label(text="I'm a label", font=("Arial",24,"bold"))
my_label.grid(column=1,row=1) #side="bottom" #expand=True #tries to take up whole space of the screen (in this case means centring it)

#button
def button_clicked():
    my_label["text"] = input_field.get()
button = Button(text="click me", command=button_clicked)
button.grid(column=2,row=2)

#button2
button2 = Button(text="click me", command=button_clicked)
button2.grid(column=3,row=1)

#Entry
#options: https://tcl.tk/man/tcl8.6/TkCmd/entry.htm
input_field = Entry()
input_field.config(width=10)
input_field.grid(column=4,row=3)

#pack places items sequentially (eg, top to bottom) -- not precise
#place: allows x,y -- needs to be used for all or others won't appear -- super specific
#grid: can divide in any number of columns and rows -- hierarchically relative to other components -- can't mix grid and pack



window.mainloop() #keep the window open
