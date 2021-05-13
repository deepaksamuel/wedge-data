# search for files with the same wedge dimensions and plot the ERDF
#%%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os


data_dir = "../data-single-wedge" # the folder containing all the depth-dose data
colnames=['x', 'y', 'z', 'd', 'd2','n']
colnames_merged=['Energy','Position','Dose']
e =[]
files =[]
f =[]
for file in os.listdir(data_dir):
    if "-EVTS-" in file:
        filename = os.fsdecode(file)
        str = filename.split("EVTS-")
        files.append("{}/{}".format(data_dir,filename))
        print(filename)
        f.append(str[1])


print(f)
unique_dims = np.unique(f)

# now unique_dims has the list unique wedge dimensions in the data dir
# Now search for files having this extension 

wedge_files =[]

for ff in files:
    if unique_dims[0] in ff:
        wedge_files.append(ff)
# wedge files contain all files with the same wedge dimension
print(wedge_files)
def getEnergy(fileName):
    s=fileName.split("/")
    str = s[len(s)-1]
    e = fileName.split("-")
    # print(e)
    return float(e[0])

i=0
e=[]
for file in wedge_files:
        energy =getEnergy(filename)
        print(file)
        dose_col_name = 'd-{}'.format(energy)
        colnames=['x', 'y', 'z', dose_col_name, 'd2','n']
        df = pd.read_csv("{}/{}".format(data_dir,filename),skiprows=2,header=0,names=colnames,usecols=['x','y',dose_col_name])   
        e.append(energy)
        if i>0:

            df_merged = pd.merge(df,df_merged,on=['x','y'])
        else:
            df_merged = df
        i=i+1

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
    