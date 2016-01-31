#This script pulls appropriate influenza sequences from years 2005-2015 
#from ~/influenza_passaging_effects/tenyear_divided_fastas/
#and also makes a pooled fasta of all sequences
#Condition: Matched sample size groups of all passage types pulled from 2005-2015
#Passage history groups:
#Unpassaged
#Generic cell
#Monkey cell
#Egg Amniote
#All passage groups pooled together including unsortable sequences
#
#
#CDM 11/30/15

echo "starting..."

BASEDIR=~/influenza_passaging_effects
SOURCE=$BASEDIR/fastas/tenyear_passage_divided_fastas




###################### Random draw of each condition using size matched to the shortest fasta, outputs samp_
echo "Randomly drawing sequences"

python $BASEDIR/scripts/randomdraw.py $SOURCE/complete_unpassaged_all_20052015.fasta $SOURCE/complete_cell_all_20052015.fasta $SOURCE/complete_monkey_all_20052015.fasta $SOURCE/complete_egg_all_20052015.fasta $SOURCE/complete_pooled_all_20052015.fasta

