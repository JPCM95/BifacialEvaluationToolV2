"""
This module creates the Graphical User Interface (GUI). and works as the main file for the project.
"""

from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import ttk
import os

import extraction
import globals
import empirical
import statistics
import plotter
import tables

""" 
Root configuration 
"""
root = Tk()
root.geometry("500x500")
root.title("Bifacial Comparison Tool (BCT)")
root.resizable(0,0)
root.iconbitmap("sun.ico")
root.propagate(0)


""" 
Welcome label 
"""
authorLabel = Label(root, text = "Welcome to the bifacial ratio comparison tool!", font=("Consolas",10))
authorLabel.config(justify='left')
authorLabel.pack(side='left', anchor="sw")


""" 
Label for tool name 
"""
toolLabel = Label(root, text=""" 1) Select the tool you used to simulate 
the data sets, or input the measured data """)
toolLabel.config(bg="light gray", justify="center", relief="ridge")
toolLabel.place(x=145, y=25)

""" 
This function creates an external window for th PVSyst case (view factor)
"""
def pvsystWindow():
    """ Create the main window """
    pvsystroot = Toplevel()
    pvsystroot.geometry("350x400")
    pvsystroot.title("PVSyst file loading window")
    pvsystroot.resizable(0, 0)
    pvsystroot.iconbitmap("sun.ico")
    pvsystroot.propagate(0)

    """ Label for monofacial energy button """
    pvloadLabel = Label(pvsystroot, text=""" Mark this option if the file contains the 
    monofacial energy data (albedo = 0 for all months) """)
    pvloadLabel.config(bg="light gray", justify="center", relief="ridge")
    pvloadLabel.place(x=30, y=25)

    def setmono():
        globals.monoCheck = monofacial.get()
        print(globals.monoCheck)

    monofacial = IntVar()

    checkMonofacial = Checkbutton(pvsystroot, text="Common albedo as 0?", variable=monofacial, onvalue=1, offvalue=0, command=setmono)
    checkMonofacial.place(x=110, y=70)

    """ Label for load file button """
    pvloadLabel = Label(pvsystroot, text="""Use the following button to find and load the 
    CSV files containing the simulated data""")
    pvloadLabel.config(bg="light gray", justify="center", relief="ridge")
    pvloadLabel.place(x=55, y=120)

    """ Entry box to display the path of the path of the CSV file, or type said path """
    currentpath1 = StringVar(pvsystroot, value=os.getcwd())
    entrybox1 = Entry(pvsystroot, textvariable=currentpath1)
    entrybox1.config(width=50)
    entrybox1.place(x=25, y=170)

    """ Update the filepath display """
    def updatefilepathpv():
        entrybox1.delete(0, END)
        entrybox1.insert(END, globals.pvfilepath)

    """ Calls the external loadfile function """
    def loadpv():
        extraction.loadpvsyst()

    """ Button to load file """
    loadButton1 = Button(pvsystroot, text="  Search file  ", command=lambda: [loadpv(), updatefilepathpv()])
    loadButton1.place(x=140, y=200)

    """ Label for module power label """
    powloadLabel = Label(pvsystroot, text="""Please insert the value for the corresponding 
    module's nominal power [kWp]:""")
    powloadLabel.config(bg="light gray", justify="center", relief="ridge")
    powloadLabel.place(x=55, y=255)

    """ Entry box for the module power """
    entrybox2 = Entry(pvsystroot)
    entrybox2.config(width=6, justify="center")
    entrybox2.place(x=155, y=300)

    """ Units label for module power """
    unitsLabel = Label(pvsystroot, text="""[kWp]""")
    unitsLabel.config(justify="center")
    unitsLabel.place(x=195, y=300)

    """ This function stores the module's power from the entry box in a global variable """
    def setpower():
        globals.modpower = float(entrybox2.get())
        print(globals.modpower)
        MessageBox.showinfo("Success", "Saved module power: {} kWp".format(globals.modpower))

        return globals.modpower

    """ Button to set module power """
    setButton1 = Button(pvsystroot, text="  Set  ", command=setpower)
    setButton1.config(width=8)
    setButton1.place(x=142, y=330)

    """ Function to reset the global variables """
    def clearset():
        globals.pvsMonoEnergy = []
        globals.pvsBifEnergy = []
        globals.pvsEfficiency = []
        globals.pvsBifGain = []
        MessageBox.showinfo("Cleared", "All values loaded have been cleared")

    """ Button to clear everything in the boxes """
    clearButton = Button(pvsystroot, text="  Clear  ", command=clearset)
    clearButton.config(background="white", foreground="red")
    clearButton.place(x=290, y=365)

    """ Root loop """
    pvsystroot.mainloop()


