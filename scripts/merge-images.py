#%%

import numpy as np
import matplotlib.pyplot as pyplot
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image as im




def get_widths(file):
    s=file.split("-")
    return float(s[4]), float(s[6])

def get_map(tw, bw, lenx=3, leny=3):
    img =[]
    slope = (bw-tw)/2.9
    for x in range(0,30):
        for y in range(0,30):
            img.append(tw + slope*y/10)
    return np.reshape(img, (30, 30))

#%%
fname = "../data/100.000000-MEV-100000-EVTS-0.300000-TW-2.200000-BW.txt"
data = pd.read_csv(fname,skiprows=3,names=["x","y","z","dose","dose2","counts"],header=None)
arr1=np.array(data["dose"])
arr2 = np.reshape(arr1, (30, 30))
plt.plot(arr1)
plt.show()
# plt.imshow(arr2)
# plt.colorbar()
# plt.show()
# tw,bw=get_widths(fname)

# m=get_map(tw,bw)
# plt.imshow(m)
# plt.colorbar()



#print(arr1[14],arr2[0,14])
#plt.plot(data["dose"])
#plt.hist(arr1,bins=100)
#plt.imshow(arr2)
#img = im.fromarray(arr2)
#img = img.convert('L')
#img.save('gfg_dummy_pic.png')
# %%

