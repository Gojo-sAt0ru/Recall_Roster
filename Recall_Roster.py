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

def get_input(): # grabs name input from UI
    global entry
    global string
    string= entry.get()
    
def get_2nd_input(): # grabs what input element of the dictionary 
    global entry2
    global string2
    string2= entry2.get()

def print_it(): # Eventually will print result to screen
    if string in str(recall_roster):
        final = tk.Label(text= recall_roster)
        final.pack()

def converter(string, string2): # Converting the string input to the index so that it can be returned 
    for i in recall_roster:
        for j in i:
            if str(j) == str(string):
                return 

label.pack()
entry.pack()
label2.pack()
entry2.pack()
button.pack()


app.mainloop()