""" 
This function creates an external window for the NREL case (ray tracing)
"""
def nrelWindow():
    """ Create the main window """
    thirdroot = Toplevel()
    thirdroot.geometry("350x200")
    thirdroot.title("NREL file loading window")
    thirdroot.resizable(0, 0)
    thirdroot.iconbitmap("sun.ico")
    thirdroot.propagate(0)

    """ Label for load label """
    loadLabel = Label(thirdroot, text="""Use the following button to find and load the 
    CSV files containing the simulated data""")
    loadLabel.config(bg="light gray", justify="center", relief="ridge")
    loadLabel.place(x=55, y=45)

    """ Entry box to display the path of the path of the CSV file, or type said path """
    currentpath = StringVar(thirdroot, value=os.getcwd())
    entrybox = Entry(thirdroot, textvariable=currentpath)
    entrybox.config(width=50)
    entrybox.place(x=25, y=95)

    """ Update the filepath display """
    def updatefilepath():
        entrybox.delete(0, END)
        entrybox.insert(END, globals.filepath)

    """ Calls the external loadfile function """
    def load():
        extraction.loadfile()

    """ Button to load file """
    loadButton = Button(thirdroot, text="  Search file  ", command=lambda: [load(), updatefilepath()])
    loadButton.place(x=140, y=125)

    """ Function to reset the global variables """
    def clearset():
        globals.nrelBifRatio = []
        globals.nrelBifEnergy = []
        globals.nrelEfficiency = []
        globals.nrelPercentBG = []
        MessageBox.showinfo("Cleared", "All values loaded have been cleared")

    """ Button to clear everything in the boxes """
    clearButton = Button(thirdroot, text="  Clear  ", command=clearset)
    clearButton.config(background="white", foreground="red")
    clearButton.place(x=295, y=170)

    """ Root loop """
    thirdroot.mainloop()


