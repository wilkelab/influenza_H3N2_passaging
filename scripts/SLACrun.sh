#This script sort a particular condition's nucleotide.fasta and nucleotide.tree files
#into the SLAC analysis file structure.
#
#For each phylogenetic subdivision, full/internal/tips, it starts SLAC(run_dNdS.bash)
#and removes the outputted sites.dat to condition_subdivision.dat
#
#Moves output to /rate_measurement_data
#CDM

if [[ $# -eq 0 ]] ; then
    echo 'No argument supplied to SLACrun.sh'
    exit 1
fi

CONDITION=$@

BASEDIR=~/influenza_passaging_effects
LOC=$BASEDIR/SLAC

cd $LOC


cp nucleotide.fasta $LOC/fulltree/
cp nucleotide.fasta $LOC/internals/
cp nucleotide.fasta $LOC/tips/

echo "copied nucleotide.fasta"

cp nucleotide.tree $LOC/fulltree/
cp nucleotide.tree $LOC/internals/
cp nucleotide.tree $LOC/tips/


echo "copied nucleotide.tree to slac/"
cd $LOC/fulltree/
echo $LOC

rm -f sites.dat
rm -f messages.log
rm -f errors.log
rm -f model.log
bash run_dNdS.bash

FILENAME=$CONDITION\_full.dat
mv sites.dat $BASEDIR/rate_measurement_data/$FILENAME
          
cd $LOC/internals/
rm -f sites.dat 
rm -f messages.log 
rm -f errors.log
rm -f model.log
bash run_dNdS.bash

FILENAME=$CONDITION\_internal.dat  
mv sites.dat $BASEDIR/rate_measurement_data/$FILENAME
    
cd $LOC/tips
rm -f sites.dat
rm -f messages.log
rm -f errors.log
rm -f model.log
bash run_dNdS.bash

FILENAME=$CONDITION\_tips.dat
echo $CONDITION
echo $FILENAME



mv sites.dat $BASEDIR/rate_measurement_data/$FILENAME

