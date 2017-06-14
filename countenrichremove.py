#!/usr/bin/env python

#This script will take a bowtie output file and count the most common part of the map that reads map to.  THen the script determines the genomic enrichment based on the number of reads mapped to each part of the map divided by the total number of reads in that have been aligned with bowtie.  If using paired end reads to map in bowtie, be sure to double the number of aligned reads for accuracy.

#python countenrichremove.py <bowtie count file> <output file> 
from collections import Counter
import sys

infile = open(sys.argv[1], 'r')

outfile = open(sys.argv[2], "w")

total = 0
for line in infile:
    col2 = line.split("\t")[1]
    total = total + int(col2)
#    print col2

infile.seek(0)

for line in infile:
    col2 = line.split("\t")[1]
    enrichment = 100 * (int(col2)/float(total))
    ochocinco =  line.rstrip() + "\t" + str(enrichment) + "\n"
    outfile.write(ochocinco)
    

