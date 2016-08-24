condition=$1
echo condition
echo $condition
outfile=${condition%.fasta}
outfile=${outfile#fastas/}
echo outfile
echo $outfile

./rank_sequences.py --aln $condition --outgroup outgroup --plot --destdir output/${outfile}_rankseq

#./rank_sequences.py --aln clairefastas/outgroup_${condition}.fasta --outgroup outgroup --plot --destdir ${condition}_rankseq

#./infer_fitness.py --aln $condition --outgroup outgroup --plot --destdir ${outfile}_inffit_def


#./infer_fitness.py --aln $condition --outgroup outgroup --gamma 3 --plot --destdir ${outfile}_inffit_gam3


#./infer_fitness.py --aln $condition --outgroup outgroup --collapse --plot --destdir ${outfile}_inffit_collapse


