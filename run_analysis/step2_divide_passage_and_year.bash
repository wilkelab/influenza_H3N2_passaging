##############################################
#Requires files: trimmedsequences.fasta (created by step2)
#Requires program: FastTree
#         FastTree must be the double-precision version, compiled with the following line
#         $ gcc -DUSE_DOUBLE -O3 -finline-functions -funroll-loops -Wall -o FastTree FastTree.c -lm
#         See http://meta.microbesonline.org/fasttree/   
#Requires scripts: passageparser.py
#                  align_and_translate.py -> only needed for formatting a new structure for painting
#                  timesort.py
#                  getpassage.py
#                  getidentifiers.py
#                  get_unique_records.py
#                  remove_sequences.py 
#
#Outputs fastas divided by year and passage history to top level passage_and_year_divided_fastas/
#Outputs fasta divided only by passage history to top level passage_divided_fastas/
##############################################

BASEDIR=~/influenza_passaging_effects
LOC=$BASEDIR/fastas/formatting_fastas
SOURCE=$BASEDIR/fastas/passage_and_year_divided_fastas
DEST=$BASEDIR/input_fasta_summary

cd $LOC

if [ -f $BASEDIR/input_data/ab.txt ]; then
	
	python $BASEDIR/scripts/remove_sequences.py $BASEDIR/input_data/ab.txt formatted.fasta trimmed.fasta abnormal_clade.fasta


# remove ab.txt sequences from main FASTA  
	echo "Removing sequences from ab.txt"
else

	echo "No file of sequences to be removed was provided"
	echo "No sequences were removed"
	cp formatted.fasta trimmed.fasta

fi

######################### Make a protein alignment for optional step of making a structure map
#Also, useful as a check for gapped sequences
python $BASEDIR/scripts/align_and_translate.py trimmed.fasta 

#########################

######################### passageparser.py splits an input list of sequences with record ids formatted PassageHistory_|_Place_number_date
python $BASEDIR/scripts/passageparser.py trimmed.fasta

mv everyID.txt $DEST/

######################## Get a count of sequences by passage type over time. timesort.py divides fastas by year (output as div_ files

rm -f $LOC/unsortable.fasta
rm -f $LOC/outgroup.fasta
rm -f $LOC/unusedyears.fasta
rm -f $DEST/timeseries_all.txt
rm -f $DEST/timeseries_yearly.txt
rm -f $DEST/timeseries_20052015.txt
rm -f $DEST/passageIDs_all.txt
rm -f $DEST/passageIDs_yearly.txt
rm -f $DEST/passageIDs_20052015.txt
rm -f $DEST/identifiers_all.txt
rm -f $DEST/identifiers_yearly.txt
rm -f $DEST/identifiers_20052015.txt

echo -e "file\tcount" >> $DEST/timeseries_all.txt
echo -e "file\tidentifier" >> $DEST/identifiers_all.txt
echo -e "file\tpassage" >> $DEST/passageIDs_all.txt

for f in allyears_*
do

	python $BASEDIR/scripts/timesort.py $f  #outputs div
	echo -n $f" " >> $DEST/timeseries_all.txt
	grep -c ">" $f >> $DEST/timeseries_all.txt

	python $BASEDIR/scripts/getpassage.py $f >>  $DEST/passageIDs_all.txt	

#	echo $f >>  $DEST/identifiers_all.txt
	python $BASEDIR/scripts/getidentifiers.py $f >> $DEST/identifiers_all.txt	

done


##################### Get rid of redundancy in outgroup.fasta, unusedyears.fasta
python $BASEDIR/scripts/get_unique_records.py $LOC/outgroup.fasta
python $BASEDIR/scripts/get_unique_records.py $LOC/unusedyears.fasta


########################

echo -e "file\tcount" >>  $DEST/timeseries_yearly.txt
echo -e "file\tidentifier" >> $DEST/identifiers_yearly.txt
echo -e "file\tpassage" >> $DEST/passageIDs_yearly.txt


for g in div_*
do
	echo -n $g" " >>  $DEST/timeseries_yearly.txt
	grep -c ">" $g >>  $DEST/timeseries_yearly.txt

	python $BASEDIR/scripts/getpassage.py $g >>  $DEST/passageIDs_yearly.txt	

#	echo -n $g >>  $DEST/identifiers_yearly.txt
	python $BASEDIR/scripts/getidentifiers.py $g >>  $DEST/identifiers_yearly.txt	

done

#################### Sorting files into folders

mv div_* $BASEDIR/fastas/passage_and_year_divided_fastas/
mv allyears_* $BASEDIR/fastas/passage_divided_fastas/
########################


###################### files are concatenated together to get groups of several passage types

cd $BASEDIR/fastas/tenyear_passage_divided_fastas/
cat $SOURCE/div_cell*200[56789].fasta $SOURCE/div_cell*201[012345].fasta > complete_cell_all_20052015.fasta
cat $SOURCE/div_unpassaged*200[56789].fasta $SOURCE/div_unpassaged*201[012345].fasta > complete_unpassaged_all_20052015.fasta
cat $SOURCE/div_egg*200[56789].fasta $SOURCE/div_egg*201[012345].fasta > complete_egg_all_20052015.fasta
cat $SOURCE/div_monkey*200[56789].fasta $SOURCE/div_monkey*201[012345].fasta > complete_monkey_all_20052015.fasta
cat $SOURCE/div_other*200[56789].fasta $SOURCE/div_other*201[012345].fasta > complete_other_all_20052015.fasta
cat $SOURCE/div_siat*200[56789].fasta $SOURCE/div_siat*201[012345].fasta > complete_siat_all_20052015.fasta
cat $SOURCE/div_nonsiat*200[56789].fasta $SOURCE/div_nonsiat*201[012345].fasta > complete_nonsiat_all_20052015.fasta



echo "combining files into pooled group of all passage types"

cat complete_unpassaged_all_20052015.fasta complete_cell_all_20052015.fasta > complete_unpassagedcell_all_20052015.fasta
cat complete_unpassagedcell_all_20052015.fasta complete_other_all_20052015.fasta > complete_unpassagedcellother_all_20052015.fasta
cat complete_unpassagedcellother_all_20052015.fasta complete_egg_all_20052015.fasta > complete_unpassagedcelleggother_all_20052015.fasta
cat complete_unpassagedcelleggother_all_20052015.fasta complete_monkey_all_20052015.fasta > complete_pooled_all_20052015.fasta

cat complete_unpassaged_all_20052015.fasta complete_siat_all_20052015.fasta > complete_unpassagedsiat_all_20052015.fasta


rm complete_unpassagedcell_all_20052015.fasta
rm complete_unpassagedcellother_all_20052015.fasta
rm complete_unpassagedcelleggother_all_20052015.fasta

echo -e "file\tcount" >>  $DEST/timeseries_20052015.txt
echo -e "file\tidentifier" >> $DEST/identifiers_20052015.txt
echo -e "file\tpassage" >> $DEST/passageIDs_20052015.txt


for g in complete_*
do
	echo -n $g" " >>  $DEST/timeseries_20052015.txt
	grep -c ">" $g >>  $DEST/timeseries_20052015.txt

	python $BASEDIR/scripts/getpassage.py $g >>  $DEST/passageIDs_20052015.txt	

#	echo -n $g >>  $DEST/identifiers_yearly.txt
	python $BASEDIR/scripts/getidentifiers.py $g >>  $DEST/identifiers_20052015.txt	

done






