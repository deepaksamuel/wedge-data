# search for files with the same wedge dimensions
#%%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os


data_dir = "../wedge-data-10000000" # the folder containing all the depth-dose data

f =[]
for file in os.listdir(data_dir):
    filename = os.fsdecode(file)
    f.append(filename)

print(f)
