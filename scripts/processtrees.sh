#This script cleans up both .tree files produced in FigTree and FASTA headers into a format 
#    that HYPHY SLAC can read and then starts the SLAC analysis.
#
#It:
#    Removes tree spaces, and extra text.
#    Removes pipe characters, ', space, and tabs
#    Starts SLACRun for each condition
#        SLACRun.sh
#        sortdata.sh
#Note: .tree base filenames must match exacly .fasta filenames 
#
#Written by CDM

if [[ $# -eq 0 ]] ; then
    echo 'No argument supplied to processtrees.sh!'
    echo 'exiting'
    exit 1
fi


BASEDIR=~/influenza_passaging_effects

FASTALOCATION=$1

LOC=$(pwd)
echo "starting process trees in:"
echo $LOC 

#tree format file created in figtree, either samp_* or complete_* prefixes.  It also tries to run HYPHY on the literal string samp*tree, not sure why, but it doesn't change anything. 
for f in {samp*tree,complete*tree}


do 
    #All of the formatting necessary to get the FASTA headers into format for HYPHY
    echo "formatting $f"
    grep '(' $f > $f.tmp
    sed -i 's/tree tree_1 = \[&R\]//g' $f.tmp
    sed -i 's/ //g' $f.tmp
    sed -i 's/[|]/_/g' $f.tmp
    sed -i "s/'//g" $f.tmp
    sed -i 's/    //g' $f.tmp
    mv $f.tmp nucleotide.tree

    CONDITION=${f%.*}
    echo $CONDITION
    sed 's/[|]/_/g' $FASTALOCATION/$CONDITION.fasta > nucleotide.fasta
    mv nucleotide.tree $BASEDIR/SLAC/
    mv nucleotide.fasta $BASEDIR/SLAC/
       
    bash $BASEDIR/scripts/SLACrun.sh $CONDITION

    cd $LOC 

done


cd $BASEDIR/rate_measurement_data/
python $BASEDIR/scripts/consolidate.py



