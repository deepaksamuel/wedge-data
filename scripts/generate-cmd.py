import numpy as np

nthreads = 64
min_E = 100
max_E = 250
step_E= 10
nevents= 10000000

min_tw= 0.1
max_bw= 15
w_step= 0.1


f = open("cmds", "w")
i=0
for tw in np.arange(min_tw,max_bw+w_step,w_step):
    for bw in np.arange(tw, max_bw+w_step, w_step):
        for E in np.arange(min_E, max_E+step_E, step_E):
            f.write("echo '{}) Generating for E:{} MeV top-width:{:.2g} cm bottom-width:{:.2g} cm Events:{}'\n".format(i,E,tw,bw,nevents))
            f.write("./exampleB1 {} {} {} {:.2g} {:.2g}\n".format(nthreads,E,nevents,tw,bw))
            i=i+1
            f.write("mv *-BW.txt wedge-data-10000000\n") #this folder must preexist!!!
 	
print("Total {} files combinations. Run source cmds".format(i))