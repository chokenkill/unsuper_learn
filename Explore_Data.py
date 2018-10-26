import pandas as pd
import seaborn as sns

path = "/Users/av/Documents/Drilling/unsuper_learn/"

# All Depth Converted Data
Alpha = pd.read_csv(path+"AlphaDepthConvertedData.csv")
Bravo = pd.read_csv(path+"BravoDepthConvertedData.csv")
Charlie = pd.read_csv(path+"CharlieDepthConvertedData.csv")
Delta = pd.read_csv(path+"DeltaDepthConvertedData.csv")
Foxtrot = pd.read_csv(path+"FoxtrotDepthConvertedData.csv")


Alpha_eql = Alpha.loc[(Alpha['RT 01S BIT DEPTH'] == Alpha['RT 01S HOLE DEPTH'])]  # Only want values where the bit is at bottom of hole
# I believe we want this bc according to paper, ROP only matters when bit at bottom of hole
# Not sure how necessary this is

Bravo_eql = Bravo.loc[(Bravo['RT 01S BIT DEPTH'] == Bravo['RT 01S HOLE DEPTH'])]
Charlie_eql = Charlie.loc[(Charlie['RT 01S BIT DEPTH'] == Charlie['RT 01S HOLE DEPTH'])]
Delta_eql = Delta.loc[(Delta['RT 01S BIT DEPTH'] == Delta['RT 01S HOLE DEPTH'])]
Foxtrot_eql = Foxtrot.loc[(Foxtrot['RT 01S BIT DEPTH'] == Foxtrot['RT 01S HOLE DEPTH'])]

print('Alpha\n')
print(Alpha[['RT 01S BIT DEPTH','RT 01S HOLE DEPTH', 'RT 01S VC ON BOTTOM ROP']].describe())
print('Alpha_eql')
print(Alpha_eql[['RT 01S BIT DEPTH','RT 01S HOLE DEPTH','RT 01S VC ON BOTTOM ROP']].describe())

print('\nBravo\n')
print(Bravo[['RT 01S BIT DEPTH','RT 01S HOLE DEPTH','RT 01S VC ON BOTTOM ROP']].describe())
print('Bravo_eql')
print(Bravo_eql[['RT 01S BIT DEPTH','RT 01S HOLE DEPTH','RT 01S VC ON BOTTOM ROP']].describe())

print('\nCharlie\n')
print(Charlie[['RT 01S BIT DEPTH','RT 01S HOLE DEPTH','RT 01S VC ON BOTTOM ROP']].describe())
print('Charlie_eql')
print(Charlie_eql[['RT 01S BIT DEPTH','RT 01S HOLE DEPTH','RT 01S VC ON BOTTOM ROP']].describe())

print('\nDelta\n')
print(Delta[['RT 01S BIT DEPTH','RT 01S HOLE DEPTH','RT 01S VC ON BOTTOM ROP']].describe())
print('Delta_eql')
print(Delta_eql[['RT 01S BIT DEPTH','RT 01S HOLE DEPTH','RT 01S VC ON BOTTOM ROP']].describe())

print('\nFoxtrot\n')
print(Foxtrot[['RT 01S BIT DEPTH','RT 01S HOLE DEPTH','RT 01S VC ON BOTTOM ROP']].describe())
print('Foxtrot_eql')
print(Foxtrot_eql[['RT 01S BIT DEPTH','RT 01S HOLE DEPTH','RT 01S VC ON BOTTOM ROP']].describe())

# Eliminates about 400 data points per well
# Doesn't seem to have a big impact on the mean ROP
# could be eliminating some outliers but I see very little change in std across wells

# Checking if any of these variables are highly correlated and can be removed from our feature set
# Commented out because it's slow and unnecessary after running this part once

# sns.set(font_scale=0.5)
# pp = sns.pairplot(Alpha_eql, vars=['RT 01S BIT DEPTH', 'RT 01S VC ON BOTTOM ROP', 'RT 01S VC WEIGHT ON BIT CLEANSED VALUE',
#                                    'RT 01S SURFACE TORQUE CLEANSED VALUE', 'RT 01S SURFACE RPM CLEANSED VALUE',
#                                    'RT 01S FLOW RATE OUT CLEANSED VALUE'], plot_kws={"s":2})
# pp.savefig("pairplot.png")

# There's no correlation between any of the variables


