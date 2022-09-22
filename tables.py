"""
This module contains the functions to create the tables depending on the number of columns for each case, and also
the functions related to the simulation cases.
"""

from tkinter import *
from tkinter import messagebox as MessageBox
from tkintertable import TableCanvas
import numpy as np
import globals
import empirical
import statistics


""" 
Function to create a six column table 
"""
def sixcolumns(col1, col2, col3, col4, col5, col6, colname1, colname2, colname3, colname4, colname5, colname6):
    array = np.array([col1, col2, col3, col4, col5, col6])
    tarray = np.transpose(array)

    master = Toplevel()
    tframe = Frame(master)
    tframe.pack()

    data = {'row1': {colname1: float(tarray[0, 0]), colname2: float(tarray[0, 1]), colname3: float(tarray[0, 2]),
                     colname4: float(tarray[0, 3]), colname5: float(tarray[0, 4]), colname6: float(tarray[0, 5])},

            'row2': {colname1: float(tarray[1, 0]), colname2: float(tarray[1, 1]), colname3: float(tarray[1, 2]),
                     colname4: float(tarray[1, 3]), colname5: float(tarray[1, 4]), colname6: float(tarray[1, 5])},


            'row3': {colname1: float(tarray[2, 0]), colname2: float(tarray[2, 1]), colname3: float(tarray[2, 2]),
                     colname4: float(tarray[2, 3]), colname5: float(tarray[2, 4]), colname6: float(tarray[2, 5])},


            'row4': {colname1: float(tarray[3, 0]), colname2: float(tarray[3, 1]), colname3: float(tarray[3, 2]),
                     colname4: float(tarray[3, 3]), colname5: float(tarray[3, 4]), colname6: float(tarray[3, 5])},


            'row5': {colname1: float(tarray[4, 0]), colname2: float(tarray[4, 1]), colname3: float(tarray[4, 2]),
                     colname4: float(tarray[4, 3]), colname5: float(tarray[4, 4]), colname6: float(tarray[4, 5])},


            'row6': {colname1: float(tarray[5, 0]), colname2: float(tarray[5, 1]), colname3: float(tarray[5, 2]),
                     colname4: float(tarray[5, 3]), colname5: float(tarray[5, 4]), colname6: float(tarray[5, 5])},


            'row7': {colname1: float(tarray[6, 0]), colname2: float(tarray[6, 1]), colname3: float(tarray[6, 2]),
                     colname4: float(tarray[6, 3]), colname5: float(tarray[6, 4]), colname6: float(tarray[6, 5])},


            'row8': {colname1: float(tarray[7, 0]), colname2: float(tarray[7, 1]), colname3: float(tarray[7, 2]),
                     colname4: float(tarray[7, 3]), colname5: float(tarray[7, 4]), colname6: float(tarray[7, 5])},


            'row9': {colname1: float(tarray[8, 0]), colname2: float(tarray[8, 1]), colname3: float(tarray[8, 2]),
                     colname4: float(tarray[8, 3]), colname5: float(tarray[8, 4]), colname6: float(tarray[8, 5])},


            'row10': {colname1: float(tarray[9, 0]), colname2: float(tarray[9, 1]), colname3: float(tarray[9, 2]),
                      colname4: float(tarray[9, 3]), colname5: float(tarray[9, 4]), colname6: float(tarray[9, 5])},


            'row11': {colname1: float(tarray[10, 0]), colname2: float(tarray[10, 1]), colname3: float(tarray[10, 2]),
                      colname4: float(tarray[10, 3]), colname5: float(tarray[10, 4]), colname6: float(tarray[10, 5])},


            'row12': {colname1: float(tarray[11, 0]), colname2: float(tarray[11, 1]), colname3: float(tarray[11, 2]),
                      colname4: float(tarray[11, 3]), colname5: float(tarray[11, 4]), colname6: float(tarray[11, 5])}
            }

    table = TableCanvas(tframe, data=data)
    # table.redraw()
    table.show()

    master.mainloop()


""" 
Unused, but placed in case the user needs it) Function to create a five column table 
"""
# def fivecolumns(col1, col2, col3, col4, col5, colname1, colname2, colname3, colname4, colname5):
#     array = np.array([col1, col2, col3, col4, col5])
#     tarray = np.transpose(array)
#
#     master = Toplevel()
#     tframe = Frame(master)
#     tframe.pack()
#
#     data = {'row1': {colname1: float(tarray[0, 0]), colname2: float(tarray[0, 1]), colname3: float(tarray[0, 2]),
#                      colname4: float(tarray[0, 3]), colname5: float(tarray[0, 4])},
#
#             'row2': {colname1: float(tarray[1, 0]), colname2: float(tarray[1, 1]), colname3: float(tarray[1, 2]),
#                      colname4: float(tarray[1, 3]), colname5: float(tarray[1, 4])},
#
#
#             'row3': {colname1: float(tarray[2, 0]), colname2: float(tarray[2, 1]), colname3: float(tarray[2, 2]),
#                      colname4: float(tarray[2, 3]), colname5: float(tarray[2, 4])},
#
#
#             'row4': {colname1: float(tarray[3, 0]), colname2: float(tarray[3, 1]), colname3: float(tarray[3, 2]),
#                      colname4: float(tarray[3, 3]), colname5: float(tarray[3, 4])},
#
#
#             'row5': {colname1: float(tarray[4, 0]), colname2: float(tarray[4, 1]), colname3: float(tarray[4, 2]),
#                      colname4: float(tarray[4, 3]), colname5: float(tarray[4, 4])},
#
#
#             'row6': {colname1: float(tarray[5, 0]), colname2: float(tarray[5, 1]), colname3: float(tarray[5, 2]),
#                      colname4: float(tarray[5, 3]), colname5: float(tarray[5, 4])},
#
#
#             'row7': {colname1: float(tarray[6, 0]), colname2: float(tarray[6, 1]), colname3: float(tarray[6, 2]),
#                      colname4: float(tarray[6, 3]), colname5: float(tarray[6, 4])},
#
#
#             'row8': {colname1: float(tarray[7, 0]), colname2: float(tarray[7, 1]), colname3: float(tarray[7, 2]),
#                      colname4: float(tarray[7, 3]), colname5: float(tarray[7, 4])},
#
#
#             'row9': {colname1: float(tarray[8, 0]), colname2: float(tarray[8, 1]), colname3: float(tarray[8, 2]),
#                      colname4: float(tarray[8, 3]), colname5: float(tarray[8, 4])},
#
#
#             'row10': {colname1: float(tarray[9, 0]), colname2: float(tarray[9, 1]), colname3: float(tarray[9, 2]),
#                       colname4: float(tarray[9, 3]), colname5: float(tarray[9, 4])},
#
#
#             'row11': {colname1: float(tarray[10, 0]), colname2: float(tarray[10, 1]), colname3: float(tarray[10, 2]),
#                       colname4: float(tarray[10, 3]), colname5: float(tarray[10, 4])},
#
#
#             'row12': {colname1: float(tarray[11, 0]), colname2: float(tarray[11, 1]), colname3: float(tarray[11, 2]),
#                       colname4: float(tarray[11, 3]), colname5: float(tarray[11, 4])}
#             }
#
#     table = TableCanvas(tframe, data=data)
#     # table.redraw()
#     table.show()
#
#     master.mainloop()


