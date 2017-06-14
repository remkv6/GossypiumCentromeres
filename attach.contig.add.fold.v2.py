#!/usr/bin/env python

#This script is taking three different input files and associating them based on name.
#Usage python <kmer file> <contig file> <blast output>
import sys

# This if the kmer file of a format:kmer number, kmer sequence, cenh3 hits, igg hits, fold enrichment
f1 = open(sys.argv[1], 'r')

#This file is a blast output file, but we are only interested in matching column1, so we can attach column2 to file 1.
f2 = open(sys.argv[2], 'r')

#Single line file, with fasta sequences and fasta names of the cap3 contigs 
f3 = open(sys.argv[3], 'r')


d1 = dict()
d2 = dict()
d3 = dict()
Contigattached = []
d4 = dict()

for line in f1:
	key = line.split("\t")[0]
	value = line.rstrip()
	d1[key] = value
	
for entry in f2:
	key = entry.split()[0].rstrip()
	value = entry
	d2[key] = value

for key,value in d1.iteritems():
		if key in d2.keys():
			Contigattached.append((d1[key]) + (d2[key]))

for row in f3:
	mod = row.split("\t")[0].strip(">")
	key = mod.rstrip()
	###this looks correct.  --> sequence \t >contigID
	value = row.rstrip()
	d3[key] = value
	#print value
	#print key

for row in Contigattached:
	key = row.split()[5]
	#print key
        
	value = row.rstrip()
	d4[key] = value
	#print (d4[key])
#for key, value in d4.iteritems():
	if key in d3.keys():
		print (d3[key]) + "\t" + (d4[key])


	


			

