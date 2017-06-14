#!/usr/bin/env python
###This script should associate the names and values from two files.  Most likely, two blast output files.    

from collections import defaultdict
from collections import Counter
from operator import itemgetter
import sys
import re
###contig and region file with hit location, number of hits, and percentage of total hits in genome (6 total columns)
infile1 = open(sys.argv[1], 'r')

###blast out files with region in col1, ClusterContig in col2, and bitscore in col3
infile2 = open(sys.argv[2], 'r')

outfile = open(sys.argv[3], "w")

d1 = defaultdict(list) 
d2 = defaultdict(list)
d3 = defaultdict(list)
d4 = defaultdict(list)


###get the region/contig names, placing them in a dictionary
##### key = Chr12.7867897-787966 value = chr12:987987-98798798 chr12 87987-876976 chr01 559888 22 0.22 (whole line)
for line in infile1:
    key = line.split("\t")[0]
    value = line
    d1[key].append(value.rstrip())

###takes the blast.out file separates into columns,adds region name to region list, creates dictionary with regions as the keys.  The contig names are removed from the values so that they can be counted later, and then the clusters (values) are attached to the keys in list form
### 
region = []
for row in infile2:
    ### this is the region/contig -- a 6 column file
    reg1 = row.split("\t")[0]
    region.append(row.split("\t")[0])
    col2 = row.split("\t")[1]
    clusteruniq = re.sub("Contig.*", "",col2)
#    print row + "\t" + clusteruniq
    d2[reg1].append(clusteruniq)

###Counts the total number of the top 3 clusters for each region(per key in the d2 dictionary)    
for key, value in d2.items():
    z = Counter(value)
    for string, count in z.most_common(3):
        result = '%s %7d' % (string, count)        
        ### at this point result will display a count for each of the top 3 clusters for each key
        d3[key].append(result.rstrip())

###adding dictionary 3 values to an array
anarray = []

for key, value in d3.items():
    for entry in value:
         anarray.append(key + "\t" + entry)

###separating array values(d3 values) by tab
reconfiguredarray = []
prevname = 0

for line in anarray:
    name = line.split("\t")[0]
    cluster = line.split("\t")[1]
    ###separating the keys and values from d1 by a comma 
    for key, value in d1.items():
       if key == name:
           for entry in value:
               reconfiguredarray.append(entry + "," + cluster)
               ###initiating a the starting value for the next loop
               if prevname == 0:
                   prevname = entry    

### splits the new array be the previously inserted column, and then adds all three clusters(col1, d4.value) to each identical name (col2, d4.key).  Essentially this puts all of the cluster names and counts for each unique name(key) at the end of the name(key).
for line in reconfiguredarray:
    name = line.split(",")[0]
    cluster = line.split(",")[1]
#    print cluster
    ###iterates through all names that are identical to the name in prevname
    if name == prevname:
        d4[name].append(cluster)
        prevname = name
    ###this is needed to initiate another dictionary key for a new name
    else:
        prevname = name
        d4[name].append(cluster)

###This basically takes the d4 dictionary and prints it in a readable format
for key, value in d4.items():
    trim = str(value)[2:-2]
    nospaces = re.sub("      ", ": ", str(trim))
    noapos = re.sub("'", "", nospaces)
    final = re.sub(",", "\t", noapos)
    outfile.write( key + "\t" + final + "\n")
              