""" 
Function to create a four column table 
"""
def fourcolumns(col1, col2, col3, col4, colname1, colname2, colname3, colname4):
    array = np.array([col1, col2, col3, col4])
    tarray = np.transpose(array)

    master = Toplevel()
    tframe = Frame(master)
    tframe.pack()

    data = {'row1': {colname1: float(tarray[0, 0]), colname2: float(tarray[0, 1]), colname3: float(tarray[0, 2]),
                     colname4: float(tarray[0, 3])},

            'row2': {colname1: float(tarray[1, 0]), colname2: float(tarray[1, 1]), colname3: float(tarray[1, 2]),
                     colname4: float(tarray[1, 3])},

            'row3': {colname1: float(tarray[2, 0]), colname2: float(tarray[2, 1]), colname3: float(tarray[2, 2]),
                     colname4: float(tarray[2, 3])},

            'row4': {colname1: float(tarray[3, 0]), colname2: float(tarray[3, 1]), colname3: float(tarray[3, 2]),
                     colname4: float(tarray[3, 3])},

            'row5': {colname1: float(tarray[4, 0]), colname2: float(tarray[4, 1]), colname3: float(tarray[4, 2]),
                     colname4: float(tarray[4, 3])},

            'row6': {colname1: float(tarray[5, 0]), colname2: float(tarray[5, 1]), colname3: float(tarray[5, 2]),
                     colname4: float(tarray[5, 3])},

            'row7': {colname1: float(tarray[6, 0]), colname2: float(tarray[6, 1]), colname3: float(tarray[6, 2]),
                     colname4: float(tarray[6, 3])},

            'row8': {colname1: float(tarray[7, 0]), colname2: float(tarray[7, 1]), colname3: float(tarray[7, 2]),
                     colname4: float(tarray[7, 3])},

            'row9': {colname1: float(tarray[8, 0]), colname2: float(tarray[8, 1]), colname3: float(tarray[8, 2]),
                     colname4: float(tarray[8, 3])},

            'row10': {colname1: float(tarray[9, 0]), colname2: float(tarray[9, 1]), colname3: float(tarray[9, 2]),
                      colname4: float(tarray[9, 3])},

            'row11': {colname1: float(tarray[10, 0]), colname2: float(tarray[10, 1]), colname3: float(tarray[10, 2]),
                      colname4: float(tarray[10, 3])},

            'row12': {colname1: float(tarray[11, 0]), colname2: float(tarray[11, 1]), colname3: float(tarray[11, 2]),
                      colname4: float(tarray[11, 3])}
            }

    table = TableCanvas(tframe, data=data)
    # table.redraw()
    table.show()

    master.mainloop()


""" 
Function to create a three column table 
"""
def threecolumns(col1, col2, col3, colname1, colname2, colname3):
    array = np.array([col1, col2, col3])
    tarray = np.transpose(array)

    master = Toplevel()
    tframe = Frame(master)
    tframe.pack()

    data = {'row1': {colname1: float(tarray[0, 0]), colname2: float(tarray[0, 1]), colname3: float(tarray[0, 2])},

            'row2': {colname1: float(tarray[1, 0]), colname2: float(tarray[1, 1]), colname3: float(tarray[1, 2])},

            'row3': {colname1: float(tarray[2, 0]), colname2: float(tarray[2, 1]), colname3: float(tarray[2, 2])},

            'row4': {colname1: float(tarray[3, 0]), colname2: float(tarray[3, 1]), colname3: float(tarray[3, 2])},

            'row5': {colname1: float(tarray[4, 0]), colname2: float(tarray[4, 1]), colname3: float(tarray[4, 2])},

            'row6': {colname1: float(tarray[5, 0]), colname2: float(tarray[5, 1]), colname3: float(tarray[5, 2])},

            'row7': {colname1: float(tarray[6, 0]), colname2: float(tarray[6, 1]), colname3: float(tarray[6, 2])},

            'row8': {colname1: float(tarray[7, 0]), colname2: float(tarray[7, 1]), colname3: float(tarray[7, 2])},

            'row9': {colname1: float(tarray[8, 0]), colname2: float(tarray[8, 1]), colname3: float(tarray[8, 2])},

            'row10': {colname1: float(tarray[9, 0]), colname2: float(tarray[9, 1]), colname3: float(tarray[9, 2])},

            'row11': {colname1: float(tarray[10, 0]), colname2: float(tarray[10, 1]), colname3: float(tarray[10, 2])},

            'row12': {colname1: float(tarray[11, 0]), colname2: float(tarray[11, 1]), colname3: float(tarray[11, 2])}
            }

    table = TableCanvas(tframe, data=data)
    # table.redraw()
    table.show()

    master.mainloop()


