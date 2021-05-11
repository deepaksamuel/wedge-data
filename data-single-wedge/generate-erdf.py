#%%
# merges all depth dose data into one single table
# first column: energy; rest of the columns: dose at the depths
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os


directory = "." # the folder containing all the depth-dose data
colnames=['X', 'Y', 'Z', 'Total Dose', 'Total2','Entries']
colnames_merged=['Energy','Position','Dose']
d =[]


def getEnergy(fileName):
    e = fileName.split("-")
    return float(e[0])

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".txt"): #or filename.endswith(".py"): 
        #print(os.path.join(directory, filename))
        print(filename)
        #df = pd.read_csv(os.path.join(directory, filename),skiprows=3,header=0,names=colnames)   
        df = pd.read_csv(filename,skiprows=3,header=0,names=colnames)   
        energy =getEnergy(filename)
        for i in range(0,299):
            d.append([energy,df['Z'][i],df['Total Dose'][i]])
        #plt.plot(df['Z'],df['Total Dose'])
        
        continue
    else:
        continue
df_merged = pd.DataFrame(d,columns=colnames_merged)
plt.plot(df_merged['Energy'],df_merged['Dose'])
#


# %%