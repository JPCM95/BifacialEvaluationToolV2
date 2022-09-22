"""
This module contains the function to plot the different required cases
"""
from tkinter import messagebox as MessageBox
from matplotlib import pyplot as plt
import globals
import empirical


""" Plot style and list containing the months for plotting """
plt.style.use("classic")
months = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]

""" 
General function to plot four different variables. Its inputs are the globals lists for each desired value to graph, 
the names for their labels, the desired label for the Y axis and the main title.
"""
def plotFour(var1, var2, var3, var4, label1, label2, label3, label4, labelY, vartitle):
    # Graph
    plt.close()
    plt.figure("{}".format(vartitle))

    plt.plot(months, var1, marker="o", color="#c0392b", label=label1)
    plt.plot(months, var2, marker="o", color="#3498db", label=label2)
    plt.plot(months, var3, marker="o", color="#27ae60",label=label3)
    plt.plot(months, var4, marker="D", color="#7f8c8d", label=label4, linestyle="--")

    plt.xlabel("Month [-]")
    plt.ylabel(labelY)
    plt.title(vartitle)

    plt.legend()
    plt.tight_layout()
    plt.grid()
    plt.show()


""" 
General function to plot three different variables. Its inputs are the globals lists for each desired value to graph, 
the names for their labels, the desired label for the Y axis and the main title.
"""
def plotThree(var1, var2, var3, label1, label2, label3, labelY, vartitle):
    # Graph
    plt.close()
    plt.figure("{}".format(vartitle))

    plt.plot(months, var1, marker="o", color="#c0392b",label=label1)
    plt.plot(months, var2, marker="o", color="#3498db",label=label2)
    plt.plot(months, var3, marker="o", color="#27ae60", label=label3)

    plt.xlabel("Month [-]")
    plt.ylabel(labelY)
    plt.title(vartitle)

    plt.legend()
    plt.tight_layout()
    plt.grid()
    plt.show()


""" 
General function to plot two different variables. Its inputs are the globals lists for each desired value to graph, the 
names for their labels, the desired label for the Y axis and the main title.
"""
def plotTwo(var1, var2, label1, label2, labelY, vartitle):
    # Graph
    plt.close()
    plt.figure("{}".format(vartitle))

    plt.plot(months, var1, marker="o", color="#c0392b", label=label1)
    plt.plot(months, var2, marker="o", color="#3498db", label=label2)

    plt.xlabel("Month [-]")
    plt.ylabel(labelY)
    plt.title(vartitle)

    plt.legend()
    plt.tight_layout()
    plt.grid()
    plt.show()


"""
General function to plot one different variables. Its inputs are the globals list for the desired value to graph, the 
name for its label, the desired label for the Y axis and the main title.
"""
def plotOne(var1, label1, labelY, vartitle):
    # Graph
    plt.close()
    plt.figure("{}".format(vartitle))
    plt.plot(months, var1, marker="o", color="#c0392b", label=label1)
    plt.xlabel("Month [-]")
    plt.ylabel(labelY)
    plt.title(vartitle)

    plt.legend()
    plt.tight_layout()
    plt.grid()

    plt.show()