""" 
Function to create a two column table 
"""
def twocolumns(col1, col2, colname1, colname2):
    array = np.array([col1, col2])
    tarray = np.transpose(array)

    master = Toplevel()
    tframe = Frame(master)
    tframe.pack()

    data = {'row1': {colname1: float(tarray[0, 0]), colname2: float(tarray[0, 1])},

            'row2': {colname1: float(tarray[1, 0]), colname2: float(tarray[1, 1])},

            'row3': {colname1: float(tarray[2, 0]), colname2: float(tarray[2, 1])},

            'row4': {colname1: float(tarray[3, 0]), colname2: float(tarray[3, 1])},

            'row5': {colname1: float(tarray[4, 0]), colname2: float(tarray[4, 1])},

            'row6': {colname1: float(tarray[5, 0]), colname2: float(tarray[5, 1])},

            'row7': {colname1: float(tarray[6, 0]), colname2: float(tarray[6, 1])},

            'row8': {colname1: float(tarray[7, 0]), colname2: float(tarray[7, 1])},

            'row9': {colname1: float(tarray[8, 0]), colname2: float(tarray[8, 1])},

            'row10': {colname1: float(tarray[9, 0]), colname2: float(tarray[9, 1])},

            'row11': {colname1: float(tarray[10, 0]), colname2: float(tarray[10, 1])},

            'row12': {colname1: float(tarray[11, 0]), colname2: float(tarray[11, 1])}
            }

    table = TableCanvas(tframe, data=data)
    # table.redraw()
    table.show()
    master.mainloop()


""" 
Function to create a one column table 
"""
def onecolumns(col1, colname1):
    array = np.array([col1])
    tarray = np.transpose(array)

    master = Toplevel()
    tframe = Frame(master)
    tframe.pack()

    data = {'row1': {colname1: float(tarray[0, 0])},

            'row2': {colname1: float(tarray[1, 0])},

            'row3': {colname1: float(tarray[2, 0])},

            'row4': {colname1: float(tarray[3, 0])},

            'row5': {colname1: float(tarray[4, 0])},

            'row6': {colname1: float(tarray[5, 0])},

            'row7': {colname1: float(tarray[6, 0])},

            'row8': {colname1: float(tarray[7, 0])},

            'row9': {colname1: float(tarray[8, 0])},

            'row10': {colname1: float(tarray[9, 0])},

            'row11': {colname1: float(tarray[10, 0])},

            'row12': {colname1: float(tarray[11, 0])}
            }

    table = TableCanvas(tframe, data=data)
    # table.redraw()
    table.show()
    master.mainloop()


