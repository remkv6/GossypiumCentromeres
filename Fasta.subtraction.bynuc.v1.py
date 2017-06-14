#!/usr/bin/env python

#This script takes blast output in the form of qseqid "\t" qseq, and extracts fasta sequences that match nucleotides.

#This will only work if the fasta file has all of the sequence on one line
#Usage python <blast output> <fasta file> <output file>

import sys
from collections import defaultdict

#blast output with seq to remove
f1 = open(sys.argv[1], 'r')
#Fasta file to remove names from
f2 = open(sys.argv[2], 'r')
#write to this file
f3 = open(sys.argv[3], 'w')

d = defaultdict(list)
d2 = defaultdict(list)
value =[]



for line in f1:
    key = line.split()[0]
    value = line.split()[1]
    d[key] = value
print d

i = 0
nucseq = 0
for seq  in f2:
   if seq[0] == '>':
        key = seq
   else:
        value = seq
        d2[key] = value
        i = 1

for (key, value) in set(d.items()) & set(d2.items()):
    if d[value] == d2[value]:
        test =0
    else:
        #f3.write(final)
        name =d2.items([key])
        seq = str(d2[value])
        print str(name) 
f1.close()
f2.close()
f3.close()

