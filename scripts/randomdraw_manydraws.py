"""

This script randomly draws groups from a set of FASTA files, matched to the number of sequences in the shortest FASTA file.
It makes three random samples in up to triplicate of the same size as the smallest group given as an argument 

Output:
    Ex. samp_150a_egg_19952015.fasta
    Sample a, of 150 egg sequences. 

With a numeric command line argument, it will make random draws of that size
With a list of FASTA files as command line arguments, it will make random draws that match the length of the shortest file.

requires:
    lengthdetermine.py
CDM 11/2/2015

"""

import lengthdetermine
import sys                                                              
from Bio import SeqIO
from Bio.Alphabet import generic_dna
import random

def random_draw_many():

    print sys.argv

    if sys.argv[1].isdigit():
        print "length provided"
        length = int(sys.argv[1])
        print sys.argv[1]
        print sys.argv[2]
        fastaname=sys.argv[2]
        fastalength = open(fastaname, "r").read().count(">")
        if fastalength < length:
            length = 0.7 * fastalength
            length = int(length)

    #else:
    #    print "length determined"
    #    args = sys.argv[1:]
    #    length = lengthdetermine.fastalength(args)



    print "the size of draws is: "
    print length

    #will just be one file
    for arg in sys.argv[2:]:
        print arg
        records = open(arg, "r").read().split(">")
        print records[-1]
        tmprecords = records
        #This deals with a whitespace that messes with the random sample
        for record in tmprecords:
	     if "atg" not in record:
                records.remove(record) 
        #Take up to three random draws      
        for i in range(0,50):
            #Don't need to take a sample if the length of the FASTA matches the sample size
            #if length + 1 == len(records):
            #    randrecords = records
               
            #else: 
            #Only take a sample if there are enough sequences left
            #try:
            randrecords = random.sample(records, length)
            #except ValueError:
            #print "out of sequences, no more draws from this condition"
            #break
            #Want draw without replacement, so remove sequences which have already
            #been drawn from records for subsequent draws
            #records = [record for record in records if record not in randrecords]
            

	    outfilename = "samp_"+arg.split("_")[-3]+"_"+str(length)+"x"+str(i)+"_" + arg.split("_")[-1]     
            print outfilename 
            outfile=open(outfilename, "w")
            print "final length"
            print len(randrecords)
            for record in randrecords:
                rec = ">" + record
                outfile.write(rec)


random_draw_many()

