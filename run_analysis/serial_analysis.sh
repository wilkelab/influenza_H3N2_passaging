BASEDIR=$( pwd )


mkdir $BASEDIR/fastas/single_serial_fastas


echo "First get nonSIAT1 division"
python $BASEDIR/scripts/single_vs_serial_nonsiat.py $BASEDIR/fastas/allsequences20052015_fastas/complete_nonsiat_all_20052015.fasta $BASEDIR/fastas/single_serial_fastas


echo "Count single vs serial"

python $BASEDIR/scripts/count_serial.py $BASEDIR/fastas/allsequences20052015_fastas/complete_pooled_all_20052015.fasta $BASEDIR/fastas/single_serial_fastas

cd $BASEDIR/fastas/single_serial_fastas


grep ">" allyears_nonsiatserial.fasta | awk -F'|' '{print $1}' | sort -u > $BASEDIR/input_fasta_summary/nonsiatserialIDs.txt 

grep ">" allyears_nonsiatsingle.fasta | awk -F'|' '{print $1}' | sort -u > $BASEDIR/input_fasta_summary/nonsiatsingleIDs.txt 

grep ">" allyears_serial.fasta | awk -F'|' '{print $1}' | sort -u > $BASEDIR/input_fasta_summary/allserialIDs.txt 
grep ">" allyears_single.fasta | awk -F'|' '{print $1}' | sort -u > $BASEDIR/input_fasta_summary/allsingleIDs.txt 