""" 
This is the main plotting function. It takes care of evaluating each possible combination from the check and radio 
buttons, calling the functions from empirical.py to calculate the desired values, and call the corresponding function
to plot either one, two or three variables. If any required data is missing, it notifies the user via pop-up window.
"""
def plot():
    # Four variables scenario
    # PVSyst, NREL, Solar World and real data
    if globals.pvscheck == 1 and globals.nrelcheck == 1 and globals.swcheck == 1 and globals.realcheck == 1:
        if globals.radioselect == "BifacialGain":
            try:
                globals.pvsBifGain = empirical.bifGainCalc(globals.pvsBifEnergy, globals.pvsMonoEnergy)
                plotFour(globals.pvsBifGain, globals.nrelPercentBG, globals.swPercentBG, globals.realBifacialGain, "PVSyst",
                         "NREL", "Solar World", "Measured data", "Bifacial gain [%]", "Bifacial gain values per month")
            except:
                MessageBox.showerror("Missing data", "Please load all the corresponding CSV files")

        elif globals.radioselect == "BifacialEnergy":
            try:
                globals.nrelBifEnergy = empirical.bifEnergyCalc(globals.pvsMonoEnergy, globals.nrelBifRatio)
                globals.swBifEnergy = empirical.bifEnergyCalc(globals.pvsMonoEnergy, globals.empiricalList)
                plotFour(globals.pvsBifEnergy, globals.nrelBifEnergy, globals.swBifEnergy, globals.realBifacialEnergy,
                         "PVSyst", "NREL", "Solar World", "Measured data", "Bifacial energy [kWh]", "Bifacial energy values per month")
            except:
                MessageBox.showerror("Missing data", "The monofacial energy from PVSyst CSVs and the bifacial gains for"
                                                     " each simulation tool are needed to calculate the bifacial energy")

    # Three variables scenarios
    # PVSyst, NREL and Solar World
    elif globals.pvscheck == 1 and globals.nrelcheck == 1 and globals.swcheck == 1:
        if globals.radioselect == "BifacialGain":
            try:
                globals.pvsBifGain = empirical.bifGainCalc(globals.pvsBifEnergy, globals.pvsMonoEnergy)
                plotThree(globals.pvsBifGain, globals.nrelPercentBG, globals.swPercentBG, "PVSyst", "NREL",
                          "Solar World",
                          "Bifacial gain [%]", "Bifacial gain values per month")
            except:
                MessageBox.showerror("Missing data", "Please load all the corresponding CSV files")

        elif globals.radioselect == "BifacialEnergy":
            try:
                globals.nrelBifEnergy = empirical.bifEnergyCalc(globals.pvsMonoEnergy, globals.nrelBifRatio)
                globals.swBifEnergy = empirical.bifEnergyCalc(globals.pvsMonoEnergy, globals.empiricalList)
                plotThree(globals.pvsBifEnergy, globals.nrelBifEnergy, globals.swBifEnergy, "PVSyst", "NREL",
                          "Solar World",
                          "Bifacial energy [kWh]", "Bifacial energy values per month")
            except:
                MessageBox.showerror("Missing data", "The monofacial energy from PVSyst CSVs and the bifacial gains for"
                                                     " each simulation tool are needed to calculate the bifacial energy")

        elif globals.radioselect == "ModuleEnergy":
            try:
                globals.nrelEfficiency = empirical.modEffCalc(globals.nrelBifEnergy, globals.modpower)
                globals.swEfficiency = empirical.modEffCalc(globals.swBifEnergy, globals.modpower)
                plotThree(globals.pvsEfficiency, globals.nrelEfficiency, globals.swEfficiency, "PVSyst", "NREL",
                          "Solar World",
                          "Module energy efficiency [kWh/kWp]", "Module energy efficiency values per month")
            except:
                MessageBox.showerror("Missing data", "The bifacial energy from each simulation tool and the module power"
                                                     " at PVSyst are needed to calculate the module energy efficiency")

    # PVSyst,NREL and real data
    elif globals.pvscheck == 1 and globals.nrelcheck == 1 and globals.realcheck == 1:
        if globals.radioselect == "BifacialGain":
            try:
                globals.pvsBifGain = empirical.bifGainCalc(globals.pvsBifEnergy, globals.pvsMonoEnergy)
                plotThree(globals.pvsBifGain, globals.nrelPercentBG, globals.realBifacialGain, "PVSyst", "NREL",
                          "Measured data",
                          "Bifacial gain [%]", "Bifacial gain values per month")
            except:
                MessageBox.showerror("Missing data", "Please load all the corresponding CSV files")

        elif globals.radioselect == "BifacialEnergy":
            try:
                globals.nrelBifEnergy = empirical.bifEnergyCalc(globals.pvsMonoEnergy, globals.nrelBifRatio)
                globals.swBifEnergy = empirical.bifEnergyCalc(globals.pvsMonoEnergy, globals.empiricalList)
                plotThree(globals.pvsBifEnergy, globals.nrelBifEnergy, globals.realBifacialEnergy, "PVSyst", "NREL",
                          "Measured data",
                          "Bifacial energy [kWh]", "Bifacial energy values per month")
            except:
                MessageBox.showerror("Missing data", "The monofacial energy from PVSyst CSVs and the bifacial gains for"
                                                     " each simulation tool are needed to calculate the bifacial energy")

    # PVSyst, Solar World and real data
    elif globals.pvscheck == 1 and globals.swcheck == 1 and globals.realcheck == 1:
        if globals.radioselect == "BifacialGain":
            try:
                globals.pvsBifGain = empirical.bifGainCalc(globals.pvsBifEnergy, globals.pvsMonoEnergy)
                plotThree(globals.pvsBifGain, globals.swPercentBG, globals.realBifacialGain, "PVSyst", "Solar World",
                          "Measured data",
                          "Bifacial gain [%]", "Bifacial gain values per month")
            except:
                MessageBox.showerror("Missing data", "Please load all the corresponding CSV files")

        elif globals.radioselect == "BifacialEnergy":
            try:
                globals.swBifEnergy = empirical.bifEnergyCalc(globals.pvsMonoEnergy, globals.empiricalList)
                plotThree(globals.pvsBifEnergy, globals.swBifEnergy, globals.realBifacialEnergy, "PVSyst", "Solar World",
                          "Measured data",
                          "Bifacial energy [kWh]", "Bifacial energy values per month")
            except:
                MessageBox.showerror("Missing data", "The monofacial energy from PVSyst CSVs and the bifacial gains for"
                                                     " each simulation tool are needed to calculate the bifacial energy")

    # NREL, Solar World and real data
    elif globals.nrelcheck == 1 and globals.swcheck == 1 and globals.realcheck == 1:
        if globals.radioselect == "BifacialGain":
            try:
                plotThree(globals.nrelPercentBG, globals.swPercentBG, globals.realBifacialGain, "NREL", "Solar World",
                          "Measured data", "Bifacial gain [%]", "Bifacial gain values per month")
            except:
                MessageBox.showerror("Missing data", "Please load all the corresponding CSV files and data")

        elif globals.radioselect == "BifacialEnergy":
            try:
                globals.nrelBifEnergy = empirical.bifEnergyCalc(globals.pvsMonoEnergy, globals.nrelBifRatio)
                globals.swBifEnergy = empirical.bifEnergyCalc(globals.pvsMonoEnergy, globals.empiricalList)
                plotThree(globals.nrelBifEnergy, globals.swBifEnergy, globals.realBifacialEnergy, "NREL", "Solar World",
                          "Measured data", "Bifacial energy [kWh]", "Bifacial energy values per month")
            except:
                MessageBox.showerror("Missing data", "The monofacial energy from PVSyst CSVs and the bifacial gains for"
                                                     " each simulation tool are needed to calculate the bifacial energy")

    # Two variables scenarios
    # PVSyst and NREL
    elif globals.pvscheck == 1 and globals.nrelcheck == 1:
        if globals.radioselect == "BifacialGain":
            try:
                globals.pvsBifGain = empirical.bifGainCalc(globals.pvsBifEnergy, globals.pvsMonoEnergy)
                plotTwo(globals.pvsBifGain, globals.nrelPercentBG, "PVSyst", "NREL", "Bifacial gain [%]",
                        "Bifacial gain values per month")
            except:
                MessageBox.showerror("Missing data", "Please load all the corresponding CSV files")

        elif globals.radioselect == "BifacialEnergy":
            try:
                globals.nrelBifEnergy = empirical.bifEnergyCalc(globals.pvsMonoEnergy, globals.nrelBifRatio)
                plotTwo(globals.pvsBifEnergy, globals.nrelBifEnergy, "PVSyst", "NREL", "Bifacial energy [kWh]",
                        "Bifacial energy values per month")
            except:
                MessageBox.showerror("Missing data", "The monofacial energy from PVSyst CSVs and the bifacial gains for"
                                                     " each simulation tool are needed to calculate the bifacial energy")

        elif globals.radioselect == "ModuleEnergy":
            try:
                globals.nrelEfficiency = empirical.modEffCalc(globals.nrelBifEnergy, globals.modpower)
                plotTwo(globals.pvsEfficiency, globals.nrelEfficiency, "PVSyst", "NREL", "Module energy efficiency [kWh/kWp]",
                        "Module energy efficiency per month")
            except:
                MessageBox.showerror("Missing data",
                                     "The bifacial energy from each simulation tool and the module power"
                                     " at PVSyst are needed to calculate the module energy efficiency")

    # PVSyst and Solar World
    elif globals.pvscheck == 1 and globals.swcheck == 1:
        if globals.radioselect == "BifacialGain":
            try:
                globals.pvsBifGain = empirical.bifGainCalc(globals.pvsBifEnergy, globals.pvsMonoEnergy)
                plotTwo(globals.pvsBifGain, globals.swPercentBG, "PVSyst", "Solar World", "Bifacial gain [%]",
                        "Bifacial gain values per month")
            except:
                MessageBox.showerror("Missing data", "Please load all the corresponding CSV files and data")

        elif globals.radioselect == "BifacialEnergy":
            try:
                globals.swBifEnergy = empirical.bifEnergyCalc(globals.pvsMonoEnergy, globals.empiricalList)
                plotTwo(globals.pvsBifEnergy, globals.swBifEnergy, "PVSyst", "Solar World", "Bifacial energy [kWh]",
                        "Bifacial energy values per month")
            except:
                MessageBox.showerror("Missing data", "The monofacial energy from PVSyst CSVs and the bifacial gains for"
                                                     " each simulation tool are needed to calculate the bifacial energy")

        elif globals.radioselect == "ModuleEnergy":
            try:
                globals.swEfficiency = empirical.modEffCalc(globals.swBifEnergy, globals.modpower)
                plotTwo(globals.pvsEfficiency, globals.swEfficiency, "PVSyst", "Solar World", "Module energy efficiency [kWh/kWp]",
                        "Module energy efficiency per month")
            except:
                MessageBox.showerror("Missing data",
                                     "The bifacial energy from each simulation tool and the module power"
                                     " at PVSyst are needed to calculate the module energy efficiency")

    # NREL and Solar World
    elif globals.nrelcheck == 1 and globals.swcheck == 1:
        if globals.radioselect == "BifacialGain":
            try:
                plotTwo(globals.nrelPercentBG, globals.swPercentBG, "NREL", "Solar World", "Bifacial gain [%]",
                        "Bifacial gain values per month")
            except:
                MessageBox.showerror("Missing data", "Please load all the corresponding CSV files and data")

        elif globals.radioselect == "BifacialEnergy":
            try:
                globals.nrelBifEnergy = empirical.bifEnergyCalc(globals.pvsMonoEnergy, globals.nrelBifRatio)
                globals.swBifEnergy = empirical.bifEnergyCalc(globals.pvsMonoEnergy, globals.empiricalList)
                plotTwo(globals.nrelBifEnergy, globals.swBifEnergy, "NREL", "Solar World", "Bifacial energy [kWh]",
                        "Bifacial energy values per month")
            except:
                MessageBox.showerror("Missing data", "The monofacial energy from PVSyst CSVs and the bifacial gains for"
                                                     " each simulation tool are needed to calculate the bifacial energy")

        elif globals.radioselect == "ModuleEnergy":
            try:
                globals.nrelEfficiency = empirical.modEffCalc(globals.nrelBifEnergy, globals.modpower)
                globals.swEfficiency = empirical.modEffCalc(globals.swBifEnergy, globals.modpower)
                plotTwo(globals.nrelEfficiency, globals.swEfficiency, "NREL", "Solar World", "Module energy efficiency [kWh/kWp]",
                        "Module energy efficiency per month")
            except:
                MessageBox.showerror("Missing data",
                                     "The bifacial energy from each simulation tool and the module power"
                                     " at PVSyst are needed to calculate the module energy efficiency")

    #PVSyst and real data
    elif globals.pvscheck == 1 and globals.realcheck == 1:
        if globals.radioselect == "BifacialGain":
            try:
                globals.pvsBifGain = empirical.bifGainCalc(globals.pvsBifEnergy, globals.pvsMonoEnergy)
                plotTwo(globals.pvsBifGain, globals.realBifacialGain, "PVSyst", "Measured data", "Bifacial gain [%]",
                        "Bifacial gain values per month")
            except:
                MessageBox.showerror("Missing data", "Please load all the corresponding CSV files")

        elif globals.radioselect == "BifacialEnergy":
            try:
                plotTwo(globals.pvsBifEnergy, globals.realBifacialEnergy, "PVSyst", "Measured data", "Bifacial energy [kWh]",
                        "Bifacial energy values per month")
            except:
                MessageBox.showerror("Missing data", "Please load all the corresponding CSV files")

    # NREL and real data
    elif globals.nrelcheck == 1 and globals.realcheck == 1:
        if globals.radioselect == "BifacialGain":
            try:
                plotTwo(globals.nrelPercentBG, globals.realBifacialGain, "NREL", "Measured data", "Bifacial gain [%]",
                        "Bifacial gain values per month")
            except:
                MessageBox.showerror("Missing data", "Please load all the corresponding CSV files")

        elif globals.radioselect == "BifacialEnergy":
            try:
                globals.nrelBifEnergy = empirical.bifEnergyCalc(globals.pvsMonoEnergy, globals.nrelBifRatio)
                plotTwo(globals.nrelBifEnergy, globals.realBifacialEnergy, "NREL", "Measured data",
                        "Bifacial energy [kWh]", "Bifacial energy values per month")
            except:
                MessageBox.showerror("Missing data", "The monofacial energy from PVSyst CSVs and the bifacial gains for "
                                                     "NREL's simulation tool are needed to calculate the bifacial energy")

    # Solar World and real data
    elif globals.swcheck == 1 and globals.realcheck == 1:
        if globals.radioselect == "BifacialGain":
            try:
                plotTwo(globals.swPercentBG, globals.realBifacialGain, "Solar World", "Measured data", "Bifacial gain [%]",
                        "Bifacial gain values per month")
            except:
                MessageBox.showerror("Missing data", "Please input all the values needed for the calculations")

        elif globals.radioselect == "BifacialEnergy":
            try:
                globals.swBifEnergy = empirical.bifEnergyCalc(globals.pvsMonoEnergy, globals.empiricalList)
                plotTwo(globals.swBifEnergy, globals.realBifacialEnergy, "Solar World", "Measured data", "Bifacial energy [kWh]",
                        "Bifacial energy values per month")
            except:
                MessageBox.showerror("Missing data", "The monofacial energy from PVSyst CSVs and the bifacial gains for"
                                                     " Solar World are needed to calculate the bifacial energy")


    # One variable
    # PVSyst
    elif globals.pvscheck == 1:
        if globals.radioselect == "BifacialGain":
            try:
                globals.pvsBifGain = empirical.bifGainCalc(globals.pvsBifEnergy, globals.pvsMonoEnergy)
                plotOne(globals.pvsBifGain, "PVSyst", "Bifacial gain [%]", "Bifacial gain values per month")
            except:
                MessageBox.showerror("Missing data", "Please load all the corresponding CSV files")

        elif globals.radioselect == "BifacialEnergy":
            try:
                plotOne(globals.pvsBifEnergy, "PVSyst", "Bifacial energy [kWh]", "Bifacial energy values per month")
            except:
                MessageBox.showerror("Missing data", "Please load all the corresponding CSV files")

        elif globals.radioselect == "ModuleEnergy":
            try:
                plotOne(globals.pvsEfficiency,"PVSyst", "Module energy efficiency [kWh/kWp]", "Module energy efficiency per month")
            except:
                MessageBox.showerror("Missing data", "Please load all the corresponding CSV files")

    # NREL
    elif globals.nrelcheck == 1:
        if globals.radioselect == "BifacialGain":
            try:
                plotOne(globals.nrelPercentBG, "NREL", "Bifacial gain [%]", "Bifacial gain values per month")
            except:
                MessageBox.showerror("Missing data", "Please load all the corresponding CSV files")

        elif globals.radioselect == "BifacialEnergy":
            try:
                globals.nrelBifEnergy = empirical.bifEnergyCalc(globals.pvsMonoEnergy, globals.nrelBifRatio)
                plotOne(globals.nrelBifEnergy, "NREL", "Bifacial energy [kWh]", "Bifacial energy values per month")
            except:
                MessageBox.showerror("Missing data", "The monofacial energy from PVSyst CSVs and the bifacial gains for "
                                                     "NREL's simulation tool are needed to calculate the bifacial energy")

        elif globals.radioselect == "ModuleEnergy":
            try:
                globals.nrelEfficiency = empirical.modEffCalc(globals.nrelBifEnergy, globals.modpower)
                plotOne(globals.nrelEfficiency, "NREL", "Module energy efficiency [kWh/kWp]", "Module energy efficiency per month")
            except:
                MessageBox.showerror("Missing data",
                                     "The bifacial energy calculated for NREL and the module power"
                                     " at PVSyst are needed to calculate the module energy efficiency")
    # Solar World
    elif globals.swcheck == 1:
        if globals.radioselect == "BifacialGain":
            try:
                plotOne(globals.swPercentBG, "Solar World", "Bifacial gain [%]", "Bifacial gain values per month")
            except:
                MessageBox.showerror("Missing data", "Please input all the values needed for the calculations")

        elif globals.radioselect == "BifacialEnergy":
            try:
                globals.swBifEnergy = empirical.bifEnergyCalc(globals.pvsMonoEnergy, globals.empiricalList)
                plotOne(globals.swBifEnergy, "Solar World", "Bifacial energy [kWh]", "Bifacial energy values per month")
            except:
                MessageBox.showerror("Missing data", "The monofacial energy from PVSyst CSVs and the bifacial gains for"
                                                     " Solar World are needed to calculate the bifacial energy")

        elif globals.radioselect == "ModuleEnergy":
            try:
                globals.swEfficiency = empirical.modEffCalc(globals.swBifEnergy, globals.modpower)
                plotOne(globals.swEfficiency, "Solar World", "Module energy efficiency [kWh/kWp]", "Module energy efficiency per month")
            except:
                MessageBox.showerror("Missing data",
                                     "The bifacial energy calculation for Solar World and the module power"
                                     " at PVSyst are needed to calculate the module energy efficiency")
    # Real data
    elif globals.realcheck == 1:
        if globals.radioselect == "BifacialGain":
            try:
                plotOne(globals.realBifacialGain, "Measured data", "Bifacial gain [%]", "Bifacial gain values per month")
            except:
                MessageBox.showerror("Missing data", "Please input all the values needed for the calculations")

        elif globals.radioselect == "BifacialEnergy":
            try:
                plotOne(globals.realBifacialEnergy, "Measured data", "Bifacial energy [kWh]", "Bifacial energy values per month")
            except:
                MessageBox.showerror("Missing data", "Please input all the values needed for the calculations")


