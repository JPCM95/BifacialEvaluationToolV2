"""
This module contains a function that separates the information retrieved at extraction.py and stores it individually in
dataframes identified with their corresponding simulation tool and the data they contain.
"""

import globals


"""
PVSys case: Check if the user indicates the case of monofacial energy or not, separate the important data from the rest 
and store it in an independent global variable.

NREL case: This function isolates the last column of the dataframe obtained at extraction.py and stores it at an 
individual list (global variable) to be plotted in the next step.
"""
def sort(data):
    """ Extracts the information for PVSyst  """
    if globals.toolname == "PVSyst":
        if globals.monoCheck == 1:
            try:
                monoenergy = data.loc[1:12, 'EArray']                  # Change the column label if necessary
                monoenergyList = monoenergy.tolist()
                for element in monoenergyList:
                    globals.pvsMonoEnergy.append(float(element))
                print("Mono. energy list:", globals.pvsMonoEnergy)
            except:
                pass
        else:
            try:
                energy = data.loc[1:12, 'EArray']                  # Change the column label if necessary
                energyList = energy.tolist()
                for element in energyList:
                    globals.pvsBifEnergy.append(float(element))
                print("Bif. energy list:", globals.pvsBifEnergy)
            except:
                efficiency = data.loc[1:12, 'Ya']                  # Change the column label if necessary
                efficiencyList = efficiency.tolist()
                templist = []
                daysPerMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

                for i in efficiencyList:
                    templist.append(float(i))

                effPerMonth = [i * j for i, j in zip(templist, daysPerMonth)]

                for element in effPerMonth:
                    globals.pvsEfficiency.append(round(element, 4))
                print("Eff. list:", globals.pvsEfficiency)

    """ Extracts the information for NREL Bifacial Radiance  """
    if globals.toolname == "NREL Bifacial Radiance":
        percent = data.iloc[0, 0] * 100
        globals.nrelBifRatio.append(round(data.iloc[0, 0], 4))
        globals.nrelPercentBG.append(round(percent, 4))

        print("NREL back/front ratio:\n")
        print(globals.nrelBifRatio)
        print("NREL percent BGE:\n")
        print(globals.nrelPercentBG)


