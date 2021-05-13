# search for files with the same wedge dimensions
#%%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os


data_dir = "../wedge-data-10000000" # the folder containing all the depth-dose data

files =[]
f =[]
for file in os.listdir(data_dir):
    filename = os.fsdecode(file)
    str = filename.split("EVTS-")
    files.append("{}/{}".format(data_dir,filename))
    f.append(str[1])

unique_dims = np.unique(f)

# now unique_dims has the list unique wedge dimensions in the data dir
# Now search for files having this extension 

wedge_files =[]
for ff in files:
    if unique_dims[1] in ff:
        wedge_files.append(ff)


def getEnergy(fileName):
    e = fileName.split("-")
    return float(e[0])

i=0
for file in wedge_files:
        energy =getEnergy(filename)
        dose_col_name = 'd-{}'.format(energy)
        colnames=['x', 'y', 'z', dose_col_name, 'd2','n']
        df = pd.read_csv("{}/{}".format(data_dir,filename),skiprows=2,header=0,names=colnames,usecols=['x','y',dose_col_name])   
        e.append(energy)
        if i>0:

            df_merged = pd.merge(df,df_merged,on=['x','y'])
        else:
            df_merged = df
        i=i+1

    else:
        continue