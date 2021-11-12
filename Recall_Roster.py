import tkinter as tk
app = tk.Tk()

Recall_Elements = {
"First Name": "Larry",
"Last Name": "Fake Last Name",
"Address": "Fake Address",
"Phone #": "Fake Phone",
"Email": "Fake Email"
}

def get_input():
    global entry
    string= entry.get()
    if string in Recall_Elements["First Name"]:
        label2 = tk.Label(text= Recall_Elements["Address"])
        label2.pack()
         
label = tk.Label(text="Who Are You Looking For")
label2 = tk.Label(text= "What are you looking for")
entry = tk.Entry()
entry2 = tk.Entry()
button = tk.Button(text= "Search", width= 20, command=get_input)


label.pack()
entry.pack()
label2.pack()
entry2.pack()
button.pack()


app.mainloop()