""" 
Function to generate the simulated/real data table 
"""
def gen_table_sim():
    # Four variables scenario
    # PVSyst, NREL, Solar World and real data
    if globals.pvscheck == 1 and globals.nrelcheck == 1 and globals.swcheck == 1 and globals.realcheck == 1:
        if globals.radioselect == "BifacialGain":
            try:
                globals.pvsBifGain = empirical.bifGainCalc(globals.pvsBifEnergy, globals.pvsMonoEnergy)
                fourcolumns(globals.pvsBifGain, globals.nrelPercentBG, globals.swPercentBG,
                                   globals.realBifacialGain, "PVSyst",
                                   "NREL", "Solar World", "Measured data")
            except:
                MessageBox.showerror("Missing data", "Please load all the corresponding CSV files")

        elif globals.radioselect == "BifacialEnergy":
            try:
                globals.nrelBifEnergy = empirical.bifEnergyCalc(globals.pvsMonoEnergy, globals.nrelBifRatio)
                globals.swBifEnergy = empirical.bifEnergyCalc(globals.pvsMonoEnergy, globals.empiricalList)
                fourcolumns(globals.pvsBifEnergy, globals.nrelBifEnergy, globals.swBifEnergy,
                                   globals.realBifacialEnergy,
                                   "PVSyst", "NREL", "Solar World", "Measured data")
            except:
                MessageBox.showerror("Missing data", "The monofacial energy from PVSyst CSVs and the bifacial gains for"
                                                     " each simulation tool are needed to calculate the bifacial energy")

    # Three variables scenarios
    # PVSyst, NREL and Solar World
    elif globals.pvscheck == 1 and globals.nrelcheck == 1 and globals.swcheck == 1:
        if globals.radioselect == "BifacialGain":
            try:
                globals.pvsBifGain = empirical.bifGainCalc(globals.pvsBifEnergy, globals.pvsMonoEnergy)
                threecolumns(globals.pvsBifGain, globals.nrelPercentBG, globals.swPercentBG, "PVSyst", "NREL",
                                    "Solar World")
            except:
                MessageBox.showerror("Missing data", "Please load all the corresponding CSV files")

        elif globals.radioselect == "BifacialEnergy":
            try:
                globals.nrelBifEnergy = empirical.bifEnergyCalc(globals.pvsMonoEnergy, globals.nrelBifRatio)
                globals.swBifEnergy = empirical.bifEnergyCalc(globals.pvsMonoEnergy, globals.empiricalList)
                threecolumns(globals.pvsBifEnergy, globals.nrelBifEnergy, globals.swBifEnergy, "PVSyst", "NREL",
                                    "Solar World")
            except:
                MessageBox.showerror("Missing data", "The monofacial energy from PVSyst CSVs and the bifacial gains for"
                                                     " each simulation tool are needed to calculate the bifacial energy")

        elif globals.radioselect == "ModuleEnergy":
            try:
                globals.nrelEfficiency = empirical.modEffCalc(globals.nrelBifEnergy, globals.modpower)
                globals.swEfficiency = empirical.modEffCalc(globals.swBifEnergy, globals.modpower)
                threecolumns(globals.pvsEfficiency, globals.nrelEfficiency, globals.swEfficiency, "PVSyst",
                                    "NREL",
                                    "Solar World")
            except:
                MessageBox.showerror("Missing data",
                                     "The bifacial energy from each simulation tool and the module power"
                                     " at PVSyst are needed to calculate the module energy efficiency")

    # PVSyst,NREL and real data
    elif globals.pvscheck == 1 and globals.nrelcheck == 1 and globals.realcheck == 1:
        if globals.radioselect == "BifacialGain":
            try:
                globals.pvsBifGain = empirical.bifGainCalc(globals.pvsBifEnergy, globals.pvsMonoEnergy)
                threecolumns(globals.pvsBifGain, globals.nrelPercentBG, globals.realBifacialGain, "PVSyst",
                                    "NREL",
                                    "Measured data")
            except:
                MessageBox.showerror("Missing data", "Please load all the corresponding CSV files")

        elif globals.radioselect == "BifacialEnergy":
            try:
                globals.nrelBifEnergy = empirical.bifEnergyCalc(globals.pvsMonoEnergy, globals.nrelBifRatio)
                globals.swBifEnergy = empirical.bifEnergyCalc(globals.pvsMonoEnergy, globals.empiricalList)
                threecolumns(globals.pvsBifEnergy, globals.nrelBifEnergy, globals.realBifacialEnergy, "PVSyst",
                                    "NREL",
                                    "Measured data")
            except:
                MessageBox.showerror("Missing data", "The monofacial energy from PVSyst CSVs and the bifacial gains for"
                                                     " each simulation tool are needed to calculate the bifacial energy")

    # PVSyst, Solar World and real data
    elif globals.pvscheck == 1 and globals.swcheck == 1 and globals.realcheck == 1:
        if globals.radioselect == "BifacialGain":
            try:
                globals.pvsBifGain = empirical.bifGainCalc(globals.pvsBifEnergy, globals.pvsMonoEnergy)
                threecolumns(globals.pvsBifGain, globals.swPercentBG, globals.realBifacialGain, "PVSyst",
                                    "Solar World",
                                    "Measured data")
            except:
                MessageBox.showerror("Missing data", "Please load all the corresponding CSV files")

        elif globals.radioselect == "BifacialEnergy":
            try:
                globals.swBifEnergy = empirical.bifEnergyCalc(globals.pvsMonoEnergy, globals.empiricalList)
                threecolumns(globals.pvsBifEnergy, globals.swBifEnergy, globals.realBifacialEnergy, "PVSyst",
                                    "Solar World",
                                    "Measured data")
            except:
                MessageBox.showerror("Missing data", "The monofacial energy from PVSyst CSVs and the bifacial gains for"
                                                     " each simulation tool are needed to calculate the bifacial energy")

    # NREL, Solar World and real data
    elif globals.nrelcheck == 1 and globals.swcheck == 1 and globals.realcheck == 1:
        if globals.radioselect == "BifacialGain":
            try:
                threecolumns(globals.nrelPercentBG, globals.swPercentBG, globals.realBifacialGain, "NREL",
                                    "Solar World",
                                    "Measured data")
            except:
                MessageBox.showerror("Missing data", "Please load all the corresponding CSV files and data")

        elif globals.radioselect == "BifacialEnergy":
            try:
                globals.nrelBifEnergy = empirical.bifEnergyCalc(globals.pvsMonoEnergy, globals.nrelBifRatio)
                globals.swBifEnergy = empirical.bifEnergyCalc(globals.pvsMonoEnergy, globals.empiricalList)
                threecolumns(globals.nrelBifEnergy, globals.swBifEnergy, globals.realBifacialEnergy, "NREL",
                                    "Solar World",
                                    "Measured data")
            except:
                MessageBox.showerror("Missing data", "The monofacial energy from PVSyst CSVs and the bifacial gains for"
                                                     " each simulation tool are needed to calculate the bifacial energy")

    # Two variables scenarios
    # PVSyst and NREL
    elif globals.pvscheck == 1 and globals.nrelcheck == 1:
        if globals.radioselect == "BifacialGain":
            try:
                globals.pvsBifGain = empirical.bifGainCalc(globals.pvsBifEnergy, globals.pvsMonoEnergy)
                twocolumns(globals.pvsBifGain, globals.nrelPercentBG, "PVSyst", "NREL")
            except:
                MessageBox.showerror("Missing data", "Please load all the corresponding CSV files")

        elif globals.radioselect == "BifacialEnergy":
            try:
                globals.nrelBifEnergy = empirical.bifEnergyCalc(globals.pvsMonoEnergy, globals.nrelBifRatio)
                twocolumns(globals.pvsBifEnergy, globals.nrelBifEnergy, "PVSyst", "NREL")
            except:
                MessageBox.showerror("Missing data", "The monofacial energy from PVSyst CSVs and the bifacial gains for"
                                                     " each simulation tool are needed to calculate the bifacial energy")

        elif globals.radioselect == "ModuleEnergy":
            try:
                globals.nrelEfficiency = empirical.modEffCalc(globals.nrelBifEnergy, globals.modpower)
                twocolumns(globals.pvsEfficiency, globals.nrelEfficiency, "PVSyst", "NREL")
            except:
                MessageBox.showerror("Missing data",
                                     "The bifacial energy from each simulation tool and the module power"
                                     " at PVSyst are needed to calculate the module energy efficiency")

    # PVSyst and Solar World
    elif globals.pvscheck == 1 and globals.swcheck == 1:
        if globals.radioselect == "BifacialGain":
            try:
                globals.pvsBifGain = empirical.bifGainCalc(globals.pvsBifEnergy, globals.pvsMonoEnergy)
                twocolumns(globals.pvsBifGain, globals.swPercentBG, "PVSyst", "Solar World")
            except:
                MessageBox.showerror("Missing data", "Please load all the corresponding CSV files and data")

        elif globals.radioselect == "BifacialEnergy":
            try:
                globals.swBifEnergy = empirical.bifEnergyCalc(globals.pvsMonoEnergy, globals.empiricalList)
                twocolumns(globals.pvsBifEnergy, globals.swBifEnergy, "PVSyst", "Solar World")
            except:
                MessageBox.showerror("Missing data", "The monofacial energy from PVSyst CSVs and the bifacial gains for"
                                                     " each simulation tool are needed to calculate the bifacial energy")

        elif globals.radioselect == "ModuleEnergy":
            try:
                globals.swEfficiency = empirical.modEffCalc(globals.swBifEnergy, globals.modpower)
                twocolumns(globals.pvsEfficiency, globals.swEfficiency, "PVSyst", "Solar World")
            except:
                MessageBox.showerror("Missing data",
                                     "The bifacial energy from each simulation tool and the module power"
                                     " at PVSyst are needed to calculate the module energy efficiency")

    # NREL and Solar World
    elif globals.nrelcheck == 1 and globals.swcheck == 1:
        if globals.radioselect == "BifacialGain":
            try:
                twocolumns(globals.nrelPercentBG, globals.swPercentBG, "NREL", "Solar World")
            except:
                MessageBox.showerror("Missing data", "Please load all the corresponding CSV files and data")

        elif globals.radioselect == "BifacialEnergy":
            try:
                globals.nrelBifEnergy = empirical.bifEnergyCalc(globals.pvsMonoEnergy, globals.nrelBifRatio)
                globals.swBifEnergy = empirical.bifEnergyCalc(globals.pvsMonoEnergy, globals.empiricalList)
                twocolumns(globals.nrelBifEnergy, globals.swBifEnergy, "NREL", "Solar World")
            except:
                MessageBox.showerror("Missing data", "The monofacial energy from PVSyst CSVs and the bifacial gains for"
                                                     " each simulation tool are needed to calculate the bifacial energy")

        elif globals.radioselect == "ModuleEnergy":
            try:
                globals.nrelEfficiency = empirical.modEffCalc(globals.nrelBifEnergy, globals.modpower)
                globals.swEfficiency = empirical.modEffCalc(globals.swBifEnergy, globals.modpower)
                twocolumns(globals.nrelEfficiency, globals.swEfficiency, "NREL", "Solar World")
            except:
                MessageBox.showerror("Missing data",
                                     "The bifacial energy from each simulation tool and the module power"
                                     " at PVSyst are needed to calculate the module energy efficiency")

    # PVSyst and real data
    elif globals.pvscheck == 1 and globals.realcheck == 1:
        if globals.radioselect == "BifacialGain":
            try:
                globals.pvsBifGain = empirical.bifGainCalc(globals.pvsBifEnergy, globals.pvsMonoEnergy)
                twocolumns(globals.pvsBifGain, globals.realBifacialGain, "PVSyst", "Measured data")
            except:
                MessageBox.showerror("Missing data", "Please load all the corresponding CSV files")

        elif globals.radioselect == "BifacialEnergy":
            try:
                twocolumns(globals.pvsBifEnergy, globals.realBifacialEnergy, "PVSyst", "Measured data")
            except:
                MessageBox.showerror("Missing data", "Please load all the corresponding CSV files")

    # NREL and real data
    elif globals.nrelcheck == 1 and globals.realcheck == 1:
        if globals.radioselect == "BifacialGain":
            try:
                twocolumns(globals.nrelPercentBG, globals.realBifacialGain, "NREL", "Measured data")
            except:
                MessageBox.showerror("Missing data", "Please load all the corresponding CSV files")

        elif globals.radioselect == "BifacialEnergy":
            try:
                globals.nrelBifEnergy = empirical.bifEnergyCalc(globals.pvsMonoEnergy, globals.nrelBifRatio)
                twocolumns(globals.nrelBifEnergy, globals.realBifacialEnergy, "NREL", "Measured data")
            except:
                MessageBox.showerror("Missing data",
                                     "The monofacial energy from PVSyst CSVs and the bifacial gains for "
                                     "NREL's simulation tool are needed to calculate the bifacial energy")

    # Solar World and real data
    elif globals.swcheck == 1 and globals.realcheck == 1:
        if globals.radioselect == "BifacialGain":
            try:
                twocolumns(globals.swPercentBG, globals.realBifacialGain, "Solar World", "Measured data")
            except:
                MessageBox.showerror("Missing data", "Please input all the values needed for the calculations")

        elif globals.radioselect == "BifacialEnergy":
            try:
                globals.swBifEnergy = empirical.bifEnergyCalc(globals.pvsMonoEnergy, globals.empiricalList)
                twocolumns(globals.swBifEnergy, globals.realBifacialEnergy, "Solar World", "Measured data")
            except:
                MessageBox.showerror("Missing data", "The monofacial energy from PVSyst CSVs and the bifacial gains for"
                                                     " Solar World are needed to calculate the bifacial energy")


    # One variable
    # PVSyst
    elif globals.pvscheck == 1:
        if globals.radioselect == "BifacialGain":
            try:
                globals.pvsBifGain = empirical.bifGainCalc(globals.pvsBifEnergy, globals.pvsMonoEnergy)
                onecolumns(globals.pvsBifGain, "PVSyst")
            except:
                MessageBox.showerror("Missing data", "Please load all the corresponding CSV files")

        elif globals.radioselect == "BifacialEnergy":
            try:
                onecolumns(globals.pvsBifEnergy, "PVSyst")
            except:
                MessageBox.showerror("Missing data", "Please load all the corresponding CSV files")

        elif globals.radioselect == "ModuleEnergy":
            try:
                onecolumns(globals.pvsEfficiency, "PVSyst")
            except:
                MessageBox.showerror("Missing data", "Please load all the corresponding CSV files")

    # NREL
    elif globals.nrelcheck == 1:
        if globals.radioselect == "BifacialGain":
            try:
                onecolumns(globals.nrelPercentBG, "NREL")
            except:
                MessageBox.showerror("Missing data", "Please load all the corresponding CSV files")

        elif globals.radioselect == "BifacialEnergy":
            try:
                globals.nrelBifEnergy = empirical.bifEnergyCalc(globals.pvsMonoEnergy, globals.nrelBifRatio)
                onecolumns(globals.nrelBifEnergy, "NREL")
            except:
                MessageBox.showerror("Missing data",
                                     "The monofacial energy from PVSyst CSVs and the bifacial gains for "
                                     "NREL's simulation tool are needed to calculate the bifacial energy")

        elif globals.radioselect == "ModuleEnergy":
            try:
                globals.nrelEfficiency = empirical.modEffCalc(globals.nrelBifEnergy, globals.modpower)
                onecolumns(globals.nrelEfficiency, "NREL")
            except:
                MessageBox.showerror("Missing data",
                                     "The bifacial energy calculated for NREL and the module power"
                                     " at PVSyst are needed to calculate the module energy efficiency")
    # Solar World
    elif globals.swcheck == 1:
        if globals.radioselect == "BifacialGain":
            try:
                onecolumns(globals.swPercentBG, "Solar World")
            except:
                MessageBox.showerror("Missing data", "Please input all the values needed for the calculations")

        elif globals.radioselect == "BifacialEnergy":
            try:
                globals.swBifEnergy = empirical.bifEnergyCalc(globals.pvsMonoEnergy, globals.empiricalList)
                onecolumns(globals.swBifEnergy, "Solar World")
            except:
                MessageBox.showerror("Missing data", "The monofacial energy from PVSyst CSVs and the bifacial gains for"
                                                     " Solar World are needed to calculate the bifacial energy")

        elif globals.radioselect == "ModuleEnergy":
            try:
                globals.swEfficiency = empirical.modEffCalc(globals.swBifEnergy, globals.modpower)
                onecolumns(globals.swEfficiency, "Solar World")
            except:
                MessageBox.showerror("Missing data",
                                     "The bifacial energy calculation for Solar World and the module power"
                                     " at PVSyst are needed to calculate the module energy efficiency")
    # Real data
    elif globals.realcheck == 1:
        if globals.radioselect == "BifacialGain":
            try:
                onecolumns(globals.realBifacialGain, "Measured data")
            except:
                MessageBox.showerror("Missing data", "Please input all the values needed for the calculations")

        elif globals.radioselect == "BifacialEnergy":
            try:
                onecolumns(globals.realBifacialEnergy, "Measured data")
            except:
                MessageBox.showerror("Missing data", "Please input all the values needed for the calculations")


