'''
This script calculates dN for a FASTA of trunk nucleotide sequences
Sequence must be in order from root to terminal
5/16 Claire McWhite
'''


import os
import sys
import argparse
import subprocess
from Bio import Seq
from Bio import SeqIO
from Bio.Alphabet import generic_dna
import count_sites
import count_mutations

def parse_args():
    parser = argparse.ArgumentParser(description = 'Takes a file of sequential trunk nucleotide sequences in fasta format and computes codon sitewise dN. Sequences must be ordered root -> tip')
    parser.add_argument("infile", metavar = "infile",  type = str, help = "A file containing trunk nucleotide sequences in fasta format")
    parser.add_argument("outfile", metavar = "outfile",  type = str, help = "An outfile name")
    
    return parser.parse_args()


def parse(infilename, outfilename):

    #FASTA containing trunk sequences in order of root to tip
    recs = list(SeqIO.parse(infilename, 'fasta')) 

    #Walk along the trunk, comparing each node sequence to the next node sequence
    for j in range(0, len(recs)-1):
        seq1 = recs[j].seq
        seq2 = recs[j+1].seq

     
        #Get a lists of nonsynonymous and synonymous nucleotide sites
        S =  count_sites.SiteCounter()
        ( ns_site_counts, s_site_counts ) = S.countSites( seq1)
        #print ns_site_counts
        #print s_site_counts

        #Get a lists of nonsynonymous and synonymous nucleotide mutations
        M =  count_mutations.MutationCounter()
        ( ns_mut_counts, s_mut_counts ) = M.countMutations( seq1,seq2)
        print ns_site_counts
        print ns_mut_counts
          
        #Create running totals of sitewise counts 
        if j == 0:
            total_ns_mut = ns_mut_counts
            total_ns_sites = ns_site_counts
        else:
            #total_ns_mut is total number of mutations observed at a nucleotide site
            total_ns_mut=[sum(x) for x in zip(total_ns_mut, ns_mut_counts)]
            #total_ns_sites is total of observed nonsynonymous sites.
            #Will be divided by total number of sequences to get average nonsynonous value for each site
            total_ns_sites=[sum(x) for x in zip(total_ns_sites, ns_site_counts)]

        
    ns_codon_mut=[]
    ns_codon_site=[]

    #Sum all the nonsynonymous mutations at a codon (3 nucleotide -> 1 codon)
    #Average all the nonsynonymous sites at a codon 
    for i in range(0,len(total_ns_mut), 3):
       print i
       ns_codon_mut.append(total_ns_mut[i]+total_ns_mut[i+1]+total_ns_mut[i+2])
       ns_codon_site.append((total_ns_sites[i]+total_ns_sites[i+1]+total_ns_sites[i+2]))


 
    print ns_codon_mut
    print len(ns_codon_mut)
    print ns_codon_site
    print len(ns_codon_site)   

    #Make sure mutations and sites codon list lengths are in sync
    assert len(ns_codon_mut)==len(ns_codon_site)


    #Get average number of nonsynonymous sites per codon by dividing by number of sequences      
    tot_seqs = len(recs) 
    print tot_seqs, "total sequences"
    avg_ns_sites = [ x/tot_seqs for x  in ns_codon_site]

  
    print zip(ns_codon_mut, avg_ns_sites)
    #Calculate dN by dividing total number of nonsynonymous mutation sby average number of nonsynonymous sites at codon.
    dn = [x/y if y != 0 else 0.0 for x,y in zip(ns_codon_mut, avg_ns_sites)]
    print "final DN"
    print dn
 
    print len(dn)
    outfile = open(outfilename, "w")
    outfile.write("pos\tdN\n")
    for i in range(0, len(dn)):
       output = str(i + 1) + "\t" + str( dn[i])
       outfile.write(str(output)+"\n")
    

def main():
    args = parse_args()
    while args.infile is None:
        args.infile = raw_input("\nYou gotta specify an input file: ")
        if not os.path.exists(args.infile):
            args.infile = None
    while args.outfile is None:
        args.outfile = raw_input("\nYou gotta specify an input file: ")
        if not os.path.exists(args.outfile):
            args.outfile = None

    parse(args.infile,args.outfile)

main()
 


