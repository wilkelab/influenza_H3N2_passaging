"""
This script takes FASTA files of sequences and removes duplicates

Modified by CDM
"""
from Bio import SeqIO
import sys


def remove_dups(infile):
#This removes duplicate fasta records, ie duplicate in both id and sequence
    handle = open(infile, "rU")
    records_ids = []
    records = []
#    print handle
    for record in SeqIO.parse(handle, "fasta"):

        if record.id in records_ids:
            continue #duplicate, skip
        elif not all(v in ['A', 'C', 'T', 'G', 'a', 'c', 't', 'g'] for v in record.seq):
            continue
        else:
            records_ids.append(record.id)
            records.append(record)
    handle.close()
    output_handle = open(infile, "w")
    SeqIO.write(records, output_handle, 'fasta')
    output_handle.close()

if len(sys.argv) != 2:
    print "Please provide FASTA infile as a command-line argument"

else:
    remove_dups(sys.argv[1])
