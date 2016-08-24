#Input is a fasta file with outgroup added in



for condition in fastas/outgroup_*
do

    outfile=${condition%.fasta}
    outfile=${outfile#fastas/}
    python scripts/get_trunk.py --aln $condition --outgroup outgroup  --destdir output/${outfile}_trunkseqs 

done
