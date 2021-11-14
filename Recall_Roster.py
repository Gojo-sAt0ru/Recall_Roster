import tkinter as tk
app = tk.Tk()

Recall_Elements = {
"First Name": "Larry",
"Last Name": "Fake Last Name",
"Address": "Fake Address",
"Phone #": "Fake Phone",
"Email": "Fake Email"
}


         
label = tk.Label(text="Who Are You Looking For")
label2 = tk.Label(text= "What are you looking for")
entry = tk.Entry()
entry2 = tk.Entry()
button = tk.Button(text= "Search", width= 20, command= lambda: [get_input(), get_2nd_input(), print_it()])

def get_input():
    global entry
    global string
    string= entry.get()
    

   
def get_2nd_input():
    global entry2
    global string2
    string2= entry2.get()

   

def print_it():
    if string in Recall_Elements["First Name"] and string2 in Recall_Elements:
        label3 = tk.Label(text= "You're close")
    label3.pack()


label.pack()
entry.pack()
label2.pack()
entry2.pack()
button.pack()


app.mainloop()
