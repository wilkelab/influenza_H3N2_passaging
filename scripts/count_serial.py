"""
This script takes a FASTA file (formatted.fasta) of sequences which has been reformated with formattingparser.py 
It divides this FASTA by passage history into separate FASTAs

input FASTA header format:
>E1_C1|NEW_YORK_4_2010

outputs:
allyears_nonsiat_single.fasta
allyears_nonsiat_serial.fasta
Written by CDM 7/2015
"""


from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
import re
from sets import Set
import sys


def passage_parser(fasta_file, outfileloc):



    #Regex of passage history identifiers
    #As passage annotations are not standard, these will likely have to be slightly modifed/amended with any new dataset
    #excludepattern = re.compile ("UNKNOWN_1_RHMK|TMK1_MDCK|AMNIOTIC_1_PRHMK_2|M1_RII1,C5|R1_C|R1_S|RII1_C|RII1_S|RIIX_C|RX_C|MDCK_1_RHMK|NC|_MK1")
    excludepattern = re.compile("XMDCK|EGG|ORIGINAL|LUNG|NO_PASSAGE|^P0|OR|DAY|X_$|DEE_5|^X_$|DETAILS__ND|DETAILS_MDCK")
    serialpattern = re.compile("2|3|4|5|6|1_C|X_|X_C|AND_MV1|X_S|1_S|CX|MX|C1S1|EX|X_E|MIX_RHMK|RII")
  
#    unpassagedpattern = re.compile("LUNG|P0|OR_|ORIGINAL|CLINICAL|DIRECT")
#    eggpattern = re.compile("AM[1-9]|E[1-7]|AMNIOTIC|EGG|EX|AM_[1-9]")
#    cellpattern = re.compile("S[1-9]|SX|SIAT|MDCK|C[1-9]|CX|C_[1-9]|M[1-9]|MX|X[1-9]|^X_$")
#    siatpattern = re.compile("^S[1-9]_$|SIAT2_SIAT1|SIAT3_SIAT1")
#    monkeypattern=re.compile("TMK|RMK|RHMK|RII|PMK|R[1-9]|RX")
#    siatexcludepattern=re.compile("SIAT|SX|S[1-9]")



    record_serial=[]
    serial_dict={}

    record_single=[]
    single_dict={}


    handle = open(fasta_file, "rU")

    for record in SeqIO.parse(handle, "fasta"):

        #Only want to search in passage history part of FASTA headers
        passage = record.id.split("|")[0]
  
        #Write a file of all FASTA headers
        #r.write(record.id)
        #r.write("\n")
        #count_total_sequences = count_total_sequences + 1

        #Sort sequences by passage history


        #Do not want to use sequences which have been through multiple categories of serial passaging
        #I.e. both egg and monkey cell
        if passage == "_":
            print "no passage info"
            continue
        elif excludepattern.search(passage):
            print passage
            continue


        elif serialpattern.search(passage):
            record_serial.append(record.id)
            serial_dict[record.id]=record.seq

        else:
            record_single.append(record.id)
            single_dict[record.id]=record.seq

    si_outfile = outfileloc + "/complete_single_all_20052015.fasta"
    se_outfile = outfileloc + "/complete_serial_all_20052015.fasta"

    print si_outfile, se_outfile
    si = open(si_outfile, "w")
    se = open(se_outfile, "w")


    #Remove duplicates
    record_single=list(set(record_single))
    record_serial=list(set(record_serial))

    print "single passage"
    print len(record_single)
    print "serial passage"
    print len(record_serial)


    for record in record_single:
        fastarecord= ">" + record
   	si.write("%s\n" % fastarecord)
   	si.write("%s\n" % single_dict[record])
  
    for record in record_serial:
   	fastarecord= ">" + record
   	se.write("%s\n" % fastarecord)
        se.write("%s\n" % serial_dict[record])
    si.close()
    se.close()
    handle.close()


if len(sys.argv) != 3:
    print "Please provide FASTA as infile as a command-line argument"
    print "FASTA head must be formatted as [passage]_|_[sequenceID]"
    print "Ex. >CX/C1_|_A/Arizona/09/2007"
    print "Second argument is location to put outfiles"
 
else:
    passage_parser(sys.argv[1], sys.argv[2])