"""
This function plots errors (RMSE and MBE) and the different cases depending on the variables desired 
"""
def plotErrors():
    try:
        plt.close("all")
        # PVSyst, NREL and Solar World
        if globals.pvscheck == 1 and globals.nrelcheck == 1 and globals.swcheck == 1:
            x = months
            if globals.radioselect == "BifacialGain":

                y1 = globals.rmsBGpvsyst
                y2 = globals.rmsBGnrel
                y3 = globals.rmsBGsw

                y4 = globals.mbeBGpvsyst
                y5 = globals.mbeBGnrel
                y6 = globals.mbeBGsw

                plt.figure("Errors for Bifacial Gain in Energy (BGE)")
                plt.subplot(2, 1, 1)
                plt.plot(x, y1, marker="o", label="PVSyst")
                plt.plot(x, y2, marker="o", label="NREL")
                plt.plot(x, y3, marker="o", label="Solar World")
                plt.title("Bifacial Gain in Energy (BGE)")
                plt.ylabel("RMSE [%]")
                plt.legend()
                plt.tight_layout()
                plt.grid()

                plt.subplot(2, 1, 2)
                plt.plot(x, y4, marker="o", label="PVSyst")
                plt.plot(x, y5, marker="o", label="NREL")
                plt.plot(x, y6, marker="o", label="Solar World")
                plt.xlabel("Month [-]")
                plt.ylabel("MBE [%]")
                plt.legend()
                plt.tight_layout()
                plt.grid()

                plt.show()

            elif globals.radioselect == "BifacialEnergy":

                y7 = globals.rmsBEpvsyst
                y8 = globals.rmsBEnrel
                y9 = globals.rmsBEsw

                y10 = globals.mbeBEpvsyst
                y11 = globals.mbeBEnrel
                y12 = globals.mbeBEsw

                plt.figure("Errors for Bifacial Energy")
                plt.subplot(2, 1, 1)
                plt.plot(x, y7, marker="o", label="PVSyst")
                plt.plot(x, y8, marker="o", label="NREL")
                plt.plot(x, y9, marker="o", label="Solar World")
                plt.title("Bifacial Energy")
                plt.ylabel("RMSE [%]")
                plt.legend()
                plt.tight_layout()
                plt.grid()

                plt.subplot(2, 1, 2)
                plt.plot(x, y10, marker="o", label="PVSyst")
                plt.plot(x, y11, marker="o", label="NREL")
                plt.plot(x, y12, marker="o", label="Solar World")
                plt.xlabel("Month [-]")
                plt.ylabel("MBE [%]")
                plt.legend()
                plt.tight_layout()
                plt.grid()

                plt.show()

        # PVSyst and NREL
        elif globals.pvscheck == 1 and globals.nrelcheck == 1:
            x = months
            if globals.radioselect == "BifacialGain":

                y1 = globals.rmsBGpvsyst
                y2 = globals.rmsBGnrel

                y4 = globals.mbeBGpvsyst
                y5 = globals.mbeBGnrel

                plt.figure("Errors for Bifacial Gain in Energy (BGE)")
                plt.subplot(2, 1, 1)
                plt.plot(x, y1, marker="o", label="PVSyst")
                plt.plot(x, y2, marker="o", label="NREL")
                plt.title("Bifacial Gain in Energy (BGE)")
                plt.ylabel("RMSE [%]")
                plt.legend()
                plt.tight_layout()
                plt.grid()

                plt.subplot(2, 1, 2)
                plt.plot(x, y4, marker="o", label="PVSyst")
                plt.plot(x, y5, marker="o", label="NREL")
                plt.xlabel("Month [-]")
                plt.ylabel("MBE [%]")
                plt.legend()
                plt.tight_layout()
                plt.grid()

                plt.show()

            elif globals.radioselect == "BifacialEnergy":

                y7 = globals.rmsBEpvsyst
                y8 = globals.rmsBEnrel
                y10 = globals.mbeBEpvsyst
                y11 = globals.mbeBEnrel

                plt.figure("Errors for Bifacial Energy")
                plt.subplot(2, 1, 1)
                plt.plot(x, y7, marker="o", label="PVSyst")
                plt.plot(x, y8, marker="o", label="NREL")
                plt.title("Bifacial Energy")
                plt.ylabel("RMSE [%]")
                plt.legend()
                plt.tight_layout()
                plt.grid()

                plt.subplot(2, 1, 2)
                plt.plot(x, y10, marker="o", label="PVSyst")
                plt.plot(x, y11, marker="o", label="NREL")
                plt.xlabel("Month [-]")
                plt.ylabel("MBE [%]")
                plt.legend()
                plt.tight_layout()
                plt.grid()

                plt.show()

        # PVSyst and Solar World
        elif globals.pvscheck == 1 and globals.swcheck == 1:
            x = months
            if globals.radioselect == "BifacialGain":

                y1 = globals.rmsBGpvsyst
                y3 = globals.rmsBGsw
                y4 = globals.mbeBGpvsyst
                y6 = globals.mbeBGsw

                plt.figure("Errors for Bifacial Gain in Energy (BGE)")
                plt.subplot(2, 1, 1)
                plt.plot(x, y1, marker="o", label="PVSyst")
                plt.plot(x, y3, marker="o", label="Solar World")
                plt.title("Bifacial Gain in Energy (BGE)")
                plt.ylabel("RMSE [%]")
                plt.legend()
                plt.tight_layout()
                plt.grid()

                plt.subplot(2, 1, 2)
                plt.plot(x, y4, marker="o", label="PVSyst")
                plt.plot(x, y6, marker="o", label="Solar World")
                plt.xlabel("Month [-]")
                plt.ylabel("MBE [%]")
                plt.legend()
                plt.tight_layout()
                plt.grid()
                plt.show()

            elif globals.radioselect == "BifacialEnergy":
                y7 = globals.rmsBEpvsyst
                y9 = globals.rmsBEsw
                y10 = globals.mbeBEpvsyst
                y12 = globals.mbeBEsw

                plt.figure("Errors for Bifacial Energy")
                plt.subplot(2, 1, 1)
                plt.plot(x, y7, marker="o", label="PVSyst")
                plt.plot(x, y9, marker="o", label="Solar World")
                plt.title("Bifacial Energy")
                plt.ylabel("RMSE [%]")
                plt.legend()
                plt.tight_layout()
                plt.grid()

                plt.subplot(2, 1, 2)
                plt.plot(x, y10, marker="o", label="PVSyst")
                plt.plot(x, y12, marker="o", label="Solar World")
                plt.xlabel("Month [-]")
                plt.ylabel("MBE [%]")
                plt.legend()
                plt.tight_layout()
                plt.grid()

                plt.show()

        # NREL and Solar World
        elif globals.nrelcheck == 1 and globals.swcheck == 1:
            x = months
            if globals.radioselect == "BifacialGain":

                y2 = globals.rmsBGnrel
                y3 = globals.rmsBGsw
                y5 = globals.mbeBGnrel
                y6 = globals.mbeBGsw

                plt.figure("Errors for Bifacial Gain in Energy (BGE)")
                plt.subplot(2, 1, 1)
                plt.plot(x, y2, marker="o", label="NREL")
                plt.plot(x, y3, marker="o", label="Solar World")
                plt.title("Bifacial Gain in Energy (BGE)")
                plt.ylabel("RMSE [%]")
                plt.legend()
                plt.tight_layout()
                plt.grid()

                plt.subplot(2, 1, 2)
                plt.plot(x, y5, marker="o", label="NREL")
                plt.plot(x, y6, marker="o", label="Solar World")
                plt.xlabel("Month [-]")
                plt.ylabel("MBE [%]")
                plt.legend()
                plt.tight_layout()
                plt.grid()
                plt.show()

            elif globals.radioselect == "BifacialEnergy":
                y8 = globals.rmsBEnrel
                y9 = globals.rmsBEsw
                y11 = globals.mbeBEnrel
                y12 = globals.mbeBEsw

                plt.figure("Errors for Bifacial Energy")
                plt.subplot(2, 1, 1)
                plt.plot(x, y8, marker="o", label="NREL")
                plt.plot(x, y9, marker="o", label="Solar World")
                plt.title("Bifacial Energy")
                plt.ylabel("RMSE [%]")
                plt.legend()
                plt.tight_layout()
                plt.grid()

                plt.subplot(2, 1, 2)
                plt.plot(x, y11, marker="o", label="NREL")
                plt.plot(x, y12, marker="o", label="Solar World")
                plt.xlabel("Month [-]")
                plt.ylabel("MBE [%]")
                plt.legend()
                plt.tight_layout()
                plt.grid()

                plt.show()

        # PVSyst
        elif globals.pvscheck == 1:
            x = months
            if globals.radioselect == "BifacialGain":

                y1 = globals.rmsBGpvsyst
                y4 = globals.mbeBGpvsyst

                plt.figure("Errors for Bifacial Gain in Energy (BGE)")
                plt.subplot(2, 1, 1)
                plt.plot(x, y1, marker="o", label="PVSyst")
                plt.title("Bifacial Gain in Energy (BGE)")
                plt.ylabel("RMSE [%]")
                plt.legend()
                plt.tight_layout()
                plt.grid()

                plt.subplot(2, 1, 2)
                plt.plot(x, y4, marker="o", label="PVSyst")
                plt.xlabel("Month [-]")
                plt.ylabel("MBE [%]")
                plt.legend()
                plt.tight_layout()
                plt.grid()
                plt.show()

            elif globals.radioselect == "BifacialEnergy":
                y7 = globals.rmsBEpvsyst
                y10 = globals.mbeBEpvsyst

                plt.figure("Errors for Bifacial Energy")
                plt.subplot(2, 1, 1)
                plt.plot(x, y7, marker="o", label="PVSyst")
                plt.title("Bifacial Energy")
                plt.ylabel("RMSE [%]")
                plt.legend()
                plt.tight_layout()
                plt.grid()

                plt.subplot(2, 1, 2)
                plt.plot(x, y10, marker="o", label="PVSyst")
                plt.xlabel("Month [-]")
                plt.ylabel("MBE [%]")
                plt.legend()
                plt.tight_layout()
                plt.grid()

                plt.show()

        # NREL
        elif globals.nrelcheck == 1:
            x = months
            if globals.radioselect == "BifacialGain":

                y2 = globals.rmsBGnrel
                y5 = globals.mbeBGnrel

                plt.figure("Errors for Bifacial Gain in Energy (BGE)")
                plt.subplot(2, 1, 1)
                plt.plot(x, y2, marker="o", label="NREL")
                plt.title("Bifacial Gain in Energy (BGE)")
                plt.ylabel("RMSE [%]")
                plt.legend()
                plt.tight_layout()
                plt.grid()

                plt.subplot(2, 1, 2)
                plt.plot(x, y5, marker="o", label="NREL")
                plt.xlabel("Month [-]")
                plt.ylabel("MBE [%]")
                plt.legend()
                plt.tight_layout()
                plt.grid()

                plt.show()

            elif globals.radioselect == "BifacialEnergy":
                y8 = globals.rmsBEnrel
                y11 = globals.mbeBEnrel

                plt.figure("Errors for Bifacial Energy")
                plt.subplot(2, 1, 1)
                plt.plot(x, y8, marker="o", label="NREL")
                plt.title("Bifacial Energy")
                plt.ylabel("RMSE [%]")
                plt.legend()
                plt.tight_layout()
                plt.grid()

                plt.subplot(2, 1, 2)
                plt.plot(x, y11, marker="o", label="NREL")
                plt.xlabel("Month [-]")
                plt.ylabel("MBE [%]")
                plt.legend()
                plt.tight_layout()
                plt.grid()

                plt.show()

        # Solar World
        elif globals.swcheck == 1:
            x = months
            if globals.radioselect == "BifacialGain":

                y3 = globals.rmsBGsw
                y6 = globals.mbeBGsw

                plt.figure("Errors for Bifacial Gain in Energy (BGE)")
                plt.subplot(2, 1, 1)
                plt.plot(x, y3, marker="o", label="Solar World")
                plt.title("Bifacial Gain in Energy (BGE)")
                plt.ylabel("RMSE [%]")
                plt.legend()
                plt.tight_layout()
                plt.grid()

                plt.subplot(2, 1, 2)
                plt.plot(x, y6, marker="o", label="Solar World")
                plt.xlabel("Month [-]")
                plt.ylabel("MBE [%]")
                plt.legend()
                plt.tight_layout()
                plt.grid()

                plt.show()

            elif globals.radioselect == "BifacialEnergy":
                y9 = globals.rmsBEsw
                y12 = globals.mbeBEsw

                plt.figure("Errors for Bifacial Energy")
                plt.subplot(2, 1, 1)
                plt.plot(x, y9, marker="o", label="Solar World")
                plt.title("Bifacial Energy")
                plt.ylabel("RMSE [%]")
                plt.legend()
                plt.tight_layout()
                plt.grid()

                plt.subplot(2, 1, 2)
                plt.plot(x, y12, marker="o", label="Solar World")
                plt.xlabel("Month [-]")
                plt.ylabel("MBE [%]")
                plt.legend()
                plt.tight_layout()
                plt.grid()

                plt.show()
    except:
        MessageBox.showerror("Missing data","Missing data: Please load all the corresponding data and plot it to make the calculations needed")











