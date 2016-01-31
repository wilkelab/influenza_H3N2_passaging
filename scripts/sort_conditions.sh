#This script pulls appropriate influenza sequences according to experimental 
#conditions defined input file from condition_parameters
#from ~/influenza_passaging_effects/tenyear_divided_fastas/
#It concatenates files from each passage history into complete_x_20052014.fasta, 
#and also makes a pooled fasta of all sequences
#Condition: Every sequences from all passage types 2005-2014
#Required scripts:
#          randomdraw.py
#Required program:
#          FastTree compiled for short branch lengths (see README.txt)
#CDM 10/30/15

echo "starting..."

#CONDITION needs to have a matching parameters_CONDITION.sh file in /scripts
CONDITION=$1

#OPTION should be either "samp" or "comp"
#samp if doing a random draw of sequences
#complete if no random draw
OPTION=$2


BASEDIR=~/influenza_passaging_effects

rm -rf $BASEDIR/fastas/${CONDITION}_fastas
mkdir $BASEDIR/fastas/${CONDITION}_fastas

LOC=$BASEDIR/fastas/${CONDITION}_fastas
cd $LOC


#Condition parameters for choosing FASTA files and performing random draws if necessary

bash $BASEDIR/condition_parameters/parameters_${CONDITION}.sh $LOC

###################### an outgroup made up of sequences pre-1978 will be used for rooting
echo "adding in outgroup"


for f in ${OPTION}*.fasta
do
	

	cat $f $BASEDIR/fastas/formatting_fastas/outgroup.fasta > ${f/${OPTION}/outgroup}

done
#################### Make trees from the outgroup containing FASTAs

echo "begin making trees"


for h in outgroup_*.fasta
do 
      FastTree -gtr -nt -nosupport $h > ${h/fasta/tree}
      echo "$h"
done



#################### Sorting files into folders

rm -rf $BASEDIR/trees/${CONDITION}_trees/ 
mkdir $BASEDIR/trees/${CONDITION}_trees/

mv *tree $BASEDIR/trees/${CONDITION}_trees/
