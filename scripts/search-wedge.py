# search for files with the same wedge dimensions and plot the ERDF 
# in image format using a formula (see code below)
#%%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from PIL import Image

print(pd.__version__)
data_dir = "../wedge-data-1000000-2cm" # the folder containing all the depth-dose data
#dim_indx = 7 # use this to go to another dimension file


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
ii=0
for dims in unique_dims:
    same_dim_files =[] # files having the same dimensions
    #print(unique_dims[dim_indx])
    for ff in full_file_names:
        #print(ff)
        if dims in ff:
            same_dim_files.append(ff)

    def getEnergy(fileName):
        s=fileName.split("-MEV-")
        if "/" in s[0]:
            e = s[0].split("/")
            return float(e[len(e)-1])
        else:
            return float(s[0])
        

    i=0
    e=[]
    for file in same_dim_files:
            #print(file)
            energy =getEnergy(file)
            dose_col_name = 'd-{}'.format(energy)
            colnames=['x', 'y', 'z', dose_col_name, 'd2','n']
            df = pd.read_csv("{}/{}".format(data_dir,file),skiprows=2,header=0,names=colnames,usecols=['x','y',dose_col_name])   
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
        erdf.append(sw/sd)    # formula for ERDF: Sig EiDi/Sig Di

    df_merged['erdf'] = erdf
    df_merged.to_excel("{}.xlsx".format(dims))

    # verification formula
    # =$D$1*D2+$E$1*E2+$F$1*F2+$G$1*G2+$H$1*H2+$I$1*I2+$J$1*J2+$K$1*K2+$L$1*L2+$M$1*M2+$N$1*N2+$O$1*O2+$P$1*P2 + $Q$1*Q2 +$R$1*R2 + $S$1*S2

    print("Wedge image for {}".format(dims))
    erdf_image = np.reshape(erdf, (20, 20))
    plt.imshow(erdf_image, cmap='hot')
    plt.colorbar()
    plt.show()
    # im = Image.fromarray(np.reshape(erdf, (20, 20)))
    # im.save("out.jpeg")
    plt.imsave("{}.png".format(dims), erdf_image)
    ii =ii+1
    png_data=plt.imread("{}.png".format(dims))
    print(png_data)
    if(ii==1):
        break
#%%



