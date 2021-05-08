import numpy as np

nthreads = 64
min_E = 100
max_E = 250
step_E= 10
nevents= 100000

min_tw= 0.1
max_bw= 26
w_step= 0.1

f = open("cmds", "w")
i=0
for tw in np.arange(min_tw,max_bw+w_step,w_step):
    for bw in np.arange(tw, max_bw+w_step, w_step):
        for E in np.arange(min_E, max_E+step_E, step_E):
            f.write("./exampleB1 {} {} {} {} {}\n".format(nthreads,E,nevents,tw,bw))
            i=i+1
	
print("Total {} files combinations. Run source cmds".format(i))
