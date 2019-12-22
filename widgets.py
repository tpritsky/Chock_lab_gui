#!/usr/bin/python

from tkinter import Tk, Label, Button, W, E, StringVar, OptionMenu, Radiobutton, IntVar, Checkbutton
import pandas as pd
import datetime
import tkMessageBox
from tkFileDialog   import askopenfilename, askopenfilenames

class MyFirstGUI:
    def __init__(self, master):
        
        self.master = master
        master.title("A simple GUI")

        '''functions:
            --------------------------------------------------------------------------------'''
        def callback():
            filez = askopenfilenames(parent=root,title='Choose a file')
            lst = list(filez)
            #name= askopenfilename()
            print (lst)

        def greet():
            print("Greetings!")

        #submit parameters
        def submit_function():
            print("hello world")
            for i in self.list_columns_selected:
                print(i.get())

        '''variables:
            ---------------------------------------------------------------------------------'''

        OPTIONS = [
                   "12hr",
                   "24hr",
                   ] #etc
            
        variable = StringVar(master)
        variable.set(OPTIONS[0]) # default value
        var = IntVar() #variable for radiobutton


        self.list_columns_selected = [] #stores list of columns for analysis
        min_time = datetime.datetime(2013,11, 28, 0) #earliest date from which to report data
        max_time = datetime.datetime(2013,11,28, 7) #latest date from which to report data

        num_hours_for_avg = 2 #number of hours to average data over
        min_number_of_entries = 1 #minimum number of nonzero entries to calculate average; otherwise return average of zero

        data_columns = ["value1", "value2", "value3"]   #column names from the dataset

        '''widgets:
           ----------------------------------------------------------------------------------'''

        #Title
        self.label1 = Label(master, text="Welcome to the GUI...")
        self.label1.grid(row=0, sticky = W)

        #Description
        self.label2 = Label(master, text="Description: This is a generic GUI that allows the user to upload a file and set parameters.")
        self.label2.grid(columnspan = 4, sticky= W, row = 3)

        #parameters title
        self.label3 = Label(master, text = "Parameters: ")
        self.label3.grid(sticky= W, row = 5)

        #Variables of interest array button
        self.R1 = Radiobutton(master, text="Cerebral Saturation", variable=var, value=1,
                             command=greet)
        self.R1.grid(row = 7, sticky = W, padx=30)

        self.R2 = Radiobutton(master, text="Renal Saturation", variable=var, value=2,
                             command=greet)
        self.R2.grid(row = 8, sticky = W, padx=30)

        self.R3 = Radiobutton(master, text="Other", variable=var, value=3,
                             command=greet)
        self.R3.grid(row = 9, sticky = W, padx=30)

        #Time period title
        self.label3 = Label(master, text = "2. Time Period: ")
        self.label3.grid(sticky= W, row = 10)

        #Time period explanation
        self.label3 = Label(master, text = "Little challenging to implement...can do later")
        self.label3.grid(sticky= W, columnspan = 3, row = 11, padx=20)

        #Frequency title
        self.label3 = Label(master, text = "3. Frequency: ")
        self.label3.grid(sticky= W, row = 12)

        #Frequency dropdown menu
        self.dropdown1 = OptionMenu(master, variable, *OPTIONS)
        self.dropdown1.grid(sticky= W, row=13, padx=20)

        #File upload Title
        self.label3 = Label(master, text = "File Uploads: ")
        self.label3.grid(sticky= W, row = 14)


        #File Upload Widget
        self.uploadFileButton = Button(master, text ="Upload", command = callback)
        self.uploadFileButton.grid(row=14, padx = 40)

        #check button variables of interest widget

        #listof var names
        var_names = ["Csat", "Rsat", "Other"]

        #Variables of interest title
        self.label4 = Label(master, text = "Variables of Interest: ")
        self.label4.grid(sticky= W, row = 15, padx=20)

        '''
           for i in range(0, len(var_names)):
           column_selected = IntVar()
           self.check = Checkbutton(master, text=var_names[i], variable=column_selected, onvalue = 8)
           self.list_columns_selected.append(column_selected)
           self.check.grid(row=16 + i, sticky = W, padx=30)
           '''
        #Submit button
        self.submitButton = Button(master, text = "Submit", command = submit_function)
        self.submitButton.grid(row = 16 + len(var_names), sticky = W)

#self.greet_button = Button(master, text="Greet", command=greet)
#self.close_button = Button(master, text="Close", command=master.quit)

#self.label1.grid(columnspan=2, sticky=W)
#self.greet_button.grid(row=1)
#self.close_button.grid(row=1, column=1)

#self.B = Button(master, text ="Hello", command = callback)
#self.B.grid(row=3, column = 1)

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()



# (...)

