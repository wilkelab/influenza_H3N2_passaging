"""

This script takes in a FASTA file of sequences with header format "PASSAGE_HISTORY_|_STRAIN_ID" and lists all passage IDs
Input format:
>E1_C1_|_NEW_YORK_4_2010
NNNNNNNNNNNNNN
>RHMK_|_MARYLAND_1_1992
NNNNNNNNNNNNNN

outputs:
E1_C1
RHMK

Written by CDM
"""


from Bio import SeqIO
import sys


def passage_list(fasta_file):

    infile = fasta_file
    handle = open(infile, "rU")
    rec=[]

    #Get just the passage history annotation
    for record in SeqIO.parse(handle, "fasta"):
        rec.append(record.id.split("|")[0])
    #Nonredundant list
    rec=list(set(rec))
    for r in rec:
        print str(infile) + "\t" +  r[:-1]



if len(sys.argv) != 2:
    print "Please provide FASTA as infile as a command-line argument"
    print "FASTA head must be formatted as [passage]_|_[sequenceID]"
    print "Ex. >CX/C1_|_A/Arizona/09/2007"

else:
    passage_list(sys.argv[1])


