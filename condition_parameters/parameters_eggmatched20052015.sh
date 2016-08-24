#This script pulls appropriate influenza sequences from years -2015 
#from ~/influenza_passaging_effects/tenyear_divided_fastas/
#and also makes a pooled fasta of all sequences
#Condition: Matched sample size groups of all passage types pulled from -2015
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
SOURCE=$BASEDIR/fastas/passage_and_year_divided_fastas




###################### Random draw of each condition using size matched to the shortest fasta, outputs samp_
echo "Randomly drawing sequences"

#python $BASEDIR/scripts/randomdraw.py $SOURCE/div_unpassaged_all_2015.fasta $SOURCE/div_cell_all_2015.fasta $SOURCE/div_monkey_all_2015.fasta $SOURCE/div_egg_all_2015.fasta $SOURCE/div_pooled_all_2015.fasta

python $BASEDIR/scripts/randomdraw.py 100 $SOURCE/div_unpassaged_all_2015.fasta $SOURCE/div_cell_all_2015.fasta $SOURCE/div_monkey_all_2015.fasta $SOURCE/div_egg_all_2015.fasta $SOURCE/div_pooled_all_2015.fasta







