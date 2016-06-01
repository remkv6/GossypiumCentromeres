#!/usr/bin/env python

#This script will take blast output to and decide output the number of hits that fall within the range of the centromere and those that dont
import numpy as np   
import sys
from collections import Counter
import pandas as pd
from collections import defaultdict
infile = open(sys.argv[1], 'r')
#outfile = open(sys.argv[2], "w")



defined = []

for line in infile:
    col1 = line.split("\t")[0]
    col2 = line.split("\t")[1]
    col3 = line.split("\t")[8]
    position = int(col3)
    positionA = 0
    positionB = 1000000
    
    if col2 ==  "Chr01" or col2 == "Chr1":
        while not position <= positionA and position >= positionB:
            positionA += 1000000            
            positionB += 1000000
        defined.append(col1 + "\t " + col2 + "\t" + str(positionA))
    if col2 ==  "Chr02" or col2 == "Chr2":
        while not position <= positionA and position >= positionB:
            positionA += 1000000
            positionB += 1000000
        defined.append(col1 + "\t " + col2 + "\t" + str(positionA))
    if col2 ==  "Chr03" or col2 == "Chr3":
        while not position <= positionA and position >= positionB:
            positionA += 1000000
            positionB += 1000000
        defined.append(col1 + "\t" + col2 + "\t" + str(positionA)) 
    if col2 ==  "Chr04" or col2 == "Chr4":
        while not position <= positionA and position >= positionB:
            positionA += 1000000
            positionB += 1000000
        defined.append( col1 + "\t" + col2 + "\t" + str(positionA))
    if col2 ==  "Chr05" or col2 == "Chr5":
        while not position <= positionA and position >= positionB:
            positionA += 1000000
            positionB += 1000000
        defined.append(col1 + "\t" + col2 + "\t " + str(positionA))
    if col2 ==  "Chr06" or col2 == "Chr6":
        while not position <= positionA and position >= positionB:
            positionA += 1000000
            positionB += 1000000
        defined.append(col1 + "\t" + col2 + "\t" + str(positionA))
    if col2 ==  "Chr07" or col2 == "Chr7":
        while not position <= positionA and position >= positionB:
            positionA += 1000000
            positionB += 1000000
        defined.append(col1 + "\t" + col2 + "\t" + str(positionA))
    if col2 ==  "Chr08" or col2 == "Chr8":
        while not position <= positionA and position >= positionB:
            positionA += 1000000
            positionB += 1000000
        defined.append(col1 + "\t" + col2 + "\t" + str(positionA))
    if col2 ==  "Chr09" or col2 == "Chr9":
        while not position <= positionA and position >= positionB:
            positionA += 1000000
            positionB += 1000000
        defined.append(col1 + "\t" + col2 + "\t" + str(positionA))
    if col2 ==  "Chr10":
        while not position <= positionA and position >= positionB:
            positionA += 1000000
            positionB += 1000000
        defined.append(col1 + "\t" + col2 + "\t" + str(positionA))
    if col2 ==  "Chr11":
        while not position <= positionA and position >= positionB:
            positionA += 1000000
            positionB += 1000000
        defined.append(col1 + "\t" + col2 + "\t" + str(positionA))
    if col2 ==  "Chr12":
        while not position <= positionA and position >= positionB:
            positionA += 1000000
            positionB += 1000000
        defined.append(col1  + "\t" + col2 + "\t" + str(positionA))
    if col2 ==  "Chr13":
        while not position <= positionA and position >= positionB:
            positionA += 1000000
            positionB += 1000000
        defined.append(col1 + "\t" + col2 + "\t" + str(positionA))

counter = defaultdict(int)
##counts the number of blast hits in each bin
for row in defined:
    counter[row] += 1
##converts dictionary to list
sums = []
for key in counter:
    combine = key + "\t" + str(counter[key])
    sums.append(combine)
    
prevent = []
for entry in sums:
    zap = entry.split("\t")[0]
#    print entry
    prevent.append(zap)
unique = set(prevent)
#print unique


### associates total number of blast hits for each query to the query name
recount = []
for entry in unique:
    total = 0
    for row in sums:
        col1 = row.split("\t")[0]
        col4 = row.split("\t")[3]
        
        if col1 == entry:
            total = total + int(col4)
    recount.append(entry + "\t" + str(total))
#    print recount
##prints list of top hits if greater than .25% of blast hits fall into one bin
for row in recount:
    column1 = row.split("\t")[0]
    column2 = row.split("\t")[1]
    for line in sums:
       indivcol1 = line.split("\t")[0] 
       indivcol4 = line.split("\t")[3]
#       print indivcol4
       if column1 == indivcol1:
           percent = float(indivcol4)/float(column2)
#           print indivcol1 + str(percent)
           if percent >= .002:
               if int(indivcol4) > 9:   
                   print line + "\t" + str(percent)



#for row in sums:
#    eeeee row
#    col1 = row.split("\t")[0]
#    col4 = row.split("\t")[3]
#    total = 0
#    print col4 
#    for entry in queries:
#       print entry
#       if col1 == entry:
#          total += int(col4)
#       print entry + str(total)


#        col3 = row.split("\t")[2]
#        col4 = row.split(",")[1]
#        print col1





#test = Counter(defined)
#print test
#for row in Counter(defined):
#    print row
#    col1 = row.split("\t")[0]
#    col2 = row.split("\t")[1]
#    col3 = row.split("\t")[2]
    #col4 = row.split(":")[1]
#    queries = np.unique(col1).tolist()
#    print col4 
