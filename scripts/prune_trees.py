from ete3 import Tree
from Bio import SeqIO
import argparse
import random
from copy import deepcopy


def pruning(inputtree, inputfasta, tree_outfilename):
    #This function remove sequences from a FASTA from a larger tree
    

    #Full initial tree - to be pruned
    k = open(inputtree, "r").read() 

    #ete3 Tree format
    f = Tree(inputtree)
 
    #List of IDs to be picked from the full FASTA
    IDlist=[] 
    fasta = open(inputfasta, "rU")
    record_dict = SeqIO.to_dict(SeqIO.parse(fasta, "fasta"))
    for recordID in record_dict.keys():
         print recordID
         IDlist.append(recordID)
    print IDlist

    tree_outfile=open(tree_outfilename, "w")

    print "pruning...", inputfasta
    f.prune(IDlist, preserve_branch_length=True)
    f.write(format=0, outfile=tree_outfilename)
    print "pruned", inputfasta






def parse_args():

   parser=argparse.ArgumentParser(description = 'Takes a newick tree and a FASTA file, and prunes away sequences not contained in FASTA from tree')
   parser.add_argument('inputtree', metavar='inputtree', type=str, help = 'A Newick format Tree. IDs must match FASTA sequences')
   parser.add_argument('inputfasta', metavar='inputfasta', type=str, help = 'a fasta file of aligned nucleotide sequences. must match tree terminal node ids')
   parser.add_argument('tree_outfilename', metavar='tree_outfilename', type=str, help = 'outfile name for pruned tree')
   return parser.parse_args()


  
def main():
   args = parse_args()
   pruning(args.inputtree, args.inputfasta, args.tree_outfilename)

main()

