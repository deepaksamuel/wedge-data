#%%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os




data_dir = "../data-single-wedge" # the folder containing all the depth-dose data
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
for file in os.listdir(data_dir):
    filename = os.fsdecode(file)
    if filename.endswith(".txt"): #or filename.endswith(".py"): 
        
        print(filename)
        energy =getEnergy(filename)
        dose_col_name = 'd-{}'.format(energy)
        colnames=['x', 'y', 'z', dose_col_name, 'd2','n']
        df = pd.read_csv("{}/{}".format(data_dir,filename),skiprows=3,header=0,names=colnames,usecols=['x','y',dose_col_name])   
        e.append(energy)
        if i>0:
            df_merged = pd.merge(df,df_merged,on=['x','y'])
        else:
            df_merged = df
        i=i+1

    else:
        continue
n_columns=len(df_merged.columns)-2
wepl =[]

for i in reversed(e):
    w =0
    for i in range (n_columns): 
        wepl.append




    


# df2=df_merged.iloc[:,2:] # remove the x, y columns
# cols = df2.columns
# e = []
# for n in cols:
#     e1 = n.split('-')
#     e.append(float(e1[1])) # get the energy from the column names

# df2 = df2.transpose()
# df2['energy'] = e

# #df2 contains energy in the last column and the dose at that energy
# # each column is for a specific x, y pixel in the order given in  


# # plotting one pixel erdf
# plt.scatter(df2['energy'],df2[17]) # plotting the 17th pixel
# plt.show()


# # plotting erdf of all rows having the same WEPL (along x)
# y_row = 26
# same_row_indices=np.arange(y_row,899,30) # all pixel with this indices will have the same wepl


# for i in same_row_indices:
#     plt.scatter(df2['energy'],df2[i])

# plt.show()


# #summing ERDF along constant zones
# pixel_value = 10  # between 0 and 29 this is proportional to the width of the wedge and therefore to WEPL
# df_const = df_merged[(df_merged.y == pixel_value)] # select only pixel where y=1
# df_sum =df_const.sum(axis = 0, skipna = True)
# e1 = df_sum.index # get index
# e2 =[]
# for n in e1:
#     if "-" in n:
#         e3 = n.split('-')
#         e2.append(float(e3[1])) # get the energy from the column names

# df_sum = df_sum[2:,]
# plt.scatter(e2,df_sum)




# # %%