"""
This module contains the functions to estimate the statistical errors
"""
import numpy as np
import globals
from tkinter import messagebox as MessageBox


""" 
Root mean square error (RMSE) - Predictions and targets need to be arrays
"""
def rmse(predictions, targets):
    return np.sqrt(((predictions - targets) ** 2).mean())


""" 
Mean bias error (MBE)  
"""
def mbe(predictions, targets):
    return np.mean(predictions - targets)


"""
Function to calculate the bifacial gain errors
"""
def BGerrors():
    try:
        globals.rmsBGpvsyst = [rmse(i,j) for i,j in zip(np.array(globals.pvsBifGain),np.array(globals.realBifacialGain))]
        globals.rmsBGnrel = [rmse(i,j) for i,j in zip(np.array(globals.nrelPercentBG),np.array(globals.realBifacialGain))]
        globals.rmsBGsw = [rmse(i,j) for i,j in zip(np.array(globals.swPercentBG),np.array(globals.realBifacialGain))]

        globals.mbeBGpvsyst = [mbe(i,j) for i,j in zip(np.array(globals.pvsBifGain),np.array(globals.realBifacialGain))]
        globals.mbeBGnrel = [mbe(i,j) for i,j in zip(np.array(globals.nrelPercentBG),np.array(globals.realBifacialGain))]
        globals.mbeBGsw = [mbe(i,j) for i,j in zip(np.array(globals.swPercentBG),np.array(globals.realBifacialGain))]

    except:
        MessageBox.showerror("Missing data",
                             "Please load all the corresponding CSV files and calculations for all cases"
                             "of Bifacial Gain and Bifacial Energy")


"""
Function to calculate the bifacial energy errors
"""
def BEerrors():
    try:
        globals.rmsBEpvsyst = [rmse(i, j) for i, j in zip(np.array(globals.pvsBifEnergy), np.array(globals.realBifacialEnergy))]
        globals.rmsBEnrel = [rmse(i, j) for i, j in zip(np.array(globals.nrelBifEnergy), np.array(globals.realBifacialEnergy))]
        globals.rmsBEsw = [rmse(i, j) for i, j in zip(np.array(globals.swBifEnergy), np.array(globals.realBifacialEnergy))]

        globals.mbeBEpvsyst = [mbe(i, j) for i, j in zip(np.array(globals.pvsBifEnergy), np.array(globals.realBifacialEnergy))]
        globals.mbeBEnrel = [mbe(i, j) for i, j in zip(np.array(globals.nrelBifEnergy), np.array(globals.realBifacialEnergy))]
        globals.mbeBEsw = [mbe(i, j) for i, j in zip(np.array(globals.swBifEnergy), np.array(globals.realBifacialEnergy))]

    except:
        MessageBox.showerror("Missing data",
                             "Please load all the corresponding CSV files and calculations for all cases"
                             "of Bifacial Gain and Bifacial Energy")