""" 
This fuction creates an external window to input the data for the Solar World case (empirical) 
"""
def empInputWindow():
    """ Create the window """
    secondRoot = Toplevel()
    secondRoot.geometry("700x450")
    secondRoot.title("Solar World calculator window")
    secondRoot.resizable(0, 0)
    secondRoot.iconbitmap("sun.ico")
    secondRoot.propagate(0)

    """ Label with introduction """
    eqIntroLabel = Label(secondRoot,
    text="The following equation is used to calculate the Bifacial Gain in Energy (BGE) using the empirical model provided by Solar World:\n")
    eqIntroLabel.place(x=5, y=25)
    eqIntroLabel.config(justify="center")

    """ Equation """
    formula = PhotoImage(file="empFormula.gif")
    formulaLabel = Label(secondRoot, image=formula)
    formulaLabel.place(x=5, y=65)

    """ Small instruction label """
    inputsLabel = Label(secondRoot,
    text="Please provide the input values for:")
    inputsLabel.place(x=5, y=120)
    inputsLabel.config(justify="center")

    """ Ornamental ridge label """
    background1 = Label(secondRoot, relief="ridge")
    background1.config(width=98, height=15)
    background1.place(x=5, y=142)


    """ Monthly albedo label """
    monthlyinputsLabel = Label(secondRoot,
    text="Monthly albedo (\u03b1):")
    monthlyinputsLabel.place(x=10, y=150)
    monthlyinputsLabel.config(justify="center")

    """ Jan label and entry box """
    labelJan = Label(secondRoot, text="Jan.")
    labelJan.place(x=10, y=185)
    labelJan.config(justify="center")

    entryJan = Entry(secondRoot)
    entryJan.place(x=45, y=185)
    entryJan.config(width=6)

    """ Feb label and entry box """
    labelFeb = Label(secondRoot, text="Feb.")
    labelFeb.place(x=10, y=215)
    labelFeb.config(justify="center")

    entryFeb = Entry(secondRoot)
    entryFeb.place(x=45, y=215)
    entryFeb.config(width=6)

    """ Mar label and entry box """
    labelMar = Label(secondRoot, text="Mar.")
    labelMar.place(x=10, y=245)
    labelMar.config(justify="center")

    entryMar = Entry(secondRoot)
    entryMar.place(x=45, y=245)
    entryMar.config(width=6)

    """ Apr label and entry box """
    labelApr = Label(secondRoot, text="Apr.")
    labelApr.place(x=10, y=275)
    labelApr.config(justify="center")

    entryApr = Entry(secondRoot)
    entryApr.place(x=45, y=275)
    entryApr.config(width=6)

    """ May label and entry box """
    labelMay = Label(secondRoot, text="May.")
    labelMay.place(x=10, y=305)
    labelMay.config(justify="center")

    entryMay = Entry(secondRoot)
    entryMay.place(x=45, y=305)
    entryMay.config(width=6)

    """ Jun label and entry box """
    labelJun = Label(secondRoot, text="Jun.")
    labelJun.place(x=10, y=335)
    labelJun.config(justify="center")

    entryJun = Entry(secondRoot)
    entryJun.place(x=45, y=335)
    entryJun.config(width=6)

    """ Jul label and entry box """
    labelJul = Label(secondRoot, text="Jul.")
    labelJul.place(x=95, y=185)
    labelJul.config(justify="center")

    entryJul = Entry(secondRoot)
    entryJul.place(x=130, y=185)
    entryJul.config(width=6)

    """ Aug label and entry box """
    labelAug = Label(secondRoot, text="Aug.")
    labelAug.place(x=95, y=215)
    labelAug.config(justify="center")

    entryAug = Entry(secondRoot)
    entryAug.place(x=130, y=215)
    entryAug.config(width=6)

    """ Sep label and entry box """
    labelSep = Label(secondRoot, text="Sep.")
    labelSep.place(x=95, y=245)
    labelSep.config(justify="center")

    entrySep = Entry(secondRoot)
    entrySep.place(x=130, y=245)
    entrySep.config(width=6)

    """ Oct label and entry box """
    labelOct = Label(secondRoot, text="Oct.")
    labelOct.place(x=95, y=275)
    labelOct.config(justify="center")

    entryOct = Entry(secondRoot)
    entryOct.place(x=130, y=275)
    entryOct.config(width=6)

    """ Nov label and entry box """
    labelNov = Label(secondRoot, text="Nov.")
    labelNov.place(x=95, y=305)
    labelNov.config(justify="center")

    entryNov = Entry(secondRoot)
    entryNov.place(x=130, y=305)
    entryNov.config(width=6)

    """ Dec label and entry box """
    labelDec = Label(secondRoot, text="Dec.")
    labelDec.place(x=95, y=335)
    labelDec.config(justify="center")

    entryDec = Entry(secondRoot)
    entryDec.place(x=130, y=335)
    entryDec.config(width=6)


    """ Common albedo label """
    commoninputsLabel = Label(secondRoot,
    text="Or set a common albedo value:")
    commoninputsLabel.place(x=250, y=150)
    commoninputsLabel.config(justify="center")

    """ Set common albedo label and entry box """
    labelcommon = Label(secondRoot, text="Common value")
    labelcommon.place(x=255, y=185)
    labelcommon.config(justify="center")

    entrycommon = Entry(secondRoot)
    entrycommon.place(x=355, y=185)
    entrycommon.config(width=6)

    """ Function to set common albedo to all entry boxes """
    def setcommonalb():
        entries = [entryJan, entryFeb, entryMar, entryApr, entryMay, entryJun, entryJul, entryAug, entrySep, entryOct,
                   entryNov, entryDec]

        for ent in entries:
            ent.delete(0, END)
            ent.insert(END, float(entrycommon.get()))

    """ Button to set common value """
    setButton = Button(secondRoot, text="  Set  ", command=setcommonalb)
    setButton.config(width=8)
    setButton.place(x=295, y=225)

    """ Other values label """
    otherinputsLabel = Label(secondRoot,
    text="Other values:")
    otherinputsLabel.place(x=455, y=150)
    otherinputsLabel.config(justify="center")

    """ Bifacial factor label and entry box """
    labelBif = Label(secondRoot, text="Bifacial factor (\u03D5pmp)")
    labelBif.place(x=490, y=185)
    labelBif.config(justify="center")

    entryBif = Entry(secondRoot)
    entryBif.place(x=620, y=185)
    entryBif.config(width=10)

    """ GCR label and entry box """
    labelGCR = Label(secondRoot, text="Ground coverage ratio (GCR)")
    labelGCR.place(x=455, y=215)
    labelGCR.config(justify="center")

    entryGCR = Entry(secondRoot)
    entryGCR.place(x=620, y=215)
    entryGCR.config(width=10)

    """ Clearance height label and entry box """
    labelClear = Label(secondRoot, text="Clearance height (h)")
    labelClear.place(x=500, y=245)
    labelClear.config(justify="center")

    entryClear = Entry(secondRoot)
    entryClear.place(x=620, y=245)
    entryClear.config(width=10)

    """This function retrieves the values from the entry boxes and calls the function located in empirical.py module"""
    def entries():
        albedos = [float(entryJan.get()), float(entryFeb.get()), float(entryMar.get()), float(entryApr.get()),
                   float(entryMay.get()), float(entryJun.get()), float(entryJul.get()), float(entryAug.get()),
                   float(entrySep.get()), float(entryOct.get()), float(entryNov.get()), float(entryDec.get())]

        print("Albedos:", albedos)

        bifgain = float(entryBif.get())
        GCR = float(entryGCR.get())
        clearheight = float(entryClear.get())

        for albvalue in albedos:
            empirical.empmodel(albvalue, bifgain, GCR, clearheight)

        MessageBox.showinfo("Success!", "Bifacial gain has been calculated successfully")

    """ Result label """
    calcLabel = Label(secondRoot)
    calcLabel.place(x=280, y=380)
    calcLabel.config(text="Calculate BGE[%]", fg="blue")

    """ Button to calculate the result """
    calcButton = Button(secondRoot, text="  Calculate  ", command=entries)
    calcButton.place(x=290, y=410)

    """ Function to clear the values from all the boxes and from the bifacial gain list"""
    def clearset():
        boxes = [entryJan, entryFeb, entryMar, entryApr, entryMay, entryJun, entryJul, entryAug, entrySep, entryOct,
                   entryNov, entryDec, entrycommon, entryBif, entryGCR, entryClear]

        for value in boxes:
            value.delete(0, END)
        globals.empiricalList = []
        globals.swPercentBG = []
        MessageBox.showinfo("Cleared", "All values for Solar World's bifacial gain have been cleared")



    """ Button to clear everything in the boxes """
    clearButton = Button(secondRoot, text="  Clear  ", command=clearset)
    clearButton.config(background="white", foreground="red")
    clearButton.place(x=630, y=335)


    """ End of loob for the window """
    secondRoot.mainloop()


