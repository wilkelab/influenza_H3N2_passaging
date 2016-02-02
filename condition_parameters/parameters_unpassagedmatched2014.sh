#This script pulls appropriate influenza sequences from years 2014 from ~/influenza_passaging_effects/passage_and_year_divided_fastas/
#It concatenates files from each passage history into complete_x_20052015.fasta, and also makes a pooled fasta of all sequences
#Condtion: Matched samples of non-SIAT MDCK, MDCK-SIAT1, and unpassaged from 2014
#Passage history groups:
#unpassaged
#MDCK-SIAT1
#Non-SIAT1 cell culture
#
#CDM 10/30/15

echo "starting..."

BASEDIR=~/influenza_passaging_effects
SOURCE=$BASEDIR/fastas/passage_and_year_divided_fastas


###################### Random draw of each condition using size matched to the shortest fasta, outputs samp_
echo "Randomly drawing sequences"


python $BASEDIR/scripts/randomdraw.py $SOURCE/div_siat_all_2014.fasta $SOURCE/div_nonsiat_all_2014.fasta $SOURCE/div_unpassaged_all_2014.fasta


