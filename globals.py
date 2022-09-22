""" This module contains all the global variables used across the different modules. """


""" Name of the simulation tool used """
toolname = ""

""" File path for PVSyst csv """
pvfilepath = ""

""" PVSyst data lists """
modpower = float
pvsMonoEnergy = []
pvsBifEnergy = []
pvsEfficiency = []
pvsBifGain = []

""" Check for the usage of monofacial energy """
monoCheck = int

""" File path for NREL csv """
filepath = ""

""" NREL data lists """
nrelBifRatio = []
nrelBifEnergy = []
nrelEfficiency = []
nrelPercentBG = []

""" Solar World data lists """
empiricalList = []
swBifEnergy = []
swEfficiency = []
swPercentBG = []

""" Measured data lists """
realBifacialGain = []
realBifacialEnergy = []

""" Boolean values for the check buttons """
pvscheck = int
nrelcheck = int
swcheck = int
realcheck = int

""" String value for radio buttons """
radioselect = ""

""" Error lists """
# Bifacial gain errors
rmsBGpvsyst = []
rmsBGnrel = []
rmsBGsw = []
mbeBGpvsyst = []
mbeBGnrel = []
mbeBGsw = []

""" Bifacial energy errors """
rmsBEpvsyst = []
rmsBEnrel = []
rmsBEsw = []
mbeBEpvsyst = []
mbeBEnrel = []
mbeBEsw = []