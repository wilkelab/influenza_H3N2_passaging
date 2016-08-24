
#This script cleans up both .tree files produced in FigTree and FASTA headers into a format 
#    that HYPHY SLAC can read and then starts the SLAC analysis.
#
#It takes a condition as a command line arg
#Choice of conditions found in condition_parameters

#It:
#    Removes tree spaces, and extra text.
#    Removes pipe characters, apostrophes, space, and tabs
#    Starts SLACRun.sh for each condition
   
#Note: .tree base filenames must match exacly .fasta filenames, i.e. files in the FASTALOCATION folder and the tree folder must have the same base filename, except with appropriate .tree and .fasta endings 
#
#Written by CDM


if [[ $# -eq 0 ]] ; then
    echo 'No argument supplied to startSLAC.sh!'
    echo 'Please give a condition and either "samp" or "complete" as arguments'
    echo 'Ex. bash startSLAC.sh allsequences complete'
    echo 'Ex. bash startSLAC.sh matchedsample_nonsiatsiat samp'
    echo 'exiting'
    exit 1
fi

BASEDIR=~/influenza_passaging_effects


CONDITION=$1
CONDITIONTYPE=$2

TREELOCATION=~/influenza_passaging_effects/trees/${CONDITION}_trees
FASTALOCATION=~/influenza_passaging_effects/fastas/${CONDITION}_fastas

echo $TREELOCATION
cd $TREELOCATION
#tree format file created in figtree, either samp_* or complete_* prefixes.  It also tries to run HYPHY on the literal string samp*tree, not sure why, but it doesn't change anything. 



for f in ${CONDITIONTYPE}*tree


do


    #All of the formatting necessary to get the FASTA headers into format for HYPHY
    #Most cleaning only affect NEXUS format from FigTree, but pipes and apostrophes need to be removed from all newicks
    echo "formatting $f"
    grep '(' $f > $f.tmp
    sed -i 's/tree tree_1 = \[&R\]//g' $f.tmp
    sed -i 's/ //g' $f.tmp
    sed -i 's/[|]/_/g' $f.tmp
    sed -i "s/'//g" $f.tmp
    sed -i 's/    //g' $f.tmp
    mv $f.tmp nucleotide.tree

    BASEFILENAME=${f%.*}
    echo $BASEFILENAME
    sed 's/[|]/_/g' $FASTALOCATION/$BASEFILENAME.fasta > nucleotide.fasta
    mv nucleotide.tree $BASEDIR/SLAC/
    mv nucleotide.fasta $BASEDIR/SLAC/

    bash $BASEDIR/scripts/SLACrun.sh $BASEFILENAME
    cd $TREELOCATION
  
done


cd $BASEDIR/rate_measurement_data/
python $BASEDIR/scripts/consolidate.py


mv $BASEDIR/rate_measurement_data/slac_output.csv $BASEDIR/data_analysis/slac_output.csv

echo "rate measurements added to slac_output.csv"
































