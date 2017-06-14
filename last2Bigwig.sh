#!/usr/bin/bash

#This is a collection of scripts and programs to take ChIP-seq data from reads to a bigwig file that can be analyzed on jbrowse
#this script should be run in the directory above your mira assembly
#last2Bigwig.sh <letter designation of fastq> <letter designation of database> <location of genome fasta> <chromosome length file(tabular)>

###PERFORM THESE TASKS FIRST PART 1###
#Build database from WGS $2 would be the fasta sequence of the genome
#echo "building last database"
#mkdir ../$1\lastdb
#cd /home/remkv6/centromererepeats/$1\lastdb
#lastdb $1\db $3
#cd /home/remkv6/centromererepeats/chip$1
#prepare read files for gap analysis
#head -n 12000 $1\ChipAssembly_out.1.fastq >$1\head.1.fastq
#head -n 12000 $1\ChipAssembly_out.2.fastq >$1\head.2.fastq

#Check for mean read separation
#echo "estimating gap size"
#fastq-interleave $1\head.1.fastq $1\head.2.fastq | lastal -Q1 -i1 ../$2\lastdb/$2\db | last-pair-probs -e

#map reads to database using mean distance of read separation and standard deviation
#echo "enter mean gap length and standard deviation"
#read mean std

#map all the reads
#echo "mapping reads"
#fastq-interleave $1\ChipAssembly_out.1.fastq $1\ChipAssembly_out.2.fastq | lastal -Q1 -i1 ../$2\lastdb/$2\db | last-pair-probs -f $mean -s $std > $1\.maf

#convert to sam format
#echo "converting maf to sam format"
#maf-convert sam $1\.maf > $1\.sam

#to check if header is present, should see first ten lines starting with @
#head D1.sam 

#add the header, most likely needed every time, and convert to bam
#echo "converting sam to bam format"
#samtools view -bT $3 $1\.sam > $1\.bam

#sort the bam file
#echo "sorting bam file"
#samtools sort $1\.bam $1\.sorted

#index, create .bai file -- our server does not support adding a different name.  use only below
#echo "creating bam index"
#samtools index $1\.sorted.bam

#convert to bedGraph -- may need to be modified to include both strands in the data
#echo "converting bam to bedGraph"
#bedtools genomecov -bg -ibam $1\.sorted.bam -g $4 >$1\.sorted.bedGraph

#sort by case, wasnt necessary last time...
#LC_COLLATE=C sort -k1,1 -k2,2n $1\.sorted.bedGraph >$1\.resorted.bedGraph

echo "creating BigWig file, start getting excited!"
#convert to bigwig file
# bedgraphtobigwi <bedgraph file> <chromosome size file> <bigwig output name>
#source ~/myEnv/bin/activate
~/kentUtils/bin/bedGraphToBigWig $1\.resorted.bedGraph $4  $1\.bw





 

#rename contig to backbone to fulful mira requirements
#echo "renaming contigs"
#python ~/bin/renamer.py $name\ChipAssembly_out.unpadded.fasta.cap.contigs  $name\ChipAssembly_out.unpadded.cap.backbone.fasta
#python ~/bin/renamer.py $name\ChipAssembly_out.unpadded.fasta.cap.contigs.qual  $name\ChipAssembly_out.unpadded.cap.backbone.fasta.qual

#extract entries from mira assembly quality file to represent the singlet fasta entries without extra entries.  Not sure if this is necessary, but probably makes it faster
#echo "extracting entries from mira assembly quality file"
#python ~/bin/dup.remover.qual.py $name\ChipAssembly_out.unpadded.fasta.cap.singlets $2  $name\subtracted.fasta.qual

#combine the singlet.fasta file and the cap3 contig file
#echo "concatenating fasta files"
#cat $name\ChipAssembly_out.unpadded.cap.backbone.fasta $name\ChipAssembly_out.unpadded.fasta.cap.singlets > $name\reference.final.fasta
#cat $name\ChipAssembly_out.unpadded.cap.backbone.fasta.qual $name\subtracted.fasta.qual > $name\reference.final.fasta.qual

#nice -n 18 mira mappingmanifest.conf >&log.mapping

#contigstats=~/centromererepeats/chip$name/$name\ChipMapping_assembly/$name\ChipMapping_d_info/$name\ChipMapping_info_contigstats.txt
#echo "Finding Top40 most abundant contigs"
#python ~/bin/extract_reads_mira.py $contigstats Top40contigs

#echo "extracting fasta sequences"
#python ~/bin/Fasta.extractor.mira.py Top40contigs $name\reference.final.fasta  final.contigs.fasta

#echo "running splitfasta.pl"
#perl ~/bin/splitfasta.pl final.contigs.fasta out 1

#for loop just increments the variable i to name the files
#LIMIT=50
#echo "running perplot"
#for ((i=1; i <= LIMIT ; i++))
#do
#    eval perplot out.$i 30 100 A2T2 out.$i
#done

#echo "trimming perplot output"
#for ((nexti=1; nexti <= LIMIT ; nexti++))
#do    
#    tail -n 152 out.$nexti\.perplot > tail.out.$nexti\.perplot
#done

#echo "finding regions of significant periodicity in your input"
#python ~/bin/2Periodicity.py tail.out*[0-90-9].perplot

#echo "extracting fasta sequences"
#python ~/bin/filename2fasta.py 

#echo "cleaning up temporary files"
#rm \tail*
#rm out*

