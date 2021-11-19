import tkinter as tk
app = tk.Tk()

recall_roster= {
"First Name": "Larry",
"Last Name": "Fake Last Name",
"Address": "Fake Address",
"Phone #": "Fake Phone",
"Email": "Fake Email"
}, {
"First Name": "Megan",
"Last Name": "Fake Last Name",
"Address": "Fake Address",
"Phone #": "Fake Phone",
"Email": "Fake Email"}
    


         
label = tk.Label(text="Who Are You Looking For")
label2 = tk.Label(text= "What are you looking for")
entry = tk.Entry()
entry2 = tk.Entry()
button = tk.Button(text= "Search", width= 20, command= lambda: [get_input(), get_2nd_input(), print_it()])
final = tk.Label()

def get_input():
    global entry
    global string
    string= entry.get()
    

   
def get_2nd_input():
    global entry2
    global string2
    string2= entry2.get()

   

def print_it():
    if string in str(recall_roster):
        final = tk.Label(text= )
        final.pack()


label.pack()
entry.pack()
label2.pack()
entry2.pack()
button.pack()


app.mainloop()
