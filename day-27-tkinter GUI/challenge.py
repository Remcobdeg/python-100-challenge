from tkinter import *

FONT = ("Arial",24,"normal")

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20,pady=20) #padding per widget

#Miles label
miles_label = Label(text="Miles")
miles_label.grid(column=3,row=1) #side="bottom" #expand=True #tries to take up whole space of the screen (in this case means centring it)

#KM label
km_label = Label(text="Km")
km_label.grid(column=3,row=2) #side="bottom" #expand=True #tries to take up whole space of the screen (in this case means centring it)

#outcome label
outcome_label = Label(text="0")
outcome_label.grid(column=2,row=2) #side="bottom" #expand=True #tries to take up whole space of the screen (in this case means centring it)

#equal label
equal_label = Label(text="is equal to")
equal_label.grid(column=1,row=2) #side="bottom" #expand=True #tries to take up whole space of the screen (in this case means centring it)


#calculate button
def miles_to_km():
    outcome_label["text"] = round(float(input_field.get())*1.6)
button = Button(text="Calculate", command=miles_to_km)
button.grid(column=2,row=3)

#Entry
#options: https://tcl.tk/man/tcl8.6/TkCmd/entry.htm
input_field = Entry()
input_field.config(width=10)
input_field.grid(column=2,row=1)


window.mainloop() #keep the window open
