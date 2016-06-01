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
    
    if col2 ==  "A01" or col2 == "Chr1" or col2== "At_chr1":
        while not position <= positionA and position >= positionB:
            positionA += 1000000            
            positionB += 1000000
        defined.append(col1 + "\t " + col2 + "\t" + str(positionA))
    if col2 ==  "A02" or col2 == "Chr2" or col2== "At_chr2" :
        while not position <= positionA and position >= positionB:
            positionA += 1000000
            positionB += 1000000
        defined.append(col1 + "\t " + col2 + "\t" + str(positionA))
    if col2 ==  "A03" or col2 == "Chr3" or col2== "At_chr3":
        while not position <= positionA and position >= positionB:
            positionA += 1000000
            positionB += 1000000
        defined.append(col1 + "\t" + col2 + "\t" + str(positionA)) 
    if col2 ==  "A04" or col2 == "Chr4" or col2== "At_chr4":
        while not position <= positionA and position >= positionB:
            positionA += 1000000
            positionB += 1000000
        defined.append( col1 + "\t" + col2 + "\t" + str(positionA))
    if col2 ==  "A05" or col2 == "Chr5"  or col2== "At_chr5":
        while not position <= positionA and position >= positionB:
            positionA += 1000000
            positionB += 1000000
        defined.append(col1 + "\t" + col2 + "\t " + str(positionA))
    if col2 ==  "A06" or col2 == "Chr6"  or col2== "At_chr6":
        while not position <= positionA and position >= positionB:
            positionA += 1000000
            positionB += 1000000
        defined.append(col1 + "\t" + col2 + "\t" + str(positionA))
    if col2 ==  "A07" or col2 == "Chr7" or col2== "At_chr7":
        while not position <= positionA and position >= positionB:
            positionA += 1000000
            positionB += 1000000
        defined.append(col1 + "\t" + col2 + "\t" + str(positionA))
    if col2 ==  "A08" or col2 == "Chr8" or col2== "At_chr8":
        while not position <= positionA and position >= positionB:
            positionA += 1000000
            positionB += 1000000
        defined.append(col1 + "\t" + col2 + "\t" + str(positionA))
    if col2 ==  "A09" or col2 == "Chr9" or col2== "At_chr9":
        while not position <= positionA and position >= positionB:
            positionA += 1000000
            positionB += 1000000
        defined.append(col1 + "\t" + col2 + "\t" + str(positionA))
    if col2 ==  "A10" or col2 == "At_chr10":
        while not position <= positionA and position >= positionB:
            positionA += 1000000
            positionB += 1000000
        defined.append(col1 + "\t" + col2 + "\t" + str(positionA))
    if col2 ==  "A11" or col2== "At_chr11":
        while not position <= positionA and position >= positionB:
            positionA += 1000000
            positionB += 1000000
        defined.append(col1 + "\t" + col2 + "\t" + str(positionA))
    if col2 ==  "A12" or col2== "At_chr12":
        while not position <= positionA and position >= positionB:
            positionA += 1000000
            positionB += 1000000
        defined.append(col1  + "\t" + col2 + "\t" + str(positionA))
    if col2 ==  "A13" or col2== "At_chr13":
        while not position <= positionA and position >= positionB:
            positionA += 1000000
            positionB += 1000000
        defined.append(col1 + "\t" + col2 + "\t" + str(positionA))
    if col2== "Dt_chr1" or col2 ==  "D01":
        while not position <= positionA and position >= positionB:
            positionA += 1000000
            positionB += 1000000
        defined.append(col1 + "\t " + col2 + "\t" + str(positionA))
    if col2== "Dt_chr2" or col2 ==  "D02":
        while not position <= positionA and position >= positionB:
            positionA += 1000000
            positionB += 1000000
        defined.append(col1 + "\t " + col2 + "\t" + str(positionA))
    if col2== "Dt_chr3" or col2 ==  "D03":
        while not position <= positionA and position >= positionB:
            positionA += 1000000
            positionB += 1000000
        defined.append(col1 + "\t" + col2 + "\t" + str(positionA))
    if col2== "Dt_chr4" or col2 ==  "D04":
        while not position <= positionA and position >= positionB:
            positionA += 1000000
            positionB += 1000000
        defined.append( col1 + "\t" + col2 + "\t" + str(positionA))
    if  col2 == "Dt_chr5"or col2 ==  "D05":
        while not position <= positionA and position >= positionB:
            positionA += 1000000
            positionB += 1000000
        defined.append(col1 + "\t" + col2 + "\t " + str(positionA))
    if col2== "Dt_chr6"or col2 ==  "D06":
        while not position <= positionA and position >= positionB:
            positionA += 1000000
            positionB += 1000000
        defined.append(col1 + "\t" + col2 + "\t" + str(positionA))
    if col2 == "Dt_chr7" or col2 ==  "D07":
        while not position <= positionA and position >= positionB:
            positionA += 1000000
            positionB += 1000000
        defined.append(col1 + "\t" + col2 + "\t" + str(positionA))
    if col2 == "Dt_chr8" or col2 ==  "D08":
        while not position <= positionA and position >= positionB:
            positionA += 1000000
            positionB += 1000000
        defined.append(col1 + "\t" + col2 + "\t" + str(positionA))
    if col2 == "Dt_chr9" or col2 ==  "D09":
        while not position <= positionA and position >= positionB:
            positionA += 1000000
            positionB += 1000000
        defined.append(col1 + "\t" + col2 + "\t" + str(positionA))
    if col2 == "Dt_chr10" or col2 ==  "D10":
        while not position <= positionA and position >= positionB:
            positionA += 1000000
            positionB += 1000000
        defined.append(col1 + "\t" + col2 + "\t" + str(positionA))
    if col2== "Dt_chr11" or col2 ==  "D11":
        while not position <= positionA and position >= positionB:
            positionA += 1000000
            positionB += 1000000
        defined.append(col1 + "\t" + col2 + "\t" + str(positionA))
    if col2 == "Dt_chr12" or col2 ==  "D12":
        while not position <= positionA and position >= positionB:
            positionA += 1000000
            positionB += 1000000
        defined.append(col1  + "\t" + col2 + "\t" + str(positionA))
    if col2== "Dt_chr13" or col2 ==  "D13":
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
##prints list of top hits if greater than 25% of blast hits fall into one bin
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