"""  
Function to create the extra window to input measured data
"""
def realData():
    """ Create the window """
    realRoot = Toplevel()
    realRoot.geometry("455x350")
    realRoot.title("Measured data input window")
    realRoot.resizable(0, 0)
    realRoot.iconbitmap("sun.ico")
    realRoot.propagate(0)

    """ Label with introduction """
    realIntroLabel = Label(realRoot,
    text="Please input the measured values for monthly bifacial gain and bifacial energy: ")
    realIntroLabel.place(x=7, y=10)
    realIntroLabel.config(justify="center")

    """ Ornamental ridge label """
    background1 = Label(realRoot, relief="ridge")
    background1.config(width=62, height=15)
    background1.place(x=7, y=50)

    """ Monthly BG label """
    monthlyinputsLabel = Label(realRoot,
    text="Monthly bifacial gain [%]:")
    monthlyinputsLabel.place(x=17, y=58)
    monthlyinputsLabel.config(justify="center")

    """ Jan label and entry box """
    labelJan = Label(realRoot, text="Jan.")
    labelJan.place(x=17, y=93)
    labelJan.config(justify="center")

    entryJan = Entry(realRoot)
    entryJan.place(x=52, y=93)
    entryJan.config(width=6)

    """ Feb label and entry box """
    labelFeb = Label(realRoot, text="Feb.")
    labelFeb.place(x=17, y=123)
    labelFeb.config(justify="center")

    entryFeb = Entry(realRoot)
    entryFeb.place(x=52, y=123)
    entryFeb.config(width=6)

    """ Mar label and entry box """
    labelMar = Label(realRoot, text="Mar.")
    labelMar.place(x=17, y=153)
    labelMar.config(justify="center")

    entryMar = Entry(realRoot)
    entryMar.place(x=52, y=153)
    entryMar.config(width=6)

    """ Apr label and entry box """
    labelApr = Label(realRoot, text="Apr.")
    labelApr.place(x=17, y=183)
    labelApr.config(justify="center")

    entryApr = Entry(realRoot)
    entryApr.place(x=52, y=183)
    entryApr.config(width=6)

    """ May label and entry box """
    labelMay = Label(realRoot, text="May.")
    labelMay.place(x=17, y=213)
    labelMay.config(justify="center")

    entryMay = Entry(realRoot)
    entryMay.place(x=52, y=213)
    entryMay.config(width=6)

    """ Jun label and entry box """
    labelJun = Label(realRoot, text="Jun.")
    labelJun.place(x=17, y=243)
    labelJun.config(justify="center")

    entryJun = Entry(realRoot)
    entryJun.place(x=52, y=243)
    entryJun.config(width=6)

    """ Jul label and entry box """
    labelJul = Label(realRoot, text="Jul.")
    labelJul.place(x=102, y=93)
    labelJul.config(justify="center")

    entryJul = Entry(realRoot)
    entryJul.place(x=137, y=93)
    entryJul.config(width=6)

    """ Aug label and entry box """
    labelAug = Label(realRoot, text="Aug.")
    labelAug.place(x=102, y=123)
    labelAug.config(justify="center")

    entryAug = Entry(realRoot)
    entryAug.place(x=137, y=123)
    entryAug.config(width=6)

    """ Sep label and entry box """
    labelSep = Label(realRoot, text="Sep.")
    labelSep.place(x=102, y=153)
    labelSep.config(justify="center")

    entrySep = Entry(realRoot)
    entrySep.place(x=137, y=153)
    entrySep.config(width=6)

    """ Oct label and entry box """
    labelOct = Label(realRoot, text="Oct.")
    labelOct.place(x=102, y=183)
    labelOct.config(justify="center")

    entryOct = Entry(realRoot)
    entryOct.place(x=137, y=183)
    entryOct.config(width=6)

    """ Nov label and entry box """
    labelNov = Label(realRoot, text="Nov.")
    labelNov.place(x=102, y=213)
    labelNov.config(justify="center")

    entryNov = Entry(realRoot)
    entryNov.place(x=137, y=213)
    entryNov.config(width=6)

    """ Dec label and entry box """
    labelDec = Label(realRoot, text="Dec.")
    labelDec.place(x=102, y=243)
    labelDec.config(justify="center")

    entryDec = Entry(realRoot)
    entryDec.place(x=137, y=243)
    entryDec.config(width=6)

    """ Monthly Bif. Energy label """
    bifinputsLabel = Label(realRoot,
    text="Monthly bifacial energy [kWh]:")
    bifinputsLabel.place(x=265, y=58)
    bifinputsLabel.config(justify="center")

    """ Jan label and entry box """
    labelJan2 = Label(realRoot, text="Jan.")
    labelJan2.place(x=265, y=93)
    labelJan2.config(justify="center")

    entryJan2 = Entry(realRoot)
    entryJan2.place(x=300, y=93)
    entryJan2.config(width=6)

    """ Feb label and entry box """
    labelFeb2 = Label(realRoot, text="Feb.")
    labelFeb2.place(x=265, y=123)
    labelFeb2.config(justify="center")

    entryFeb2 = Entry(realRoot)
    entryFeb2.place(x=300, y=123)
    entryFeb2.config(width=6)

    """ Mar label and entry box """
    labelMar2 = Label(realRoot, text="Mar.")
    labelMar2.place(x=265, y=153)
    labelMar2.config(justify="center")

    entryMar2 = Entry(realRoot)
    entryMar2.place(x=300, y=153)
    entryMar2.config(width=6)

    """ Apr label and entry box """
    labelApr2 = Label(realRoot, text="Apr.")
    labelApr2.place(x=265, y=183)
    labelApr2.config(justify="center")

    entryApr2 = Entry(realRoot)
    entryApr2.place(x=300, y=183)
    entryApr2.config(width=6)

    """ May label and entry box """
    labelMay2 = Label(realRoot, text="May.")
    labelMay2.place(x=265, y=213)
    labelMay2.config(justify="center")

    entryMay2 = Entry(realRoot)
    entryMay2.place(x=300, y=213)
    entryMay2.config(width=6)

    """ Jun label and entry box """
    labelJun2 = Label(realRoot, text="Jun.")
    labelJun2.place(x=265, y=243)
    labelJun2.config(justify="center")

    entryJun2 = Entry(realRoot)
    entryJun2.place(x=300, y=243)
    entryJun2.config(width=6)

    """ Jul label and entry box """
    labelJul2= Label(realRoot, text="Jul.")
    labelJul2.place(x=350, y=93)
    labelJul2.config(justify="center")

    entryJul2 = Entry(realRoot)
    entryJul2.place(x=385, y=93)
    entryJul2.config(width=6)

    """ Aug label and entry box """
    labelAug2 = Label(realRoot, text="Aug.")
    labelAug2.place(x=350, y=123)
    labelAug2.config(justify="center")

    entryAug2 = Entry(realRoot)
    entryAug2.place(x=385, y=123)
    entryAug2.config(width=6)

    """ Sep label and entry box """
    labelSep2 = Label(realRoot, text="Sep.")
    labelSep2.place(x=350, y=153)
    labelSep2.config(justify="center")

    entrySep2 = Entry(realRoot)
    entrySep2.place(x=385, y=153)
    entrySep2.config(width=6)

    """ Oct label and entry box """
    labelOct2 = Label(realRoot, text="Oct.")
    labelOct2.place(x=350, y=183)
    labelOct2.config(justify="center")

    entryOct2 = Entry(realRoot)
    entryOct2.place(x=385, y=183)
    entryOct2.config(width=6)

    """ Nov label and entry box """
    labelNov2 = Label(realRoot, text="Nov.")
    labelNov2.place(x=350, y=213)
    labelNov2.config(justify="center")

    entryNov2 = Entry(realRoot)
    entryNov2.place(x=385, y=213)
    entryNov2.config(width=6)

    """ Dec label and entry box """
    labelDec2 = Label(realRoot, text="Dec.")
    labelDec2.place(x=350, y=243)
    labelDec2.config(justify="center")

    entryDec2 = Entry(realRoot)
    entryDec2.place(x=385, y=243)
    entryDec2.config(width=6)

    """This functions retrieve the values from the entry boxes and calls and stores them in globals.py module"""
    def entriesBG():
        realBGs = [float(entryJan.get()), float(entryFeb.get()), float(entryMar.get()), float(entryApr.get()),
                   float(entryMay.get()), float(entryJun.get()), float(entryJul.get()), float(entryAug.get()),
                   float(entrySep.get()), float(entryOct.get()), float(entryNov.get()), float(entryDec.get())]

        for value in realBGs:
            globals.realBifacialGain.append(value)

        print("Real Bifacial Gains:", globals.realBifacialGain)
        MessageBox.showinfo("Success!", "Values have been loaded successfully")

    def entriesBE():
        realBEs = [float(entryJan2.get()), float(entryFeb2.get()), float(entryMar2.get()), float(entryApr2.get()),
                   float(entryMay2.get()), float(entryJun2.get()), float(entryJul2.get()), float(entryAug2.get()),
                   float(entrySep2.get()), float(entryOct2.get()), float(entryNov2.get()), float(entryDec2.get())]

        for value in realBEs:
            globals.realBifacialEnergy.append(value)

        print("Real Bifacial Energies:", globals.realBifacialEnergy)

    """ Button to set values """
    valueButton = Button(realRoot, text="  Set  ", command=lambda: [entriesBG(), entriesBE()])
    valueButton.config(width=15)
    valueButton.place(x=170, y=300)

    """ Function to clear the values from all the boxes and from the bifacial gain list"""
    def clearset():
        boxes = [entryJan, entryFeb, entryMar, entryApr, entryMay, entryJun, entryJul, entryAug, entrySep, entryOct,
                   entryNov, entryDec, entryJan2, entryFeb2, entryMar2, entryApr2, entryMay2, entryJun2, entryJul2,
                 entryAug2, entrySep2, entryOct2, entryNov2, entryDec2]

        for value in boxes:
            value.delete(0, END)
        globals.realBifacialGain = []
        globals.realBifacialEnergy = []
        MessageBox.showinfo("Cleared", "All values for measured bifacial gain and energy have been cleared")

    """ Button to clear everything in the boxes """
    clearButton = Button(realRoot, text="  Clear  ", command=clearset)
    clearButton.config(background="white", foreground="red")
    clearButton.place(x=400, y=320)

    """ End of loob for the window """
    realRoot.mainloop()


