#!/usr/bin/env python

#This script will take blast output to and decide output the number of hits that fall within the range of the centromere and those that dont
import numpy as np   
import sys

infile = open(sys.argv[1], 'r')
#outfile = open(sys.argv[2], "w")


col1= []
rows = []

for line in infile:
    col1.append( line.split("\t")[0])
    rows.append(line)
queries = np.unique(col1).tolist()
#print queries


## subroutine comparing subject beginning sequence to a hit to the centromeric regions
def position_func():
    global nocent
    global cent
    nocent = 0
    cent = 0
    if col2 ==  "Chr01":
#        print "Chr01 hit"
#        print col3
        if position >=35000000 and position <=40000000:
#            print "centromere hit"
            cent += 1
        else: 
            nocent += 1
    if col2 ==  "Chr02":
#        print "Chr02 hit"
       if position >=34000000 and position <=39000000:
#            print "centromere hit"
            cent += 1
       else:
            nocent += 1
    if col2 ==  "Chr04":
#        print "Chr04 hit"
        if position >=22000000 and position <=28000000:
#            print "centromere hit"
            cent += 1
        else:
            nocent += 1
    if col2 ==  "Chr05":
#        print "Chr05 hit"
        if position >=24000000 and position <=32000000:
#             print "centromere hit"
             cent += 1
        else:
            nocent += 1
    if col2 ==  "Chr06":
#        print "Chr06 hit"
        if position >=24000000 and position <=27000000:
#            print "centromere hit"
            cent += 1
        else:
            nocent += 1
    if col2 ==  "Chr08":
#        print "Chr08 hit"
        if position >=23000000 and position <=28000000:
#            print "centromere hit"
            cent += 1
        else:
            nocent += 1
    if col2 ==  "Chr09":
#        print "Chr09 hit"
        if position >=30000000 and position <=37000000:
#            print "centromere hit"
            cent += 1
        else:
            nocent += 1
    if col2 ==  "Chr10":
#        print "Chr10 hit"
        if position >=30000000 and position <=35000000:
#            print "centromere hit"
            cent += 1
        else:
            nocent += 1
    if col2 ==  "Chr11":
#        print "Chr11 hit"
        if position >=320000000 and position <=39000000:
#            print "centromere hit"
            cent += 1
        else:
            nocent += 1




for entry in queries:
    centromeric = 0
    noncentromeric = 0
    for line in rows:
        col1 = line.split("\t")[0]
        col2 = line.split("\t")[1]
        col3 = line.split("\t")[2]
        position = int(col3)
        if col1 == entry:
#            print "match"
            position_func()  
            if cent == 1:
                centromeric += 1
            elif nocent == 1:
                noncentromeric += 1
    if centromeric > noncentromeric:
         print entry, "\t", centromeric, "\t", noncentromeric
    


#for  line in g:
#        w = " reads"
#        v = line + w 
#        u = nameExtract + "\t" + v + "\n"   
#        outfile.write(u)

#        x = '%'
#        z = str(enrichment) + x
#        y = nameExtract + "\t" + z + "\n"
#        outfile.write(y)
