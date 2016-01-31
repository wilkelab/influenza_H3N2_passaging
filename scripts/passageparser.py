"""
This script takes a FASTA file (formatted.fasta) of sequences which has been reformated with formattingparser.py 
It divides this FASTA by passage history into separate FASTAs

input FASTA header format:
>E1_C1|NEW_YORK_4_2010

outputs:
allyears_unpassaged.fasta
allyears_egg.fasta
allyears_cell.fasta
allyears_monkey.fasta
allyears_other.fasta
allyears_siat.fasta
allyears_nonsiat.fasta

Written by CDM 7/2015
"""


from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
import re
from sets import Set
import sys


def passage_parser(fasta_file):

    record_unpassaged = []
    unpassaged_dict = {}

    record_egg = []
    egg_dict = {}

    record_cell = []
    cell_dict = {}

    record_monk = []
    monk_dict = {}

    record_other=[]
    other_dict={}

    record_siat=[]
    siat_dict={}

    record_nonsiat=[]
    nonsiat_dict={}

    #Regex of passage history identifiers
    #As passage annotations are not standard, these will likely have to be slightly modifed/amended with any new dataset
    excludepattern = re.compile ("UNKNOWN_1_RHMK|TMK1_MDCK|AMNIOTIC_1_PRHMK_2|M1_RII1,C5|R1_C|R1_S|RII1_C|RII1_S|RIIX_C|RX_C|MDCK_1_RHMK|NC|_MK1")
    unpassagedpattern = re.compile("LUNG|P0|OR_|ORIGINAL|CLINICAL|DIRECT")
    eggpattern = re.compile("AM[1-9]|E[1-7]|AMNIOTIC|EGG|EX|AM_[1-9]")
    cellpattern = re.compile("S[1-9]|SX|SIAT|MDCK|C[1-9]|CX|C_[1-9]|M[1-9]|MX|X[1-9]|^X_$")
    siatpattern = re.compile("^S[1-9]_$|SIAT2_SIAT1|SIAT3_SIAT1")
    monkeypattern=re.compile("TMK|RMK|RHMK|RII|PMK|R[1-9]|RX")
    siatexcludepattern=re.compile("SIAT|SX|S[1-9]")

    count_total_sequences = 0

    #Make a document of every FASTA ID
    r = open("everyID.txt", "w")


    handle = open(fasta_file, "rU")

    for record in SeqIO.parse(handle, "fasta"):

        #Only want to search in passage history part of FASTA headers
        passage = record.id.split("|")[0]
  
        #Write a file of all FASTA headers
        r.write(record.id)
        r.write("\n")
        count_total_sequences = count_total_sequences + 1

        #Sort sequences by passage history


        #Do not want to use sequences which have been through multiple categories of serial passaging
        #I.e. both egg and monkey cell
        if excludepattern.search(passage):
  	   record_other.append(record.id)
           other_dict[record.id]=record.seq
	   continue
 
        elif eggpattern.search(passage):
            record_egg.append(record.id)
            egg_dict[record.id]=record.seq

        elif cellpattern.search(passage):
	    record_cell.append(record.id)
            cell_dict[record.id]=record.seq

            #Get MDCK-SIAT cell sequences 
	    if siatpattern.search(passage):
		record_siat.append(record.id)
		siat_dict[record.id]=record.seq
            #Get MDCK cell sequences that haven't been passaged through MDCK-SIAT
	    elif not siatexcludepattern.search(passage): 
		record_nonsiat.append(record.id)
		nonsiat_dict[record.id]=record.seq

        elif unpassagedpattern.search(passage):
	    record_unpassaged.append(record.id)
            unpassaged_dict[record.id]=record.seq

        elif monkeypattern.search(passage):
	    record_monk.append(record.id)
            monk_dict[record.id]=record.seq


        #Everything else
        else:
	    record_other.append(record.id)
            other_dict[record.id]=record.seq


    o = open("allyears_unpassaged.fasta", "w")
    e = open("allyears_egg.fasta", "w")
    c = open("allyears_cell.fasta", "w")
    m = open("allyears_monkey.fasta", "w")
    oth= open("allyears_other.fasta", "w")
    s = open("allyears_siat.fasta", "w")
    ns = open("allyears_nonsiat.fasta", "w")


    #Remove duplicates
    record_unpassaged=list(set(record_unpassaged))
    record_egg=list(set(record_egg))
    record_cell=list(set(record_cell))
    record_monk=list(set(record_monk))
    record_other=list(set(record_other))
    record_siat=list(set(record_siat))
    record_nonsiat=list(set(record_nonsiat))


    print "total sequences"
    print count_total_sequences
    print "unpassaged"
    print len(record_unpassaged)
    print "egg"
    print len(record_egg)
    print "monkey"
    print len(record_monk)
    print "cell"
    print len(record_cell)
    print "siat cell"
    print len(record_siat)
    print "nonsiat cell"
    print len(record_nonsiat)
    print "other"
    print len(record_other)


    for record in record_unpassaged:
        fastarecord= ">" + record
   	o.write("%s\n" % fastarecord)
   	o.write("%s\n" % unpassaged_dict[record])
  
    for record in record_egg:
   	fastarecord= ">" + record
   	e.write("%s\n" % fastarecord)
        e.write("%s\n" % egg_dict[record])

    for record in record_cell:
        fastarecord= ">" + record
        c.write("%s\n" % fastarecord)
        c.write("%s\n" % cell_dict[record])
         
    for record in record_monk:
    	fastarecord= ">" + record
    	m.write("%s\n" % fastarecord)
    	m.write("%s\n" % monk_dict[record])

    for record in record_other:
        fastarecord= ">" + record
        oth.write("%s\n" % fastarecord)
        oth.write("%s\n" % other_dict[record])
    for record in record_siat:
        fastarecord= ">" + record
        s.write("%s\n" % fastarecord)
        s.write("%s\n" % siat_dict[record])

    for record in record_nonsiat:
        fastarecord= ">" + record
        ns.write("%s\n" % fastarecord)
        ns.write("%s\n" % nonsiat_dict[record])


    o.close()
    e.close()
    c.close()
    m.close()
    r.close()
    oth.close()
    s.close()
    ns.close()
    handle.close()


if len(sys.argv) != 2:
    print "Please provide FASTA as infile as a command-line argument"
    print "FASTA head must be formatted as [passage]_|_[sequenceID]"
    print "Ex. >CX/C1_|_A/Arizona/09/2007"

else:
    passage_parser(sys.argv[1])




