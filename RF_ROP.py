import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.model_selection import LeaveOneOut
from sklearn.metrics import mean_squared_error
from math import sqrt

path = "/Users/av/Documents/Drilling/unsuper_learn/"

# All Depth Converted Data
Alpha = pd.read_csv(path+"AlphaDepthConvertedData.csv")
Bravo = pd.read_csv(path+"BravoDepthConvertedData.csv")
Charlie = pd.read_csv(path+"CharlieDepthConvertedData.csv")
Delta = pd.read_csv(path+"DeltaDepthConvertedData.csv")
Foxtrot = pd.read_csv(path+"FoxtrotDepthConvertedData.csv")

Alpha.name = 'Alpha'
Bravo.name = 'Bravo'
Charlie.name = 'Charlie'
Delta.name = 'Delta'
Foxtrot.name = 'Foxtrot'

dfs = [Alpha, Bravo, Charlie, Delta, Foxtrot]
loo = LeaveOneOut()

for train_idx, test_idx in loo.split(dfs):  # train on 4 wells and test on the 5th
    print("TRAIN:", train_idx, "TEST:", test_idx)

    train_set = pd.concat(dfs[i] for i in train_idx.tolist())
    test_set = dfs[test_idx.tolist()[0]]
    # The paper used WOB, RPM, and flow rate of drilling mud
    # I don't know what the deal with the cleansed values is, but they are all that's in this data set
    # If nothing else, gives us a starting point
    features_list = features_list = list(train_set[["RT 01S VC WEIGHT ON BIT CLEANSED VALUE", "RT 01S SURFACE TORQUE CLEANSED VALUE",
                                                    "RT 01S SURFACE RPM CLEANSED VALUE", "RT 01S FLOW RATE OUT CLEANSED VALUE"]].columns)
    train_features = np.array(train_set[["RT 01S VC WEIGHT ON BIT CLEANSED VALUE", "RT 01S SURFACE TORQUE CLEANSED VALUE",
                                         "RT 01S SURFACE RPM CLEANSED VALUE", "RT 01S FLOW RATE OUT CLEANSED VALUE"]])
    train_labels = np.array(train_set['RT 01S VC ON BOTTOM ROP'])
    test_features =  np.array(test_set[["RT 01S VC WEIGHT ON BIT CLEANSED VALUE", "RT 01S SURFACE TORQUE CLEANSED VALUE",
                                         "RT 01S SURFACE RPM CLEANSED VALUE", "RT 01S FLOW RATE OUT CLEANSED VALUE"]])
    test_labels = np.array(test_set['RT 01S VC ON BOTTOM ROP'])
    rf = RandomForestRegressor(n_estimators=100, random_state=42)  # tune n_estimators with hyperparameter optimization later
    rf.fit(train_features, train_labels)
    predictions = rf.predict(test_features)
    rms = sqrt(mean_squared_error(test_labels, predictions))





