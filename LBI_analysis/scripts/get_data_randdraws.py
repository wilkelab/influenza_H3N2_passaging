
#This is for the large random draws in order to compute the mean distance to the next year



import sys
import pandas as pd
from Bio import SeqIO
import os
import glob
import random

def get_info(fasta_file, cond, tmp_list):


     for stat in ['rankseq']:#, 'inffit_collapse', 'rankseq', 'inffit_def', 'inffit_gam3']:

        condition_label = cond.replace("outgroup_", "")
        #print condition_label
        passage = condition_label.split("_")[0]
        category = condition_label.split("_")[1]
        year = condition_label.split("_")[2]
        trial = category.split('x')[1]
#        print trial
        #if int(trial)>49:
        #  continue

        seq_loc = "output/" + str(cond) + "_" + stat

        #Get ancestral sequence from the same year, same species
        ancestral_fasta_file = seq_loc + "/ancestral_sequences.fasta"
        ancestral_dict = SeqIO.to_dict(SeqIO.parse(ancestral_fasta_file, "fasta"))
        if not ancestral_dict:
           return tmp_list
        ancestor_seq =  str(ancestral_dict["1"].seq)
        



        seqrank_file = seq_loc + "/sequence_ranking_terminals.txt"

        top_rank = pd.read_table(seqrank_file, sep="\t")
 #       #print top_rank
        seq_id = top_rank[top_rank['rank']==1]
        top_seqID = seq_id.get_value(0, '#name')

        if stat == 'rankseq':
            coi = 'LBI'

        else:
            coi = 'mean'
        top_LBI = seq_id.get_value(0, coi)

        ##print top_LBI

        record_dict = SeqIO.to_dict(SeqIO.parse(fasta_file, "fasta"))

        #get number of sequences
        numseq= len(record_dict) - 1

        #get reconstructed sequence of top hit
        top_seq = str(record_dict[top_seqID].seq)

        #get random sequence
        selection ="not found"
        while selection=="not found":  
            random_seqID = random.choice(list(record_dict.keys()))
            random_seq = str(record_dict[random_seqID].seq)
            if random_seqID=="outgroup":
                selection = "not found"
            else:
                selection = "found"

        #get mean of LBI
        mean = top_rank[[coi]].mean(axis=0).get_value(coi)
        ##print mean

        #Get stdev of LBI
        stdev = top_rank[[coi]].std(axis=0).get_value(coi)
        ##print stdev


  


        tmp_list.append([passage, year, category, trial, stat, top_seqID, mean, stdev, numseq, top_seq, ancestor_seq, random_seqID, random_seq])

     return tmp_list


 

def hamming_distance(s1, s2):
    #Return the Hamming distance between equal-length sequences
    #http://biology.stackexchange.com/questions/23523/hamming-distance-between-two-dna-strings
    if len(s1) != len(s2):
        raise ValueError("Undefined for sequences of unequal length")
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))



def hamming_to_next_year(tmp_df):
    #print "The starting tmp_df"
    #print tmp_df
    final_list=[]
    final_list.append(["passage", "year", "category", "trial", "stat", "topRankID", "mean", "stdev", "num_seq", "topRankSeq", "ancestral_seq", "random_seqID", "random_seq", "hamming_to_next_self", "hamming_to_next_unpassaged", "hamming_to_next_pooled", "hamming_rand_self", "hamming_rand_unpassaged", "hamming_rand_pooled", "ratio_self", "ratio_unpassaged", "ratio_pooled"])     
#    #print final_list
    for trial in range(0, 49):
