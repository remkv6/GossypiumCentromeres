#!/usr/bin/perl
use strict;
use warnings;
#This script calculates the bp length from the last gene in the genome to plant telomeric sequences

my $i = 1; #why is this one and not zero?
my $totalstart = 0;
my $totalend = 0;
while (<>){ #this loop just adds 1 to $i for each iteration
#next if m/#/;
#print "start i", $i, "\n";
my @split = split /\t/;


#print $split[3], "\n";
#print $i, "\t", $total, "\n";
#	$totalstart += $split[3]; #adds every line at column 3
#	$totalend += $split[4]; #adds every line at column 4

		if ($i <= 3){
		$totalstart += $split[3]; #adds every line at column 3
#			print $totalstart, "\n";
				if ($i == 3){		
				print $totalstart/3, "\n";
				$totalstart = 0;
		    }
		
				}
		elsif ($i == 4..6){
			$totalend += $split[4];			
#			print $totalend, "\n";
			if($i == 6){	
			print $totalend/3, "\n";
			

			$totalend = 0;
			$i=0;
			   }
			
				 }

#print " mid i=" . $i, "\n";
$i++;
#print "end i=" . $i, "\n";
}

