import tkinter as tk
app = tk.Tk()

recall_roster= [{
"First Name": "Larry",
"Last Name": "Fake Last Name",
"Address": "Fake Address",
"Phone #": "Fake Phone",
"Email": "Fake Email"
}, {
"First Name": "Megan",
"Last Name": "Fake Last Name",
"Address": "Fake Address",
"Phone #": "Fake Phone2",
"Email": "Fake Email"}]

#Recall_People["Larry", "Megan"]
    
label = tk.Label(text="Who Are You Looking For")
label2 = tk.Label(text= "What are you looking for")
entry = tk.Entry()
entry2 = tk.Entry()
button = tk.Button(text= "Search", width= 20, command= lambda: [get_input(), get_2nd_input(), converter(), print_it()])

def converter(): # Converting the string input to the index so that it can be returned 
    global user_input
    for i in recall_roster:
        if string in i:
            user_input = i[str(string2)]




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
        finalz = tk.Label(text= user_input)
        finalz.pack()
    

        
                


label.pack()
entry.pack()
label2.pack()
entry2.pack()
button.pack()


app.mainloop()
