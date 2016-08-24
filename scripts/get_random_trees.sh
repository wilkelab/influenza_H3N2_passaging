
BASEDIR=$( pwd )


rm -rf $BASEDIR/trees/randomsamples20052015_trees
rm -rf $BASEDIR/fastas/randomsamples20052015_fastas

mkdir $BASEDIR/trees/randomsamples20052015_trees
mkdir $BASEDIR/fastas/randomsamples20052015_fastas

f=$BASEDIR/trees/allsequences20052015_trees/complete_pooled_all_20052015.tree
echo "formatting $f"
grep '(' $f > newick.tmp
sed -i 's/tree tree_1 = \[&R\]//g' newick.tmp
sed -i 's/ //g' newick.tmp
#    sed -i 's/[|]/_/g' $f.tmp
sed -i 's/^M$//g' newick.tmp
sed -i "s/'//g" newick.tmp
sed -i 's/    //g' newick.tmp
#    mv $f.tmp nucleotide.tree



#cat newick.tmp


python scripts/random_sample_trees.py newick.tmp /home/claire2/influenza_passaging_effects/fastas/allsequences20052015_fastas/complete_pooled_all_20052015.fasta pooled 2052015 917 200


mv *.fasta $BASEDIR/fastas/randomsamples20052015_fastas
mv *.tree $BASEDIR/trees/randomsamples20052015_trees

cp $BASEDIR/trees/monkeymatched20052015_trees/samp_unpassaged_917a_20052015.tree $BASEDIR/trees/randomsamples20052015_trees

cp $BASEDIR/fastas/monkeymatched20052015_fastas/samp_unpassaged_917a_20052015.fasta $BASEDIR/fastas/randomsamples20052015_fastas

rm newick.tmp
