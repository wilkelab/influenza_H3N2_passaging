#This script pulls appropriate influenza sequences from years 2005-2015 from ~/influenza_passaging_effects/tenyear_divided_fastas/
#It also makes a pooled fasta of all sequences
#Condition: All sequences for each passage history group available from 2005-2015
#Passage groups:
#Unpassaged
#Generic cell
#Monkey cell
#Egg Amniote
#non-SIAT1 Cell
#SIAT1 MDCK
#Pooled group of Unpassaged, generic cell, monkey cell, and egg amniote
#Pooled group of MDCK-SIAT1, unpassaged
#CDM 11/30/15

LOC=$1
echo "starting..."

BASEDIR=~/influenza_passaging_effects

SOURCE=$BASEDIR/fastas/tenyear_passage_divided_fastas

#Get sequences
cp $SOURCE/*.fasta $LOC

