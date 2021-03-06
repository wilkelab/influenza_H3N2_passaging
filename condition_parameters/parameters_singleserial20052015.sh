#This script pulls appropriate influenza sequences from 2005-2015 from ~/influenza_passaging_effects/tenyear_divided_fastas/
#Condition: Matched samples of non-SIAT1 MDCK and unpassaged from 2005-2015
#Passage types:
#Non-SIAT1 cell culture
#Passaged singly and multiply
#CDM 10/30/15


echo "starting..."

BASEDIR=~/influenza_passaging_effects
SOURCE=$BASEDIR/fastas/single_serial_fastas

cp $BASEDIR/fastas/allsequences20052015_fastas/complete_unpassaged_all_20052015.fasta $SOURCE 


###################### Random draw of each condition using size matched to the shortest fasta, outputs samp_
echo "Randomly drawing sequences"

python $BASEDIR/scripts/randomdraw.py $SOURCE/complete_nonsiatmulti_all_20052015.fasta $SOURCE/complete_nonsiatdouble_all_20052015.fasta $SOURCE/complete_nonsiatsingle_all_20052015.fasta $SOURCE/complete_unpassaged_all_20052015.fasta 



