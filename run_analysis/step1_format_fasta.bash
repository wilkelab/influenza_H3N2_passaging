##########################################
#This script takes a nucleotide fasta with the header format ">[passage_history]_|_[strain_id]" ex. "C1_|_A_KENTUCKY_01_2007" 
#It makes sequence headers consistent (parser1.py) and removes duplicate sequences (get_unique_records.py)
#It then builds a tree of the nonredundant and reformatted fasta
#	This tree must be manually checked for abnormal clades
#CDM 10/1/2015
##########################################

if [[ $# -eq 0 ]] ; then
    echo 'No argument supplied to step1_format_fasta.bash'
    echo 'Requires FASTA file'
    exit 1
fi



FASTAFILE=$1
BASEDIR=~/influenza_passaging_effects




echo "starting..."

if [[ $# -eq 0 ]] ; then
    echo "Please use a filename GISAID FASTA file as a command line argument"
    echo "This file should be stored in /input_data"
    echo "See README.txt for instructions on downloading and formatting FASTA"
    echo "exiting"
    exit 1
fi

echo "fasta file:"
echo $FASTAFILE


cd $BASEDIR/input_data/

echo "reformatting sequences IDs"
python $BASEDIR/scripts/formattingparser.py $FASTAFILE

echo "removing duplicates"
python $BASEDIR/scripts/get_unique_records.py formatted.fasta

echo "building tree"
FastTree -gtr -nt -nosupport formatted.fasta > $BASEDIR/trees/formatting_trees/formatted.tree

mv formatted.fasta $BASEDIR/fastas/formatting_fastas/



echo "all done"
echo "instructions:"
echo "open formatted.tree (stored in /trees/) using a tree visualization program such as FigTree"
echo "copy long branch clades as a single continuous string into a new file named ab.txt"
echo "these sequences will be removed from the analysis"
echo "Place ab.text in in the top level input_data folder"
echo "see README.txt"

