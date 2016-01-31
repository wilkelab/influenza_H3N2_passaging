#This script pulls appropriate influenza sequences from 2005-2015 from ~/influenza_passaging_effects/tenyear_divided_fastas/
#Condition: Matched samples of non-SIAT1 MDCK and unpassaged from 2005-2015
#Passage types:
#Unpassaged
#Non-SIAT1 cell culture
#Cell
#Pooled
#CDM 10/30/15


echo "starting..."

BASEDIR=~/influenza_passaging_effects
SOURCE=$BASEDIR/fastas/tenyear_passage_divided_fastas


###################### Random draw of each condition using size matched to the shortest fasta, outputs samp_
echo "Randomly drawing sequences"

python $BASEDIR/scripts/randomdraw.py $SOURCE/complete_unpassaged_all_20052015.fasta $SOURCE/complete_nonsiat_all_20052015.fasta $SOURCE/complete_pooled_all_20052015.fasta $SOURCE/complete_cell_all_20052015.fasta


