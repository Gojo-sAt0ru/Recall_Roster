import tkinter as tk

#NameOfPerson = " " 
#function to store name

#function to make searchwindow
def createNewWindow():
    def StoreName():
        newWindow2 = tk.Toplevel(app)
        label2 = tk.Label(newWindow2, text=name_entry.get(),
            foreground="white",
            background='#34A2FE',
            width=50,
            height=10)
        label2.pack()
    newWindow = tk.Toplevel(app)
    name_entry = tk.Entry(newWindow, text="Who are you looking for?")
    button_search = tk.Button(newWindow,
    text="Search",
    width=5,
    height=2,
    bg='blue',
    fg='Red',
    command=StoreName)
    
    name_entry.pack()
    button_search.pack()

    
    

app = tk.Tk()

label = tk.Label(text="What are you trying trying to find?",
    foreground="white",
    background='#34A2FE',
    width=50,
    height=10)
button_Email = tk.Button(
    text="Email",
    width=25,
    height=5,
    bg='blue',
    fg='Red',
    command=createNewWindow
   )
button_Phone = tk.Button(
    text="Phone",
    width=25,
    height=5,
    bg='blue',
    fg='Red',
    command=createNewWindow
    )
button_Address = tk.Button(
    text="Address",
    width=25,
    height=5,
    bg='blue',
    fg='Red',
    command=createNewWindow
    )
#packing main page buttons
label.pack()
button_Email.pack()
button_Phone.pack()
button_Address.pack()


    


app.mainloop()
