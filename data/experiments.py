"""
README:IMPORTANT
The only lines that should be changed are those inside the loop in main.

Unless the input format changes, ONLY change the lines that call addto().

addto() takes a function to perform on the inputted data, some data, and
a name for the graph.

BE SURE to have a different name for each graph, or
the code will break.

SUGGESTIONS:(Not mandatory)
If you want to compute a value first before the addto() lines and
then pass it to addto(), just put that as the second parameter, and let
 the function be "lambda x:x"(without quotes).
"""

#BOILERPLATE CODE:Do NOT change unless you know what you're doing!
#BEGIN
import ast
import argparse
import numpy as np
import matplotlib.pyplot as plt
import json
import math
graphs=[]
usedgraphs=[]
names=[]
#END

#--------------------------------------------------------------------------------------------------------

#Also boilerplate stuff that can be reused
#BEGIN
def plotall(num_vars):
    for i, val in enumerate(graphs):
        if not (val in usedgraphs):
            maxval = max(val)
            newval = val
            plt.subplot()
            plt.title(names[i])
            bar_range = range(0, max(newval) + 1)
            plt.plot(bar_range, [newval.count(a) for a in range(max(newval) + 1)], color='green', marker='o')# ** (1./3) for a in range(max(newval))], color='green', marker='o')
            usedgraphs.append(newval)
            plt.show()

def addto(func, vals, name, filename):
    filename=filename.split("_num")[0]
    newname=name+":"+filename
    if not newname in names:    
        names.append(newname)
        graphs.append([])
        graphs[len(graphs)-1].append(func(vals))
    else:
        i=names.index(newname)
        graphs[i].append(func(vals))
#END

#----------------------------------------------------------------------------------------------------

def main(filename, num_vars):
    with open(filename, "r") as file:
        filel=json.load(file)
        for listform in filel:
            transposed=np.matrix(listform).T

            #Get only attractor sizes
            attractors=transposed[0].tolist()[0]
            #Get only basin sizes
            basins=transposed[1].tolist()[0]

            #Add more graphs here
            for i in basins:
                addto(lambda x:x, i, "Basin sizes", filename)

    #Plot the graphs here
    plotall(num_vars)

#---------------------------------------------------------------------------------------------------

#Run main
#BEGIN
if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Make a discrete dynamical system at random given the number of variables and canalyzing depth.')
    parser.add_argument('num', type= int)
    parser.add_argument('cores', type=int)
    parser.add_argument('num_vars', type= int)
    parser.add_argument('canalyzing_depth', type=int)
    args = parser.parse_args()
    main("num_vars="+str(args.num_vars)+"_depth="+str(args.canalyzing_depth)+".json", args.num_vars)
#END