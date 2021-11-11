import tkinter as tk
app = tk.Tk()

Recall_Roster = {
""


}

def get_input():
    global entry
    string= entry.get()
    

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
