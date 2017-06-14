#!/usr/bin/bash

#This is a collection of scripts and programs to take ChIP-seq data from reads to a bigwig file that can be analyzed on jbrowse
#this script should be run in the directory above your mira assembly
#bwa2Bigwig.sh <letter designation of genome fastq file> <letter designation of database> <location of genome fasta> <chromosome length file(tabular)>

NAME=$1
DBNAME=$2
BDBNAME=$3
CHRLEN=$4
###sickle under default parameters
#echo "trimming paired end reads with sickle"
#sickle pe -t sanger -f $NAME\.1.fastq -r $NAME\.2.fastq -o $NAME\_trim.1.fastq -p $NAME\_trim.2.fastq -s $NAME\_trim.singlets.fastq
#sickle pe -t sanger -f ../chip$NAME\IG/$NAME\IGChipAssembly_out.1.fastq -r ../chip$NAME\IG/$NAME\IGChipAssembly_out.2.fastq -o ../chip$NAME\IG/$NAME\IGChipAssembly_trim.1.fastq -p ../chip$NAME\IG/$NAME\IGChipAssembly_trim.2.fastq -s ../chip$NAME\IG/$NAME\IGChipAssembly_trim.singlets.fastq

###if your reads are single end use below
#echo "trimming single end reads with sickle"
module load sickle bwa samtools
#sickle se -t sanger -f $NAME\.fastq  -o $NAME\_trim.fastq
#head -n 4205096 $NAME\_trim.fastq > $NAME\.trunc_trim.fastq

## mapping the reads with 5 cores
echo "mapping reads"
#nice -n 18 bwa mem -t 10 -a  ~/centromererepeats/databases/$DBNAME\.fasta $NAME\.trunc_trim.fastq >$NAME\.$DBNAME\.sam
###delete this line later
nice -n 18 bwa mem -t 10 -a  ~/centromererepeats/databases/$DBNAME\.fasta $NAME\.fastq >$NAME\.$DBNAME\.sam
##converting to bam format
#echo "converting to bam"
#module load samtools
#samtools view -bT ~/centromererepeats/databases/$DBNAME\.fasta $NAME\.$DBNAME\.sam > $NAME\.$DBNAME\.bam
#samtools view -bq 1 $NAME\.$DBNAME\.bam >$NAME\.$DBNAME\.unique.bam
#samtools view -bq 1 $NAME\.$DBNAME\.bam >$NAME\.$DBNAME\.nonunique.bam
#macs2 calls the regions with significant enrichment
echo "running macs2"
##macs2 callpeak -t $NAME\.$DBNAME\.bam  -f AUTO -n $NAME --nomodel --keep-dup all &
#macs2 callpeak -B --SPMR -t $NAME\.$DBNAME\.bam  -c ../../newread.anal/D5/$NAME\.$DBNAME\.bam -f AUTO -n $NAME\broad --nomodel --broad --keep-dup all 
#wait

#echo "Sorting and extracting peak fasta sequences"
####this cat looks at the top 300 peaks, from either D, A, or AD
#cat  $NAME\_peaks.xls $NAME\broad_peaks.broadPeak | sort -k 8 -g -r |head -n 2000 >$NAME\peakssorted1.$DBNAME\.list


#to check if header is present, should see first ten lines starting with @
#head D1.sam 

#add the header, most likely needed every time, and convert to bam
echo "converting sam to bam format"
samtools view -bT -f $3 $NAME\.$DBNAME\.sam > $1\.bam

#sort the bam file
echo "sorting bam file"
samtools sort $NAME\.$DBNAME\.unique.bam $NAME\.$DBNAME\.sorted

#index, create .bai file -- our server does not support adding a different name.  use only below
echo "creating bam index"
samtools index $NAME\.$DBNAME\.sorted.bam

#convert to bedGraph --
echo "converting bam to bedGraph"
bedtools genomecov -bg -ibam $NAME\.$DBNAME\.sorted.bam -g $CHRLEN  > $NAME\.$DBNAME\.sorted.bedGraph

#sort by case, wasnt necessary last time...
LC_COLLATE=C sort -k1,1 -k2,2n $NAME\.$DBNAME\.sorted.bedGraph >$NAME\.$DBNAME\.resorted.bedGraph
#LC_COLLATE=C sort -k1,1 -k2,2n $NAME\broad_treat_pileup.bdg >$NAME\.$DBNAME\.resorted.bedGraph
echo "creating BigWig file, start getting excited!"
#convert to bigwig file
### bedgraphtobigwi <bedgraph file> <chromosome size file> <bigwig output name>
~/kentUtils/bin/bedGraphToBigWig $NAME\.$DBNAME\.resorted.bedGraph $CHRLEN  $NAME\.$DBNAME\.unique.bw





 

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

