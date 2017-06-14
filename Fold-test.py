#!/usr/bin/env python

###This script takes two fasta files that are in a jellyfish output fasta format.  This means tha the sequence IDs are the counts of each 30bp kmer in my fastq file.  This means that the only unique identifier is the sequence.
###The methodology is to essentially use two hashes, one for each file.  Make the keys the sequence and the values the fastaIDs(counts).  Get rid of the > symbol in the values(counts).  Change to numeric form.  If keys match, then print key + file1(value)/file2(value).

#Usage python <Fasta ctrl(denominator)> <Fasta file (numerator) > output

import sys
from collections import defaultdict

#blast output with seq to remove
f1 = open(sys.argv[1], 'r')
#Fasta file to remove names from
f2 = open(sys.argv[2], 'r')


IGG ={}
CH3 = {}

#IGG = defaultdict(list)
#CH3= defaultdict(list)
value =[]

i=0
for seq  in f1:
    if seq[0] == '>':
        name = seq[1:].rstrip("\n")
        

    else:
        nucseq = seq.rstrip("\n")
        i = 1
        IGG[nucseq] = name

i=0
for seq  in f2:
    if seq[0] == '>':
        name = seq[1:].rstrip("\n")

    else:
        nucseq = seq.rstrip("\n")
        
        i = 1
        CH3[nucseq] = name

for key,value in IGG.items():
    for key1, value1 in CH3.items():
        if key == key1: #IGG[key] == CH3[key1]:
       
            numerator = int(CH3.get(key1))      
            denominator = int(value)
        
            fold = float(numerator) / denominator *1.000
            print key	+ "\t" + str(fold) + "\t" + str(numerator) + "\t" + str(denominator) 
            #f3.write(final)


f1.close()
f2.close()

