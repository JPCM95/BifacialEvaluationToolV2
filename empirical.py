"""
This module contains the functions created to calculate the empirical model's bifacial gain, general bifacial gain,
general bifacial energy and general module energy efficiency.
"""

import numpy as np
import globals


""" 
Function to calculate the empirical model's bifacial gain 
"""
def empmodel(alb, bif, gcr, h):
    bge = alb * bif * 0.95 * (1.95 * (1 - np.sqrt(gcr)) * (1 - np.exp(-8.691 * h * gcr)) + 0.125 * (1 - gcr**4))
    print("\nBGE[%] = {}".format(bge))
    percent = bge * 100
    globals.empiricalList.append(round(bge, 4))
    globals.swPercentBG.append(round(percent, 4))
    print(globals.empiricalList)
    print(globals.swPercentBG)
    return percent


""" 
Function to calculate the general bifacial gain 
"""
def bifGainCalc(list1, list2):
    bgresult = [((i-j) / j)*100 for i, j in zip(list1, list2)]
    return bgresult


""" 
Function to calcule general bifacial energy 
"""
def bifEnergyCalc(monolist, bglist):
    beresult = [i + (i* j) for i, j in zip(monolist, bglist)]
    return beresult


""" 
Function to calculate general module energy efficiency 
"""
def modEffCalc(biflist, pow):
    templist = []

    for ele in biflist:
        templist.append(ele/pow)
    return templist


