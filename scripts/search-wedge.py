# search for files with the same wedge dimensions and plot the ERDF 
# in image format using a formula (see code below)
#%%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os


data_dir = "../wedge-data-10000000" # the folder containing all the depth-dose data
dim_indx = 1 # use this to go to another dimension file



colnames=['x', 'y', 'z', 'd', 'd2','n']
colnames_merged=['Energy','Position','Dose']
e =[]
full_file_names =[] # full file_name
file_name_suffix =[] # list of suffixes - to retrieve dimensions
#240.0-MEV-1000000-EVTS-0.1-TW-0.1-BW.txt

for file in os.listdir(data_dir):
    if "-EVTS-" in file:
        filename = os.fsdecode(file)
        str = filename.split("EVTS-")
        full_file_names.append("{}/{}".format(data_dir,filename))
        #print(filename)
        file_name_suffix.append(str[1])


unique_dims = np.unique(file_name_suffix)

# now unique_dims has the list of unique wedge dimensions in the data dir

same_dim_files =[] # files having the same dimensions
print(unique_dims[dim_indx])
for ff in full_file_names:
    #print(ff)
    if unique_dims[dim_indx] in ff:
        same_dim_files.append(ff)

def getEnergy(fileName):
    s=fileName.split("/")
    str = s[len(s)-1]
    e = fileName.split("-")
    # print(e)
    return float(e[0])

i=0
e=[]
for file in same_dim_files:
        energy =getEnergy(filename)
        print(file)
        dose_col_name = 'd-{}'.format(energy)
        colnames=['x', 'y', 'z', dose_col_name, 'd2','n']
        df = pd.read_csv("{}/{}".format(data_dir,filename),skiprows=2,header=0,names=colnames,usecols=['x','y',dose_col_name])   
        e.append(energy) # store the energy of this file in a list
        if i>0:
            df_merged = pd.merge(df,df_merged,on=['x','y']) # keep x,y columns commn
        else:
            df_merged = df
        i=i+1

#df_merged contains the dose measured at all the energies for the same dimensions
n_columns=len(df_merged.columns)-2
n_rows = len(df_merged.index)
wepl =[]


e = e[::-1] # this reverses the list - if this is not done the column ordering does not match with this list ordering


erdf=[]
for r in range(n_rows):
    sw=0
    sd=0
    for c in range (n_columns): 
        sw+=df_merged.iloc[r,c+2]*e[c]
        sd+=df_merged.iloc[r,c+2]
    erdf.append(sw/sd)    

df_merged['erdf'] = erdf

erdf_image = np.reshape(erdf, (30, 30))


plt.imshow(erdf_image, cmap='hot')
plt.colorbar()
plt.show()
