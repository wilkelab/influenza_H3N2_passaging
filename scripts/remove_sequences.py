"""
This script takes a file of identifiers-to-remove, removes them from the original FASTA, and saves a FASTA of the sequences which were removed

python remove_sequences.py [identifiers_to_remove.txt] [fasta_to_remove_seqs_from] [name_for_new_fasta] [name_for_FASTA_of_removed_sequences]"

CDM 10/2/2015
"""


import sys
from Bio import Seq
from Bio import SeqIO
from Bio.Alphabet import generic_dna


def remove_sequences(to_remove, orig_fasta,trimmed_fasta, abnormal_fasta):


    # clade to remove
    rem= open(to_remove, "r")    
    # initial fasta
    orig = open(orig_fasta, "r") 

    # What new fasta will be called
    trim = open(trimmed_fasta, "w")

    # Place to store sequences which were removed
    rej = open(abnormal_fasta, "w")


    rejectstring = rem.read().replace("\n","")
    print rejectstring


    untrimmed = list(SeqIO.parse(orig, "fasta"))
    for record in untrimmed:
        if record.id in rejectstring:
	    rej.write(">" + str(record.id) + "\n")
            rej.write(str(record.seq) + "\n")

	else:
            trim.write(">" + str(record.id) + "\n")
            trim.write(str(record.seq) + "\n")

    rem.close()
    rej.close()
    orig.close()
    trim.close()


if len(sys.argv) != 5:
    print "Please provide infiles"
    print "Ex. python remove_sequences.py [identifiers_to_remove.txt] [fasta_to_remove_seqs_from] [name_for_new_fasta] [name_for_FASTA_of_removed_sequences]"

else:
    remove_sequences(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])

