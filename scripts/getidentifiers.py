"""
This script takes FASTA files of sequences and lists all record IDs
Input format:
>E1_C1|NEW_YORK_4_2010
NNNNNNNNNNNNNN
>RHMK|MARYLAND_1_1992
NNNNNNNNNNNNNN

outputs:
E1_C1|NEW_YORK_4_2010
RHMK|MARYLAND_1_1992
Written by CDM
"""
from Bio import SeqIO
import sys


def rec_list(fasta_file):
    infile = fasta_file
    handle = open(infile, "rU")
    rec=[]
    for record in SeqIO.parse(handle, "fasta"):
        rec.append(record.id)

    #Nonredundant list
    recset=set(rec)
    for rec in list(recset):
        print str(infile) + "\t" +rec


if len(sys.argv) != 2:
    print "Please provide FASTA as infile as a command-line argument"
    print "FASTA head must be formatted as [passage]_|_[sequenceID]"
    print "Ex. >CX/C1_|_A/Arizona/09/2007"

else:
    rec_list(sys.argv[1])