#    for trial in [0]:
#        #print trial
        for passage in ['egg', 'unpassaged', 'pooled', 'siat', 'nonsiat', 'cell', 'monkey']:

            for year in range(2005, 2015):
    #            #print final_list
    #            #print year
                #print passage, year, trial
                ##print tmp_df['year']
                ##print tmp_df['passage']
                ##print tmp_df['trial']
                ##print tmp_df
                
                           
                    
                current = tmp_df[(tmp_df['year']==str(year)) & (tmp_df['passage']==passage) & (tmp_df['trial']==str(trial))]
                
                ##print current
               
                

                nextyear_self = tmp_df[(tmp_df['year']==str(year+1)) & (tmp_df['passage']==passage) & (tmp_df['trial']==str(trial))]

                nextyear_unpassaged = tmp_df[(tmp_df['year']==str(year+1)) & (tmp_df['passage']=='unpassaged') & (tmp_df['trial']==str(trial))]

                nextyear_pooled = tmp_df[(tmp_df['year']==str(year+1)) & (tmp_df['passage']=='pooled') & (tmp_df['trial']==str(trial))]

                #print current
                if current.empty:
                    #print current
                    #print "out of years"
                    continue

                curr_seq = current.iloc[0]['topRankSeq']
                rand_seq = current.iloc[0]['random_seq']

                ##print curr_seq
                ##print rand_seq
              
 

                try:
                     #print nextyear_self
                     next_seq_self = nextyear_self.iloc[0]['ancestral_seq']
                     #print next_seq_self
                     ham_self =  hamming_distance(curr_seq, next_seq_self)
                     ham_rand_self =  hamming_distance(rand_seq, next_seq_self)
                     ratio_self = float(ham_self)/ham_rand_self 
                     #print "hammings ", ham_self, ham_rand_self, ratio_self

                except Exception as e:
                     #print e
                     ham_self= "n/a"                    
                     #print "self problem" 
                     ham_rand_self="n/a"
                     ratio_self="n/a"
                try:
                     next_seq_unpassaged = nextyear_unpassaged.iloc[0]['ancestral_seq']
                     ham_unpassaged =  hamming_distance(curr_seq, next_seq_unpassaged)

                     ham_rand_unpassaged =  hamming_distance(rand_seq, next_seq_unpassaged)
                     ratio_unpassaged = float(ham_unpassaged)/ham_rand_unpassaged
                     
                except:
                     ham_unpassaged = "n/a"
                     ratio_unpassaged="n/a"
                     ham_rand_unpassaged="n/a"
                try:
                     next_seq_pooled = nextyear_pooled.iloc[0]['ancestral_seq']
                     ham_pooled =  hamming_distance(curr_seq, next_seq_pooled)
                     ham_rand_pooled =  hamming_distance(rand_seq, next_seq_pooled)
                     ratio_pooled = float(ham_pooled)/ham_rand_pooled

                except:
                     ham_pooled = "n/a"
                     ratio_pooled="n/a"
                     ham_rand_pooled="n/a"
                row =  map(list, current.values)[0]
                
                #print "ratios", ratio_self, ratio_unpassaged, ratio_pooled
                final_row = row + [ham_self, ham_unpassaged, ham_pooled, ham_rand_self, ham_rand_unpassaged, ham_rand_pooled, ratio_self, ratio_unpassaged, ratio_pooled]
#                #print ham_self, ham_unpassaged, ham_pooled
                ##print final_row
                final_list.append(final_row)
    #print final_list       
    return final_list
             #   top_seqID = seq_id.get_value(0, '#name')

if __name__ == '__main__':

    tmp_list=[]
    tmp_list.append(["passage", "year", "category", "trial", "stat", "topRankID", "mean", "stdev", "num_seq", "topRankSeq", "ancestral_seq", "random_seqID", "random_seq"])     
    for filename in glob.glob('fastas/outgroup_*x*_????.fasta'):
         print filename
         fasta_file = filename
         cond = filename.replace(".fasta", "")
         cond = cond.replace("fastas/", "")
         try:

             tmp_list = get_info(fasta_file, cond, tmp_list)
             #print tmp_list
         except Exception as e:
             print e
             #print "skipping, Fasta does not exist " + cond

    
    #print tmp_list
    tmp_dataframe = pd.DataFrame(tmp_list)
    tmp_dataframe.columns = tmp_dataframe.iloc[0]
    tmp_dataframe =tmp_dataframe.reindex(tmp_dataframe.index.drop(0))


#                next = tmp_df[tmp_df['year']==year + 1  && tmp_df['passage']==passage && tmp_df['stat'==stat]]
#                #print current
#
#print tmp_dataframe
final_list = hamming_to_next_year(tmp_dataframe)
final_dataframe = pd.DataFrame(final_list)
final_dataframe.columns = final_dataframe.iloc[0]
final_dataframe =final_dataframe.reindex(final_dataframe.index.drop(0))

#Not going to save each of the sequences
##print final_dataframe
final_dataframe.to_csv('single_year_analysis_50draws_sequences.txt', sep="\t", index=False)

cut_dataframe = final_dataframe[["passage", "year", "category", "trial", "stat", "topRankID", "mean", "stdev", "num_seq", "hamming_to_next_self", "hamming_to_next_unpassaged", "hamming_to_next_pooled", "hamming_rand_self", "hamming_rand_unpassaged", "hamming_rand_pooled", "ratio_self", "ratio_unpassaged", "ratio_pooled"]]
cut_dataframe.to_csv('single_year_analysis_10draws.txt', sep="\t", index=False)

