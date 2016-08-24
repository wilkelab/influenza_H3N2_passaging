#!/usr/bin/env python 
#########################################################################################
# Modified by Claire McWhite 
# for use in
# "Serial passaging causes extensive positive selection in seasonal influenza A hemagglutinin", 2016
#
# from rank_sequences.py by
#
# author: Richard Neher
# email: richard.neher@tuebingen.mpg.de
#
# Reference: Richard A. Neher, Colin A Russell, Boris I Shraiman. 
#            "Predicting evolution from the shape of genealogical trees"
#
#########################################################################################
#
# get_trunk.py
# Retrieve a fasta of 
# to a folder named by current date and time.
# INPUT:
# --aln             name of the alingment file, fasta format. can be gzipped
# --outgroup        name of the outgroup sequence. has to in the alignment file
# --destdir         output folder
# --plot            whether to plot the tree or not
#
#########################################################################################


import argparse

#########################################################################################
###parse the command line arguments
#########################################################################################
parser = argparse.ArgumentParser(description="rank sequences in a multiple sequence aligment")
parser.add_argument('--aln', type=str, required= True, help = 'alignment of sequences to by ranked')
parser.add_argument('--destdir', type=str, required= True, help = 'destination folder for output')
parser.add_argument('--outgroup', type=str,required= True, help = 'name of outgroup sequence')
parser.add_argument('--collapse', const = True, default=True, nargs='?', help='collapse internal branches with identical sequences')
#parser.add_argument('--plot', const = True, default=False, nargs='?', help='plot trees')
params=parser.parse_args()
#########################################################################################
#import matplotlib
#matplotlib.use('pdf')
import sys,time,os,argparse
sys.path.append('./trunk_src')
from sequence_ranking import *
import tree_utils
from Bio import Phylo,AlignIO,SeqIO, Align
#from matplotlib import pyplot as plt
import numpy as np

## matplotlib set up
#mpl_params = {'backend': 'pdf',  
#          'axes.labelsize': 20, 
#          'text.fontsize': 20,
#'font.sans-serif': 'Helvetica',
#'legend.fontsize': 18,
#'xtick.labelsize': 16,
#'ytick.labelsize': 16,
#'text.usetex': False}
#plt.rcParams.update(mpl_params)
#
##########################################################################################
def ofunc(fname, mode):
    '''
    custom file open that chooses between gzip and regular open
    '''
    if fname[-3:]=='.gz':
        import gzip
        return gzip.open(fname,mode)
    else:
        return open(fname,mode)
##########################################################################################

##########################################################################################
## read the alignment, identify the outgroup 
##########################################################################################
aln = Align.MultipleSeqAlignment([])
outgroup=None
with ofunc(params.aln, 'r') as alnfile:
    for sec_rec in SeqIO.parse(alnfile, 'fasta'):
        if sec_rec.name!=params.outgroup:
            aln.append(sec_rec)
        else:
            outgroup=sec_rec

if outgroup is None:
    print "outgroup not in alignment -- FATAL"
    exit()

#######################################################################################
## set up the sequence data set and make a phylo tree 
#######################################################################################
seq_data = alignment(aln, outgroup, collapse=True)
print dir(seq_data)
print seq_data.T

#######################################################################################
## output
#######################################################################################

# make directory to write files to

dirname='./' + params.destdir
if not os.path.isdir(dirname):
    os.mkdir(dirname)

# name internal nodes
for ni,node in enumerate(seq_data.T.get_nonterminals(order='preorder')):
    node.name = str(ni+1)

# write tree to file
Phylo.write(seq_data.T, dirname+'/reconstructed_tree.nwk', 'newick')

print seq_data.T
def get_parent(tree, child_clade):
    """http://biopython.org/wiki/Phylo_cookbook
    This function get names of nodes between the root and the input clade
    Output includes input clade, and not root clade"""
    node_path = tree.get_path(child_clade)
    return node_path

#create a dictionary of clades and their depth. 
#tree_depth = seq_data.T.depths()
#print tree_depth

"""Get random 2015 sequence as the terminal trunk sequence
Tree is travered by level
Sequence of the last level in 2015 is chosen"""

myclade = seq_data.T.find_elements(name=".*2015", order='level').next() 

parent = get_parent(seq_data.T, myclade)
assert myclade in parent
print "parent", parent

"""Trunk always includes root
Root always named '1'
Nodes are named with order = 'preorder' so labeling begins at root"""
trunk_names =['1'] 

for f in parent:
   trunk_names.append(f.name)


print "trunk names", trunk_names


# write inferred ancestral sequences and trunk sequences to file
with open(dirname+'/ancestral_sequences.fasta', 'w') as outfile1:
    with open(dirname+'/trunk_sequences.fasta', 'w') as outfile2:
   
        for node in seq_data.T.get_nonterminals():
            outfile1.write('>'+node.name+'\n'+str(node.seq)+'\n')
            if node.name in trunk_names:
                outfile2.write('>'+node.name+'\n'+str(node.seq)+'\n')
#Deleted since trunk doesn't include terminal
#        for node in seq_data.T.get_terminals():
#            if node.name in trunk_names:    
#                outfile2.write('>'+node.name+'\n'+str(node.seq)+'\n')
  

# plot the tree if desired
#if params.plot:
#    tree_utils.plot_prediction_tree(prediction, method='polarizer', internal=True)
#    plt.savefig(dirname+'/marked_up_tree.pdf')