"""
Drop down menu with the names for the simulation tools

callbackFunc function sets the global variable toolname as the value obtained at the dropdown menu, prints the
selected option in the console and returns that toolname, as well as calling the functions to create new windows.
"""
def callbackFunc(event):
    globals.toolname = dropdown.get()
    print("{} tool has been selected".format(globals.toolname))
    if globals.toolname == "PVSyst":
        pvsystWindow()

    elif globals.toolname == "NREL Bifacial Radiance":
        nrelWindow()

    elif globals.toolname == "Solar World":
        empInputWindow()

    elif globals.toolname == "Measured data":
        realData()

    return globals.toolname


"""
This function is used to set the values for the dropdown menu, which are initially set as empty to display no
options before the user clicks the menu
"""
def changevalues():
    dropdown["values"]=["PVSyst", "NREL Bifacial Radiance", "Solar World", "Measured data"]


dropdown = ttk.Combobox(state="readonly", values=[""], postcommand=changevalues)
dropdown.place(x=182, y=80)
dropdown.current(0)
dropdown.bind("<<ComboboxSelected>>", callbackFunc)


""" Label for tool selection at the plotter """
plotLabel = Label(root, text="""2) Select the simulation tool(s) or 
measured data you would like to graph""")
plotLabel.config(bg="light gray", justify="center", relief="ridge")
plotLabel.place(x=25, y=160)


