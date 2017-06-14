
#!/usr/bin/env python

#This script takes the periodicity plot output from perplot and extracts the significant periods from the list, if any exist  

#Usage python <periodicity file> 

import sys
import re
import os.path
import fileinput


#file input (perplot output)
f1 = fileinput.input()
#output file
 
f2 = open("significant_periods.txt", "a")


thresh1 = 2.98 #99 percentile
thresh2 = 2.52 #95 percentile
regex = '[-+]?[0-9]+(?:\.[0-9]+)?(?:[eE][-+]?[0-9]+)?' # matching any floating point number
for line in f1:
#     print line
     col1 = line.split()[1]
     col0 = line.split()[0]
#     print fileinput.filename()
     removenewline = line.strip()
#     print col1
     if re.match(regex, col0):
          highp = 11.50
          lowp = 9.50
          period = float(col0)
#          print "Filtering by period length"
          if period >= lowp and period <= highp:
#               print "Filtering by significance"
               if re.match(regex, col1):
#                   print line
                    integer = float(col1)
                    if integer >= thresh1:
                         f2.write('%r\t%r\t%r\t%r\n' % (fileinput.filename() , col0, col1, "99th percentile"))
                    elif integer >= thresh2 and integer < thresh1:
                         f2.write('%r\t%r\t%r\t%r\n' % (fileinput.filename(), col0, col1, "95th percentile"))
     

f1.close()
f2.close()

