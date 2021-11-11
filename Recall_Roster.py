import tkinter as tk
app = tk.Tk()

Recall_Elements = {
"FName": "Fake First Name",
"LName": "Fake Last Name",
"Address": "Fake Address",
"Phone #": "Fake Phone",
"Email": "Fake Email"
}

def get_input():
    global entry
    string= entry.get()
    if string in Recall_Elements["FName"]:
        label2 = tk.Label(text= Recall_Elements)
        label2.pack()
         
label = tk.Label(text="Who Are You Looking For",
    foreground="white",
    background='#34A2FE',
    width=30,
    height=10)
entry = tk.Entry()
button = tk.Button(text= "Search", width= 20, command=get_input)


label.pack()
entry.pack()
button.pack()


app.mainloop()
