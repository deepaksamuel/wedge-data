#%%
# merges all depth dose data into one single table
# first column: energy; rest of the columns: dose at the depths
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os


directory = "." # the folder containing all the depth-dose data
colnames=['x', 'y', 'z', 'd', 'd2','n']
colnames_merged=['Energy','Position','Dose']
e =[]
d =[]

df= pd.DataFrame()
df_merged = pd.DataFrame()
def getEnergy(fileName):
    e = fileName.split("-")
    return float(e[0])
i=0
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".txt"): #or filename.endswith(".py"): 
        
        print(filename)
        energy =getEnergy(filename)
        dose_col_name = 'd-{}'.format(energy)
        colnames=['x', 'y', 'z', dose_col_name, 'd2','n']
        df = pd.read_csv(filename,skiprows=3,header=0,names=colnames,usecols=['x','y',dose_col_name])   
        e.append(energy)
        if i>0:
            df_merged = pd.merge(df,df_merged,on=['x','y'])
        else:
            df_merged = df
        i=i+1

    else:
        continue


# the wepl is constant along x axis and changes along y; z is the beam direction
# select all pixels where y is constant
newdf = df_merged.loc[(df.y == 25)]
df = newdf.iloc[1,:]
plt.plot(df[2:])
plt.show()



# %%