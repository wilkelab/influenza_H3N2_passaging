"""
This script takes multiple fasta files, and determines the length of the shortest one by counting the ">" that starts a FASTA header


Written by CDM
"""

import sys

def fastalength(args):
	
    longest=0
    for infile in args:
        x = open(infile, "rU").read()
        lenx = x.count(">")
        if lenx > longest:
            longest = lenx               
	
    shortest=longest
    for infile in args:
                
        x = open(infile, "rU").read()
        lenx = x.count(">")
        if lenx < shortest:
            shortest = lenx
    print "the lowest number of sequences is: " + str(shortest)
    return shortest


