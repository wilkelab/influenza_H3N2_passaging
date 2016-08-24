#This script pulls appropriate influenza sequences from years 2014 from ~/influenza_passaging_effects/passage_and_year_divided_fastas/
#It concatenates files from each passage history into div_x_20052015.fasta, and also makes a pooled fasta of all sequences
#Condtion: Matched samples of non-SIAT MDCK, MDCK-SIAT1, and unpassaged from 2014
#Passage history groups:
#unpassaged
#MDCK-SIAT1
#Non-SIAT1 cell culture
#
#CDM 10/30/15

LOC=$1
echo "starting..."

BASEDIR=~/influenza_passaging_effects

SOURCE=$BASEDIR/fastas/passage_and_year_divided_fastas

#Get sequences

cp $SOURCE/*2015.fasta $LOC
cp $SOURCE/*2014.fasta $LOC
cp $SOURCE/*2013.fasta $LOC
cp $SOURCE/*2012.fasta $LOC
cp $SOURCE/*2011.fasta $LOC
cp $SOURCE/*2010.fasta $LOC
cp $SOURCE/*2009.fasta $LOC
cp $SOURCE/*2008.fasta $LOC
cp $SOURCE/*2007.fasta $LOC
cp $SOURCE/*2006.fasta $LOC
cp $SOURCE/*2005.fasta $LOC

cd $LOC


rm *other*

cat *2015.fasta > div_pooled_all_2015.fasta
cat *2014.fasta > div_pooled_all_2014.fasta
cat *2013.fasta > div_pooled_all_2013.fasta
cat *2012.fasta > div_pooled_all_2012.fasta
cat *2011.fasta > div_pooled_all_2011.fasta
cat *2010.fasta > div_pooled_all_2010.fasta
cat *2009.fasta > div_pooled_all_2009.fasta
cat *2008.fasta > div_pooled_all_2008.fasta
cat *2007.fasta > div_pooled_all_2007.fasta
cat *2006.fasta > div_pooled_all_2006.fasta
cat *2005.fasta > div_pooled_all_2005.fasta
#

for g in div_pooled_all_*
do
   python $BASEDIR/scripts/get_unique_records.py $g

done

for f in div*
do
#   numseq=`grep -c ">" $f`
#   if [ "$numseq" -lt 100 ]; then
#      draw=$(($factor*$numseq))
#      draw=`echo '1 k $number
#   el
   draw=100
   echo "random draw"
   echo $f
   python $BASEDIR/scripts/randomdraw_manydraws.py $draw $f
 
done


rm *_all*




