"""
This script takes a raw FASTA and :
 	 Gets open reading frames
         Gets records with consistent sequence lengths for an 
                 influenza H3 without insertions or deletions
         Makes record ID consistent, i.e. all caps, and without special characters

Written by CDM 10/1/2015
"""
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
import sys
import re


#Get orf of an input nucleotide sequence
def orf(s):

    length = len(s)
    i = 0
    while i<length-2:
        tri = s[i:i+3]
        #Find the start codon
        if tri == "atg":            
            break
        i = i + 1
    j = i
    while j<length-2:
        tri = s[j:j+3]
        #Find the stop codon
        if tri == "tga" or tri == "taa" or tri == "tag":           
            break
        j = j + 3
        
    seq = Seq(s[i:j], generic_dna)
    #Handles if there is an ATG in the sequence before the real start codon
    seq = seq[-1698:]      
    return seq


#Replace any characters that aren't A-Z or 0-9 with an underscore
def record_strip(id):        
    record_strip = re.sub('[^A-Z0-9\|]', '_', id) 
    return record_strip

#Format FASTA entries and exclude sequences with insertions or deletions
def sort(infile):

    handle = open(infile, "rU")
    a = open("formatted.fasta", "w")

    for record in SeqIO.parse(handle, "fasta"):
        #print record  
        #Make all header characters uppercase
 	record.id = (record.id).upper() 
       	record_stripped = record_strip(record.id)
	record_orf = orf(str(record.seq))
	#Expected length of a hemagglutinin sequence w/o insertions or deletions
        #print record_orf, "\n"
	if len(record_orf)==1698 and record_orf.startswith('atg'):
            fastarecord= ">" + record_stripped
            a.write("%s\n" % fastarecord)
            a.write("%s\n" % record_orf)
        else:
            print "Sequence removed"
    a.close()
    handle.close()


if len(sys.argv) != 2:
    print "Please provide FASTA as infile as a command-line argument"
    print "FASTA head must be formatted as [passage]_|_[sequenceID]"
    print "Ex. >CX/C1_|_A/Arizona/09/2007"

else:
    sort(sys.argv[1])



