"""
Pymol script to assign colors to individual residues of a protein structure 

Takes a pdb file and list of values (one per amino acid) as command line arguments
Recommend 2YP7clean.pdb as working influenza H3 structure

Written AGM, modified CDM 9/2015
"""

import sys

def color_structure(pdbname, colorvaluesname):

    cmd.load(pdbname)
    cmd.hide('all')
    cmd.show('cartoon')
    cmd.cartoon('tube')
    cmd.set('cartoon_tube_radius', 0.9)

    # open the file of new values (just 1 column of numbers, one for each alpha carbon)
    colorvalues = open(colorvaluesname, 'r')
    
    # create the global, stored array
    stored = []
    
    # read the new B factors from file
    for line in colorvalues.readlines(): stored.append( float(line) )
    
    max_b = max(stored)
    min_b = min(stored)
    
    cmd.bg_color("white")
    print min_b
    print max_b
    
    #min_b=-0.142
    #max_b=0.31
    
    # close the input files
    colorvaluesname.close()
    pdbname.close()
    
    # clear out the old B Factors
    cmd.alter("%s and n. CA"%pdb, "b=0.0")
    
    # update the B Factors with new properties
    cmd.alter("%s and n. CA"%pdb, "b=stored.pop(0)")
    
    # color the protein based on the new B Factors of the alpha carbons
    cmd.spectrum("b", "rainbow", "%s and n. CA"%pdb, minimum=min_b, maximum=max_b)
    
    cmd.ray("775", "2400")
    cmd.png("unscaled%s.png"%colorvaluesname.split("_")[0])


if len(sys.argv) != 3:
    print "Please provide pdb filename and color value filename as command-line arguments"
    print "Pymol command line -> run color_script.py -- 2YP7clean.pdb orig1000_inverse_dnds.corr"

else:
    color_structure(sys.argv[1], sys.argv[2])
