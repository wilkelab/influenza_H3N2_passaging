import sys
from itertools import izip
from Bio import SeqIO

def hamming(seq1, seq2):
   assert len(seq1) == len(seq2)
   return sum(c1 !=c2 for c1, c2 in izip(seq1, seq2))




nextyear = sys.argv[1]
prevyear = sys.argv[2]
prevyearrank = sys.argv[3]
outfilename = sys.argv[4]
outfile = open(outfilename, "w")

record1_dict = SeqIO.to_dict(SeqIO.parse(nextyear, "fasta"))
record1 = record1_dict['1']
recseq1 = record1.seq

#handle2= open(prevyear, "rU")
record2_dict =  SeqIO.to_dict(SeqIO.parse(prevyear, "fasta"))


rankfile = open(prevyearrank, "r").readlines()
for line in rankfile[1:]:
    line2 = line.split("\t")
    rec2 = record2_dict[line2[0]]
    recseq2= rec2.seq
    ham = hamming(recseq1, recseq2)
   
    #print ham
    x = str(ham) + "\t" +  line 
    outfile.write(x)

outfile.close()
#unpassaged_249a_2014_rankseqrecord1_dict.close()
#rankfile.close().close()