"""
Check buttons for the plotter
The following functions store the value of the checkbutton variables to a corresponding global variable
"""

""" This functions get the value coming from the check buttons """
def setpvs():
    globals.pvscheck = pvsyst.get()
    print(globals.pvscheck)

def setnrel():
    globals.nrelcheck = nrel.get()
    print(globals.nrelcheck)

def setsw():
    globals.swcheck = solarworld.get()
    print(globals.swcheck)

def setreal():
    globals.realcheck = realdata.get()
    print(globals.realcheck)

def changeState():
    if globals.realcheck == 1:
        radio3.config(state=DISABLED)
    else:
        radio3.config(state=NORMAL)

""" Integer values for the buttons, that work as booleans """
pvsyst = IntVar()
nrel = IntVar()
solarworld = IntVar()
realdata = IntVar()

""" Check buttons for the plotter """
check1 = Checkbutton(root, text="PVSyst", variable=pvsyst, onvalue=1, offvalue=0, command=setpvs)
check1.place(x=100, y=210)

check2 = Checkbutton(root, text="NREL", variable=nrel, onvalue=1, offvalue=0, command=setnrel)
check2.place(x=100, y=235)

check3 = Checkbutton(root, text="Solar World", variable=solarworld, onvalue=1, offvalue=0, command=setsw)
check3.place(x=100, y=260)

