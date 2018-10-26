import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

path = "/Users/av/Documents/Drilling/unsuper_learn/"

# All Depth Converted Data
Alpha = pd.read_csv(path+"AlphaDepthConvertedData.csv")
Bravo = pd.read_csv(path+"BravoDepthConvertedData.csv")
Charlie = pd.read_csv(path+"CharlieDepthConvertedData.csv")
Delta = pd.read_csv(path+"DeltaDepthConvertedData.csv")
Foxtrot = pd.read_csv(path+"FoxtrotDepthConvertedData.csv")

# The paper used WOB, RPM, and flow rate of drilling mud
# I don't know what the deal with the cleansed values is, but they are all that's in this data set
# If nothing else, gives us a starting point

# save feature names
features_list = list(Alpha[["RT 01S VC WEIGHT ON BIT CLEANSED VALUE", "RT 01S SURFACE TORQUE CLEANSED VALUE",
                  "RT 01S SURFACE RPM CLEANSED VALUE", "RT 01S FLOW RATE OUT CLEANSED VALUE"]].columns)

features = np.array(Alpha[["RT 01S VC WEIGHT ON BIT CLEANSED VALUE", "RT 01S SURFACE TORQUE CLEANSED VALUE",
                  "RT 01S SURFACE RPM CLEANSED VALUE", "RT 01S FLOW RATE OUT CLEANSED VALUE"]])

labels = np.array(Alpha["RT 01S VC ON BOTTOM ROP"])




