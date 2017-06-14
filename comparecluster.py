#!/usr/bin/env python

#This script takes two files with three columns (name "\t" anything "\t" integer) and associates the two files by column 1, and prints those liness in the first input <infile1> that have a larger column 3 than those in the second input file <infile2> to a new file.
#python <experimental file> <ctrl file> <output file>

from collections import defaultdict
import sys
import pprint
#experimental file
infile1 = open(sys.argv[1], 'r')

#ctrl file
infile2 = open(sys.argv[2], 'r')
outfile = open(sys.argv[3], "w")

array = []
d1 = defaultdict(list) 
d2 = defaultdict(list)
for line in infile1:
    array.append(line)
    key  = line.split("\t")[0]
    value = line.split("\t")[2]
    d1[key].append(value.rstrip())
for line in infile2:
    key  = line.split("\t")[0]
    value = line.split("\t")[2]
    d2[key].append(value.rstrip())

for key in d1:
    if key in d2:
         if d1[key] > d2[key]:
             print key, '\t', d1[key], d2[key]  
             for row in array:
                 name = line.split("\t")[0]
                 deadline = row +  str(d2[key])
                 if name == key:
                     outfile.write(deadline)

