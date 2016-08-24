BASEDIR=$( pwd )


mkdir $BASEDIR/fastas/single_serial_fastas


echo "First get nonSIAT1 division"
python $BASEDIR/scripts/single_vs_serial_nonsiat2.py $BASEDIR/fastas/allsequences20052015_fastas/complete_nonsiat_all_20052015.fasta $BASEDIR/fastas/single_serial_fastas


echo "Count single vs serial"

python $BASEDIR/scripts/count_serial.py $BASEDIR/fastas/allsequences20052015_fastas/complete_pooled_all_20052015.fasta $BASEDIR/fastas/single_serial_fastas
#
cd $BASEDIR/fastas/single_serial_fastas


grep ">" complete_nonsiatsingle_all_20052015.fasta | sort -u > $BASEDIR/input_fasta_summary/nonsiatsingleIDs.txt 


grep ">" complete_nonsiatserialtwice.fasta |  sort -u > $BASEDIR/input_fasta_summary/nonsiatserialtwiceIDs.txt 

grep ">" complete_nonsiatserialmulti_all_20052015.fasta | sort -u > $BASEDIR/input_fasta_summary/nonsiatserialmultiIDs.txt 

grep ">" complete_single_all_20052015.fasta  | sort -u > $BASEDIR/input_fasta_summary/singlypassagedIDs.txt 


grep ">" complete_serial_all_20052015.fasta  | sort -u > $BASEDIR/input_fasta_summary/seriallypassagedIDs.txt 








