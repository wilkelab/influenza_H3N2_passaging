"""
This script retrieves the dN column from .dat files generated from SLAC, and joins them in a table. 
Additionally joins in list of physical characteristics and other dN measurements from numbering_table.csv, which comes from 'Geometric constaints dominate the antigenic evolution of influenza H3N2 hemagglutinin', Meyer and Wilke, 2015
dN is used to approximate dN/dS where dS = 1, following S. J. Spielman, S. Wan, C. O. Wilke (preprint). One-rate models outperform two-rate models in site-specific dN/dS estimation. [bioRxiv]. doi: 10.1101/032805
7/17/2015 CDM

"""
import pandas as pd
import csv
from pandas import DataFrame
import glob
import os

def join_columns():

    #Retrieve all data files outputted by HYPHY SLAC
    pwd = os.getcwd()
    filepath1 = str(pwd)+"/*.dat"
    print filepath1
    
    #retrieve physical measurements from downloaded S1 Dataset, Meyer and Wilke, 2015, DOI: 10.1371/journal.ppat.1004940
    numtable = pd.read_table("numbering_table.csv", sep=",")
    txt = glob.glob(filepath1)
    firstfile = True
    
    #Joining columns together from the .dat files
    for textfile in txt:
    
	filename = textfile.split(".")[0]
	filename = filename.split("/")[-1]
        #print textfile,filename
	mycols=filename
	ptable = DataFrame(pd.read_table(textfile))
        #print ptable
        #Make sure the dataframe from the .dat file is not empty
        if ptable is not None:
            #Take the single rate dN/dS column  
    	    dns=DataFrame(ptable['dN'])
	
	    dns.columns=[filename]
	    #for the first file
	    if firstfile == True:
       		holder = dns
                firstfile = False
            #Join subsequent files with the first file
            else:
         	holder = holder.join(dns)
            

        else:
		print textfile + " does not exist!"
    #Add on the table from the S1 dataset
    holder=holder.join(numtable)
    #This csv will be the input data for statistics and figures
    holder.to_csv("slac_output.csv", index=False)

join_columns()