check4 = Checkbutton(root, text="Measured data", variable=realdata, onvalue=1, offvalue=0, command=lambda: [setreal(), changeState()])
check4.place(x=100, y=285)


""" Label for data selection at the plotter """
plotData = Label(root, text="""3) Select the data you would like 
to graph (single option)""")
plotData.config(bg="light gray", justify="center", relief="ridge")
plotData.place(x=270, y=160)


""" Radio buttons for the plotter, and function to set the global variable as the button selection """
def select():
    globals.radioselect = option.get()
    print(globals.radioselect)


option = StringVar()

radio1 = Radiobutton(root, text="Bifacial gain", variable=option, value="BifacialGain", command=select, state=NORMAL)
radio1.place(x=280, y=210)

radio2 = Radiobutton(root, text="Bifacial energy", variable=option, value="BifacialEnergy", command=select, state=NORMAL)
radio2.place(x=280, y=235)

radio3 = Radiobutton(root, text="Module energy efficiency", variable=option, value="ModuleEnergy", command=select, state=NORMAL)
radio3.place(x=280, y=260)


""" Button to plot """
plotButton = Button(root, text="  Plot  ", command=plotter.plot)
plotButton.config(width=8)
plotButton.place(x=215, y=330)

""" Statistical analysis button """
statButton = Button(root, text="  Statistical Analysis  ", command=lambda: [statistics.BGerrors(), statistics.BEerrors(),
                                                                            plotter.plotErrors()])
statButton.place(x=188, y=370)

""" Button to create simulations tables """
simTableButton = Button(root, text="  Data table  ", command=tables.gen_table_sim)
simTableButton.config(width=8)
simTableButton.config(background="white", foreground="blue")
simTableButton.place(x=420, y=330)

""" Button to create errors tables """
errorTableButton = Button(root, text="  Errors table  ", command=tables.gen_table_errors)
errorTableButton.config(width=8)
errorTableButton.config(background="white", foreground="red")
errorTableButton.place(x=420, y=370)


""" TEC logo image """
logo = PhotoImage(file="LOGO-TEC-resize.gif")
logoLabel = Label(root, image=logo)
logoLabel.place(x=110, y=410)


""" Main app loop """
root.mainloop()