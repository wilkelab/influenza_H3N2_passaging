"""
This script takes the allyears_[passage].fasta files created by passageparser.py, and divides them by year
It also creates an outgroup of sequences from 1968-1977
Input FASTA header format:
>E1_C1|NEW_YORK_4_2010

Outputs:
div_[passage]_all_[year].fasta, for years = 2005-2015 to fastas/passage_and_year_divided_fastas
outgroup.fasta to fastas/formatting_fastas/

CDM 9/2015
"""


from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
import sys


def time_sort(infile):
    
    filename="div_" + str(infile.split("_")[1])
    filename=filename.split(".")[0]

    filename1 = filename + "_all_2014" +".fasta"
    filename2 = filename + "_all_2013"+".fasta"
    filename3 = filename + "_all_2012" +".fasta"
    filename4 = filename + "_all_2011" +".fasta"
    filename5 = filename + "_all_2010" +".fasta"
    filename6 = filename + "_all_2009" +".fasta"
    filename7 = filename + "_all_2008"+".fasta"
    filename8 = filename + "_all_2007" +".fasta"
    filename9 = filename + "_all_2006" +".fasta"
    filename10 = filename + "_all_2005" +".fasta"
    filename11 = filename + "_all_2004" +".fasta"
    filename12 = filename + "_all_2003" +".fasta"
    filename13 = filename + "_all_2002" +".fasta"
    filename14 = filename + "_all_2001" +".fasta"
    filename15 = filename + "_all_2000" +".fasta"
    filename16 = filename + "_all_1999" +".fasta"
    filename17 = filename + "_all_1998" +".fasta"
    filename18 = filename + "_all_1997" +".fasta"
    filename19 = filename + "_all_1996" +".fasta"
    filename20 = filename + "_all_1995" +".fasta"
    filename21 = filename + "_all_2015" +".fasta"

    g1 = open(filename1, "w")
    g2 = open(filename2, "w")
    g3 = open(filename3, "w")
    g4 = open(filename4, "w")
    g5 = open(filename5, "w")
    g6 = open(filename6, "w")
    g7 = open(filename7, "w")
    g8 = open(filename8, "w")
    g9 = open(filename9, "w")
    g10 = open(filename10, "w")
    g11 = open(filename11, "w")
    g12 = open(filename12, "w")
    g13 = open(filename13, "w")
    g14 = open(filename14, "w")
    g15 = open(filename15, "w")
    g16 = open(filename16, "w")
    g17 = open(filename17, "w")
    g18 = open(filename18, "w")
    g19 = open(filename19, "w")
    g20 = open(filename20, "w")
    g21 = open(filename21, "w")
    strainer=open("unsortable.fasta", "a")
    outg = open("outgroup.fasta", "a")
    oth = open("unusedyears.fasta", "a")

    group1 = ["2014", "14"]
    group2 = ["2013", "13"]
    group3 = ["2012", "12"]
    group4 = ["2011", "11"]
    group5 = ["2010", "10"]
    group6 = ["2009", "09"]
    group7 = ["2008", "08"]
    group8 = ["2007", "07"]
    group9 = ["2006", "06"]
    group10 =["2005", "05"]
    group11 = ["2004", "04"]
    group12 = ["2003", "03"]
    group13 = ["2002", "02"]
    group14 = ["2001", "01"]
    group15 = ["2000", "00"]
    group16 = ["1999", "99"]
    group17 = ["1998", "98"]
    group18 = ["1997", "97"]
    group19 = ["1996", "96"]
    group20 = ["1995", "95"]
    group21 = ["2015", "15"]


    outgroup= ["1968", "68", "1969", "69", "1970", "70", "1971", "71", "1972", "72", "1973", "73","1974","74", "1975","75", "1976","76", "1977", "77"]

    otheryears= ["1978", "78", "1979", "79", "1980", "80", "1981", "81", "1982", "82", "1983", "83", "1984", "84", "1985", "85", "1986", "86", "1987", "87","1988", "88","1989", "89","1990", "90","1991","91", "1992", "92","1993", "93","1994", "94"]



    handle = open(infile, "rU")
    for record in  SeqIO.parse(handle, "fasta"):
        identifier = str(record.id).split("_")
        #Search for the year of the sequences, moving from end to start
        #The year should be at the end of the FASTA header, but sometimes there are other
        #pieces of text tacked on the end.
        for i in [1,2,3, 4, 5]: 
            if identifier[-i] in group21:
                g21.write(">%s\n" % record.id)
                g21.write("%s\n" % record.seq)
                break
            elif identifier[-i] in group1:    
                g1.write(">%s\n" % record.id)
                g1.write("%s\n" % record.seq)
                break
            elif identifier[-i] in group2: 
                g2.write(">%s\n" % record.id)
                g2.write("%s\n" % record.seq)
                break
            elif identifier[-i] in group3:
                g3.write(">%s\n" % record.id)
                g3.write("%s\n" % record.seq)
                break
            elif identifier[-i] in group4:
                g4.write(">%s\n" % record.id)
                g4.write("%s\n" % record.seq)
                break
            elif identifier[-i] in group5:
                g5.write(">%s\n" % record.id)
                g5.write("%s\n" % record.seq)
                break
            elif identifier[-i] in group6:
                g6.write(">%s\n" % record.id)
                g6.write("%s\n" % record.seq)
                break
            elif identifier[-i] in group7:
                g7.write(">%s\n" % record.id)
                g7.write("%s\n" % record.seq)
                break
            elif identifier[-i] in group8:
                g8.write(">%s\n" % record.id)
                g8.write("%s\n" % record.seq)
                break
            elif identifier[-i] in group9:
                g9.write(">%s\n" % record.id)
                g9.write("%s\n" % record.seq)
                break
            elif identifier[-i] in group10:    
                g10.write(">%s\n" % record.id)
                g10.write("%s\n" % record.seq)
                break
            elif identifier[-i] in group11:
                g11.write(">%s\n" % record.id)
                g11.write("%s\n" % record.seq)
                break
            elif identifier[-i] in group12:
                g12.write(">%s\n" % record.id)
                g12.write("%s\n" % record.seq)
                break
            elif identifier[-i] in group13:
                g13.write(">%s\n" % record.id)
                g13.write("%s\n" % record.seq)
                break
            elif identifier[-i] in group14:
                g14.write(">%s\n" % record.id)
                g14.write("%s\n" % record.seq)
                break
            elif identifier[-i] in group15:
                g15.write(">%s\n" % record.id)
                g15.write("%s\n" % record.seq)
                break
            elif identifier[-i] in group16:
                g16.write(">%s\n" % record.id)
                g16.write("%s\n" % record.seq)
                break
            elif identifier[-i] in group17:
                g17.write(">%s\n" % record.id)
                g17.write("%s\n" % record.seq)
                break
            elif identifier[-i] in group18:
                g18.write(">%s\n" % record.id)
                g18.write("%s\n" % record.seq)
                break
            elif identifier[-i] in group19:
                g19.write(">%s\n" % record.id)
                g19.write("%s\n" % record.seq)
                break
            elif identifier[-i] in group20:
                g20.write(">%s\n" % record.id)
                g20.write("%s\n" % record.seq)
                break
            elif identifier[-i] in group21:
                g21.write(">%s\n" % record.id)
                g21.write("%s\n" % record.seq)
                break
            elif identifier[-i] in outgroup:
                outg.write(">%s\n" % record.id)
                outg.write("%s\n" % record.seq)    
                break
            elif identifier[-i] in otheryears:
                oth.write(">%s\n" % record.id)
                oth.write("%s\n" % record.seq)    
                break    
            else:
                strainer.write(">%s\n" % record.id)

    #print infile
    g1.close()
    g2.close()
    g3.close()
    g4.close()
    g5.close()
    g6.close()
    g7.close()
    g8.close()
    g9.close()
    g10.close()
    g11.close()
    g12.close()
    g13.close()
    g14.close()
    g15.close()
    g16.close()
    g17.close()
    g18.close()
    g19.close()
    g20.close()
    g21.close()
    outg.close()
    handle.close()
    strainer.close()
def control():

    if len(sys.argv) < 2:
        print "Please provide at least one FASTA as an argument"

    else:
        args = sys.argv[1:]
        for infile in args:
            time_sort(infile)
            
control()


