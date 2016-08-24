#Input is a fasta file with outgroup added in




for condition in output/outgroup_*
do

    outfile=${condition%.fasta}
    outfile=${condition##*/}
    outfile=complete${condition##outgroup}_trunk
    echo $outfile

    #outfile=${outfile#fastas/}
    #python get_trunk.py --aln $condition --outgroup outgroup  --destdir output/${outfile}_trunkseqs 
    #python calc_dnds.py $condition/trunk_sequences.fasta -prot_outfile dnds.txt
    cp dnds_${condition%.fasta}.dat 

done
