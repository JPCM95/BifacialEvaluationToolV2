"""
This module takes care of opening the CSV files to extract its data and sends it to be sorted in the next step.
"""

from tkinter import filedialog as FileDialog
from tkinter import messagebox as MessageBox
import pandas as pd
import globals
import sorting

""" 
PVSys case: Fuction that opens the window to load the CSV files, check file extension, load the data in a pandas 
dataframe, create a message to indicate the success of the file loading, and call the sorting function with that data
"""
def loadpvsyst():
    pvspath = FileDialog.askopenfilename(title="Open file", filetypes=(("Comma-separated values", "*.csv"),
                                                                    ("All files", "*.*")))
    globals.pvfilepath = pvspath

    if pvspath == "":
        pass
    elif pvspath != '' and pvspath[-4:] != ".CSV":
        MessageBox.showerror("Error!", "Incorrect file extension")
    else:
        temporarylist = pvspath.split("/")
        pvsfilename = temporarylist[-1]
        dataf = pd.read_csv(pvspath, sep=",", skiprows=2) # , on_bad_lines='skip'
        print(dataf)
        MessageBox.showinfo("Success!", """
        File: {}
        Simulation tool: {}

        Loaded successfully!  
        """.format(pvsfilename, globals.toolname))

        return sorting.sort(dataf)


"""
NREL case: This function opens a pop-up window to enable the user to look for the desired CSV files, and then separates 
the useful information and stores it in a pandas dataframe, returning said dataframe to a different function
"""
def loadfile():
    path = FileDialog.askopenfilename(title="Open file", filetypes=(("Comma-separated values","*.csv"),
                                                                    ("All files", "*.*")))
    globals.filepath = path

    if path == "":
        pass
    elif path != '' and path[-4:] != ".csv":
        MessageBox.showerror("Error!", "Incorrect file extension")
    else:
        templist = path.split("/")
        filename = templist[-1]
        df = pd.read_csv(path)
        print(df)
        info = df.iloc[:, -1:]
        MessageBox.showinfo("Success!","""
        File: {}
        Simulation tool: {}

        Loaded successfully!  
        """.format(filename, globals.toolname))

        return sorting.sort(info)

