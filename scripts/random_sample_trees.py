from ete3 import Tree
from Bio import SeqIO
import argparse
import random
from copy import deepcopy

def pruning_tree(randrecords, tree):
    tree.prune(randrecords, preserve_branch_length=True)
    return tree   

def pruning(inputtree, inputfasta, passage, years, length, draws):

#    inputNEXUS=open(inputtree, "r").read()
#    inputNewick = inputNEXUS.

    k = open(inputtree, "r").read()
    print k
  
    f = Tree(inputtree)
   # print f

    IDlist=[]
    fasta = open(inputfasta, "rU")


    record_dict = SeqIO.to_dict(SeqIO.parse(fasta, "fasta"))
    for recordID in record_dict.keys():
         print recordID

    #    for record in SeqIO.parse(fasta, "fasta"):
         IDlist.append(recordID)
    print IDlist
    #length=5
 

    for i in range(0, draws):
            identifier = "samp"+"_"+ passage + "_" + str(length)+ "x"+ str(i)+"_"+ years
            tree_outfilename = identifier + ".tree"
            tree_outfile=open(tree_outfilename, "w")
            fasta_outfilename = identifier +".fasta"
            fasta_outfile=open(fasta_outfilename, "w")
            randrecords = random.sample(IDlist, length)
            print "Pass ", randrecords
            tmptree = deepcopy(f) 
            #print tmptree
           # print f
            print "pruning..."
            tmptree.prune(randrecords, preserve_branch_length=True)
            tmptree.write(format=0, outfile=tree_outfilename)
    #        print tmptree
            for node in tmptree.traverse("postorder"):
                if node.name=="":
                    continue
                print node.name
                ID = ">"+ node.name +"\n"
                fasta_outfile.write(ID)
                fasta_outfile.write(str(record_dict[node.name].seq)+"\n")  

            del tmptree 
    print "pruned"






def parse_args():

   parser=argparse.ArgumentParser(description = 'Takes a newick tree and an accompanying fasta file of terminal node sequences and does multiple random draws of the tree, pruning each sample')
   parser.add_argument('inputtree', metavar='inputtree', type=str, help = 'A Newick format Tree. IDs must match FASTA sequences')
   parser.add_argument('inputfasta', metavar='inputfasta', type=str, help = 'A FASTA file of aligned nucleotide sequences. Must match tree terminal node IDs')
   parser.add_argument('passage', metavar='passage', type=str, help = 'passage history')
   parser.add_argument('years', metavar='years', type=str, help = 'years ex. 20052015')
   parser.add_argument('length', metavar='length', type=int, help = 'number of sequences to draw')
   parser.add_argument('draws', metavar='draws', type=int, help = 'number of draws to make')

   return parser.parse_args()


  
def main():
   args = parse_args()
   pruning(args.inputtree, args.inputfasta, args.passage, args.years, args.length, args.draws)

main()