""" 
Fucntion to generate the errors table 
"""
def gen_table_errors():
    try:
        # PVSyst, NREL and Solar World
        if globals.pvscheck == 1 and globals.nrelcheck == 1 and globals.swcheck == 1:
            if globals.radioselect == "BifacialGain":
                globals.rmsBGpvsyst = [statistics.rmse(i, j) for i, j in
                                       zip(np.array(globals.pvsBifGain), np.array(globals.realBifacialGain))]
                globals.rmsBGnrel = [statistics.rmse(i, j) for i, j in
                                     zip(np.array(globals.nrelPercentBG), np.array(globals.realBifacialGain))]
                globals.rmsBGsw = [statistics.rmse(i, j) for i, j in
                                   zip(np.array(globals.swPercentBG), np.array(globals.realBifacialGain))]

                globals.mbeBGpvsyst = [statistics.mbe(i, j) for i, j in
                                       zip(np.array(globals.pvsBifGain), np.array(globals.realBifacialGain))]
                globals.mbeBGnrel = [statistics.mbe(i, j) for i, j in
                                     zip(np.array(globals.nrelPercentBG), np.array(globals.realBifacialGain))]
                globals.mbeBGsw = [statistics.mbe(i, j) for i, j in
                                   zip(np.array(globals.swPercentBG), np.array(globals.realBifacialGain))]

                sixcolumns(globals.rmsBGpvsyst, globals.rmsBGnrel, globals.rmsBGsw, globals.mbeBGpvsyst,
                           globals.mbeBGnrel, globals.mbeBGsw, "RMSE PVSyst", "RMSE NREL", "RMSE Solar World",
                           "MBE PVSyst", "MBE NREL", "MBE Solar World")

            elif globals.radioselect == "BifacialEnergy":
                globals.rmsBEpvsyst = [statistics.rmse(i, j) for i, j in
                                       zip(np.array(globals.pvsBifEnergy), np.array(globals.realBifacialEnergy))]
                globals.rmsBEnrel = [statistics.rmse(i, j) for i, j in
                                     zip(np.array(globals.nrelBifEnergy), np.array(globals.realBifacialEnergy))]
                globals.rmsBEsw = [statistics.rmse(i, j) for i, j in
                                   zip(np.array(globals.swBifEnergy), np.array(globals.realBifacialEnergy))]

                globals.mbeBEpvsyst = [statistics.mbe(i, j) for i, j in
                                       zip(np.array(globals.pvsBifEnergy), np.array(globals.realBifacialEnergy))]
                globals.mbeBEnrel = [statistics.mbe(i, j) for i, j in
                                     zip(np.array(globals.nrelBifEnergy), np.array(globals.realBifacialEnergy))]
                globals.mbeBEsw = [statistics.mbe(i, j) for i, j in
                                   zip(np.array(globals.swBifEnergy), np.array(globals.realBifacialEnergy))]

                sixcolumns(globals.rmsBEpvsyst, globals.rmsBEnrel, globals.rmsBEsw, globals.mbeBEpvsyst,
                           globals.mbeBEnrel, globals.mbeBEsw, "RMSE PVSyst", "RMSE NREL", "RMSE Solar World",
                           "MBE PVSyst", "MBE NREL", "MBE Solar World")



        # PVSyst and NREL
        elif globals.pvscheck == 1 and globals.nrelcheck == 1:
            if globals.radioselect == "BifacialGain":
                globals.rmsBGpvsyst = [statistics.rmse(i, j) for i, j in
                                       zip(np.array(globals.pvsBifGain), np.array(globals.realBifacialGain))]
                globals.rmsBGnrel = [statistics.rmse(i, j) for i, j in
                                     zip(np.array(globals.nrelPercentBG), np.array(globals.realBifacialGain))]
                globals.mbeBGpvsyst = [statistics.mbe(i, j) for i, j in
                                       zip(np.array(globals.pvsBifGain), np.array(globals.realBifacialGain))]
                globals.mbeBGnrel = [statistics.mbe(i, j) for i, j in
                                     zip(np.array(globals.nrelPercentBG), np.array(globals.realBifacialGain))]

                fourcolumns(globals.rmsBGpvsyst, globals.rmsBGnrel, globals.mbeBGpvsyst, globals.mbeBGnrel,
                            "RMSE PVSyst", "RMSE NREL", "MBE PVSyst", "MBE NREL")

            elif globals.radioselect == "BifacialEnergy":
                globals.rmsBEpvsyst = [statistics.rmse(i, j) for i, j in
                                       zip(np.array(globals.pvsBifEnergy), np.array(globals.realBifacialEnergy))]
                globals.rmsBEnrel = [statistics.rmse(i, j) for i, j in
                                     zip(np.array(globals.nrelBifEnergy), np.array(globals.realBifacialEnergy))]
                globals.mbeBEpvsyst = [statistics.mbe(i, j) for i, j in
                                       zip(np.array(globals.pvsBifEnergy), np.array(globals.realBifacialEnergy))]
                globals.mbeBEnrel = [statistics.mbe(i, j) for i, j in
                                     zip(np.array(globals.nrelBifEnergy), np.array(globals.realBifacialEnergy))]

                fourcolumns(globals.rmsBEpvsyst, globals.rmsBEnrel, globals.mbeBEpvsyst, globals.mbeBEnrel,
                            "RMSE PVSyst", "RMSE NREL", "MBE PVSyst", "MBE NREL")


        # PVSyst and Solar World
        elif globals.pvscheck == 1 and globals.swcheck == 1:
            if globals.radioselect == "BifacialGain":
                globals.rmsBGpvsyst = [statistics.rmse(i, j) for i, j in
                                       zip(np.array(globals.pvsBifGain), np.array(globals.realBifacialGain))]
                globals.rmsBGsw = [statistics.rmse(i, j) for i, j in
                                   zip(np.array(globals.swPercentBG), np.array(globals.realBifacialGain))]
                globals.mbeBGpvsyst = [statistics.mbe(i, j) for i, j in
                                       zip(np.array(globals.pvsBifGain), np.array(globals.realBifacialGain))]
                globals.mbeBGsw = [statistics.mbe(i, j) for i, j in
                                   zip(np.array(globals.swPercentBG), np.array(globals.realBifacialGain))]

                fourcolumns(globals.rmsBGpvsyst, globals.rmsBGsw, globals.mbeBGpvsyst, globals.mbeBGsw,
                            "RMSE PVSyst", "RMSE Solar World", "MBE PVSyst", "MBE Solar World")

            elif globals.radioselect == "BifacialEnergy":
                globals.rmsBEpvsyst = [statistics.rmse(i, j) for i, j in
                                       zip(np.array(globals.pvsBifEnergy), np.array(globals.realBifacialEnergy))]
                globals.rmsBEsw = [statistics.rmse(i, j) for i, j in
                                   zip(np.array(globals.swBifEnergy), np.array(globals.realBifacialEnergy))]
                globals.mbeBEpvsyst = [statistics.mbe(i, j) for i, j in
                                       zip(np.array(globals.pvsBifEnergy), np.array(globals.realBifacialEnergy))]
                globals.mbeBEsw = [statistics.mbe(i, j) for i, j in
                                   zip(np.array(globals.swBifEnergy), np.array(globals.realBifacialEnergy))]

                fourcolumns(globals.rmsBEpvsyst, globals.rmsBEsw, globals.mbeBEpvsyst, globals.mbeBEsw,
                            "RMSE PVSyst", "RMSE Solar World", "MBE PVSyst", "MBE Solar World")


        # NREL and Solar World
        elif globals.nrelcheck == 1 and globals.swcheck == 1:
            if globals.radioselect == "BifacialGain":
                globals.rmsBGnrel = [statistics.rmse(i, j) for i, j in
                                     zip(np.array(globals.nrelPercentBG), np.array(globals.realBifacialGain))]
                globals.rmsBGsw = [statistics.rmse(i, j) for i, j in
                                   zip(np.array(globals.swPercentBG), np.array(globals.realBifacialGain))]
                globals.mbeBGnrel = [statistics.mbe(i, j) for i, j in
                                     zip(np.array(globals.nrelPercentBG), np.array(globals.realBifacialGain))]
                globals.mbeBGsw = [statistics.mbe(i, j) for i, j in
                                   zip(np.array(globals.swPercentBG), np.array(globals.realBifacialGain))]

                fourcolumns(globals.rmsBGnrel, globals.rmsBGsw, globals.mbeBGnrel, globals.mbeBGsw,
                            "RMSE NREL", "RMSE Solar World", "MBE NREL", "MBE Solar World")

            elif globals.radioselect == "BifacialEnergy":
                globals.rmsBEnrel = [statistics.rmse(i, j) for i, j in
                                     zip(np.array(globals.nrelBifEnergy), np.array(globals.realBifacialEnergy))]
                globals.rmsBEsw = [statistics.rmse(i, j) for i, j in
                                   zip(np.array(globals.swBifEnergy), np.array(globals.realBifacialEnergy))]
                globals.mbeBEnrel = [statistics.mbe(i, j) for i, j in
                                     zip(np.array(globals.nrelBifEnergy), np.array(globals.realBifacialEnergy))]
                globals.mbeBEsw = [statistics.mbe(i, j) for i, j in
                                   zip(np.array(globals.swBifEnergy), np.array(globals.realBifacialEnergy))]

                fourcolumns(globals.rmsBEnrel, globals.rmsBEsw, globals.mbeBEnrel, globals.mbeBEsw,
                            "RMSE NREL", "RMSE Solar World", "MBE NREL", "MBE Solar World")


        # PVSyst
        elif globals.pvscheck == 1:
            if globals.radioselect == "BifacialGain":
                globals.rmsBGpvsyst = [statistics.rmse(i, j) for i, j in
                                       zip(np.array(globals.pvsBifGain), np.array(globals.realBifacialGain))]
                globals.mbeBGpvsyst = [statistics.mbe(i, j) for i, j in
                                       zip(np.array(globals.pvsBifGain), np.array(globals.realBifacialGain))]
                twocolumns(globals.rmsBGpvsyst, globals.mbeBGpvsyst, "RMSE PVSyst", "MBE PVSyst")


            elif globals.radioselect == "BifacialEnergy":
                globals.rmsBEpvsyst = [statistics.rmse(i, j) for i, j in
                                       zip(np.array(globals.pvsBifEnergy), np.array(globals.realBifacialEnergy))]
                globals.mbeBEpvsyst = [statistics.mbe(i, j) for i, j in
                                       zip(np.array(globals.pvsBifEnergy), np.array(globals.realBifacialEnergy))]
                twocolumns(globals.rmsBEpvsyst, globals.mbeBEpvsyst, "RMSE PVSyst", "MBE PVSyst")


        # NREL
        elif globals.nrelcheck == 1:
            if globals.radioselect == "BifacialGain":
                globals.rmsBGnrel = [statistics.rmse(i, j) for i, j in
                                     zip(np.array(globals.nrelPercentBG), np.array(globals.realBifacialGain))]
                globals.mbeBGnrel = [statistics.mbe(i, j) for i, j in
                                     zip(np.array(globals.nrelPercentBG), np.array(globals.realBifacialGain))]

                twocolumns(globals.rmsBGnrel, globals.mbeBGnrel, "RMSE NREL", "MBE NREL")



            elif globals.radioselect == "BifacialEnergy":
                globals.rmsBEnrel = [statistics.rmse(i, j) for i, j in
                                     zip(np.array(globals.nrelBifEnergy), np.array(globals.realBifacialEnergy))]
                globals.mbeBEnrel = [statistics.mbe(i, j) for i, j in
                                     zip(np.array(globals.nrelBifEnergy), np.array(globals.realBifacialEnergy))]

                twocolumns(globals.rmsBEnrel, globals.mbeBEnrel, "RMSE NREL", "MBE NREL")


        # Solar World
        elif globals.swcheck == 1:
            if globals.radioselect == "BifacialGain":
                globals.rmsBGsw = [statistics.rmse(i, j) for i, j in
                                   zip(np.array(globals.swPercentBG), np.array(globals.realBifacialGain))]
                globals.mbeBGsw = [statistics.mbe(i, j) for i, j in
                                   zip(np.array(globals.swPercentBG), np.array(globals.realBifacialGain))]

                twocolumns(globals.rmsBGsw, globals.mbeBGsw, "RMSE Solar World", "MBE Solar World")



            elif globals.radioselect == "BifacialEnergy":
                globals.rmsBEsw = [statistics.rmse(i, j) for i, j in
                                   zip(np.array(globals.swBifEnergy), np.array(globals.realBifacialEnergy))]
                globals.mbeBEsw = [statistics.mbe(i, j) for i, j in
                                   zip(np.array(globals.swBifEnergy), np.array(globals.realBifacialEnergy))]

                twocolumns(globals.rmsBEsw, globals.mbeBEsw, "RMSE Solar World", "MBE Solar World")

    except:
        MessageBox.showerror("Missing data",
                             "Missing data: Please load all the corresponding data and plot it to make the calculations needed")