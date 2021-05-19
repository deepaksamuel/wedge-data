import numpy as np

nthreads = 64
nevents= 1000000

#energy parameters
min_E = 100
max_E = 250
step_E= 10

#
tw = 0.1 # cm
bw= 25 # cm


f = open("../single-wedge-cmds", "w")
i=0

for E in np.arange(min_E, max_E+step_E, step_E):
    f.write("./exampleB1 {} {} {} {} {}\n".format(nthreads,E,nevents,tw,bw))
    i=i+1
	
print("Total {} files combinations. Run 'source single-wedge-cmds'".format(i))
