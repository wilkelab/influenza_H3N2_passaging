#Serial passaging causes extensive positive selection in seasonal Influenza A hemagglutinin


####This project aims to investigate the effects of viral passaging on influenza evolutionary analysis.  Running the analysis with an input of passage annotated influenza sequences will:
 
 1. Divide a nucleotide FASTA of Influenza hemagglutinin sequences into groups by passage history (egg amniote, generic cell culture, rhMK cell culture, MDCK-SIAT1 cell passaged, non-SIAT1 cell passaged, and unpassaged).

 2. Construct rooted phylogenetic trees of sequences from each passage history, as well as a pooled group of all sequences. Additionally, some experimental conditions take random draws of sequences from particular passage histories and time periods.

 3. Reconstruct dN/dS evolutionary rates using a HyPhy implementation of SLAC for the phylogenetic full tree, internal branch, and tip branches.

Repository contains data supporting:
Serial passaging causes extensive positive selection in seasonal influenza A hemagglutinin
Claire D. McWhite1,2, Austin G. Meyer1,3,4, Claus O. Wilke1,3,4

1Center for Systems and Synthetic Biology and Institute for Cellular and Molecular
Biology, The University of Texas at Austin, Austin, TX 78712

2Department of Molecular Biosciences, The University of Texas at Austin, Austin, TX
78712

3Center for Computational Biology and Bioinformatics, The University of Texas at
Austin, Austin, TX 78712

4Department of Integrative Biology, The University of Texas at Austin, Austin, TX 78712 


Repository contains all output of the analysis used in "Serial passaging causes extensive positive selection in seasonal influenza A hemagglutinin"
*All FASTA files have been removed per the GISAID user agreement*

####README contain instructions for fully rerunning this analysis, notes for analysis, and a table of contents for this repository. 

# Instructions to run analysis
Requirements:
*  Python 2.7
*  Pandas (Here, 0.13)
*  BioPython (Here, 1.66)
*  FastTree 2.18 or higher compiled for short branch lengths (see below)
*  HyPhy (Here, 2.26) http://hyphy.org/
*  R 3.2.1 or above  
*  FigTree or other tree visualization software

First, remove all .tree files in /trees/, .txt files in input_fasta_summary, and .dat files in /rate_measurement_data/, and .corr .raw .png and .csv files in data_analysis
- - -
## Initial data download and FASTA formatting
- - -

### 1. Data download and setup steps

*  git clone project into linux home directory
*  Create GISAID account (http://platform.gisaid.org/epi3/frontend)
*  From http://platform.gisaid.org/epi3/frontend -> EpiFlu tab, select sequences with the following parameters
 Type = *A*, H = *3*, N=*2*, Host = *Human*, Location = *North America*, Required Segments = *HA, only complete*
*  On the released files page, select all, and click Download
*  On the download option page, download with the following parameters: 
Format = *Sequences (nucleotides) as FASTA*, Proteins = *HA*, FASTA Header = *Isolate name, Passage details/history*, Date format= *YYYY-MD-DD, Replace spaces with underscores in FASTA header* -> click download
*  Also download GISAID acknowledgements table 
*  With enough sequences the GISAID acknowledgments table may not be able to download all at once.  May have to break up the download into several time periods
*  Place raw GISAID fasta file into the **/input_data** folder


### 2. Requirements
##### a. Compile FastTree for short branch lengths suitable for influenza data
*  Default FastTree does not allow branch lengths less than 0.0005
*  FastTree must be version 2.1.7 or higher, compiled with the following line to allow the type of short branch lengths in influenza trees:
*  Download FastTree.c (http://meta.microbesonline.org/fasttree/FastTree.c)
*  Run:
*         $ gcc -DUSE_DOUBLE -O3 -finline-functions -funroll-loops -Wall -o FastTree FastTree.c -lm
*         See http://meta.microbesonline.org/fasttree/ for details
*  Place compiled FastTree in path

### 3. Clean starting fasta of long branch length and abnormal sequences
*  In **/run_analysis** run: $ bash step1_format_fasta.bash ../input_data/[name_of_downloaded_gisaid.fasta]
*  This will output formatted.tree to the top level /trees folder. 

### 4. Manual inspection of phylogenetic tree and removal of abnormal clades
*  Often, downloaded influenza data contain anomalous sequences which introduce long branch lengths
*  Open formatted.tree (stored in /trees/formatting_trees) using a tree visualization program such as FigTree
*  Copy any long branch (over 0.01 length) clades into a new file and call it ab.txt (can be still in newick format string).
*  FASTA IDs will be parsed out of ab.txt and removed from the rest of the analysis
*  Place ab.txt into the top level **/input_data** folder

### 5. Divide FASTA by passage history and year
*  In **/run_analysis** run: $ bash step2_divide_passage_and_year.bash 
*  Outputs FASTA files divided by year and passage history to /fastas/passage_and_year_divided_fastas/
*  Outputs FASTA files divided only by passage history to /fastas/passage_divided_fastas/
*  This bash script calls remove_sequences.py, align_and_translate.py, passageparser.py, timeseries.py, timesort.py, getpassage.py, getidentifiers.py, and get_unique_records.py.
*  remove_sequences.py removes any abnormal clades created in the previous step
*  passageparser.py divides FASTA by passage history
*  timesort.py divides output of passageparser.py by year, from 2005-2015, and creates an outgroup of sequences from 1968-1977
*  timesort.py also makes a series of summary files of passage IDs, FASTA IDs, and counts by year, which are stored in **/input_fasta_summary** 
*  timeseries.py creates timeseries_all.txt and timeseries_yearly, which contain counts of sequences divided by passage type for all years and each year, respectively
*  getpassage.py creates passageIDs_all.txt and passageIDs_yearly, which list all passage IDs sorted by their defined passage type for all years and each year, respectively. Useful for making sure that passage history is being parsed correctly 
*  getidentifiers.py creates identifies_all.txt and identifiers_yearly.txt, which list all record ids sorted by passage type for all years or each year, respectively.
*  align_and_translate.py translates and align sequences. Outputs to /fastas/formatting_fastas/. Viewing the protein alignment is useful as a check for gap introducing sequences, which should be removed from this analysis
- - -

##Evolutionary rate reconstructions

In this section, evolutionary rates (dN/dS) are reconstructed from selections of subdivided FASTA files created from step2_divide_passage_and_year.bash

Parameters for each condition are stored in bash scripts in /condition_parameters with matching names. A new condition can be made in /condition_parameters/ using the format parameters_[condition_name].sh. Each new [condition_name] must be added to run_analysis/step3_sort_conditions.bash and step4_analyze_conditions.bash



* Reconstruct dN/dS for sample sizes matched to the number of sequences in the passage type with fewest sequences between 2005 and 2015. Sample size limiter = egg culture (79 sequences)
*Folders or files with names including "eggmatched20052015" contain data associated with this condition*


* Reconstruct dN/dS for size matched samples of unpassaged, non-SIAT1 cell culture, MDCK-SIAT1 cell culture, generic cell culture, and a pooled group of sequences from 2005-2015. Sample size limiter = MDCK-SIAT1 cell culture (1046 sequences)
*Folders or files with names including "siatmatched20052015" contain data associated this condition*


* Reconstruct dN/dS for size matched samples of unpassaged, monkey cell culture, non-SIAT1 cell culture, MDCK-SIAT1 cell culture, generic cell culture, and a pooled group of sequences from 2005-2015. Sample size limiter = monkey cell culture (917 sequences)
*Folders or files with names including "monkeymatched20052015" contain data associated this condition*


* Reconstruct dN/dS for size matched samples of unpassaged, non-SIAT1 cell culture, gneric cell culture, and a pooled groups of sequences from 2005-2015. Sample size limiter = unpassaged (1703 sequences)
*Folders or files with names including "unpassagedmatched20052015" contain data associated this condition* Sample size limiter = unpassaged


* Reconstruct dN/dS for size matched samples of non-SIAT1 MDCK cell culture, MDCK-SIAT1 cell culture,  unpassaged sequences from 2014. Sample size limiter = unpassaged (249 sequences)
*Folders with names including "unpassagedmatched2014" contain data associated with this condition*

* (Not used in paper) Reconstruct dN/dS for all sequences available for all passage types from 2005-2015
unpassagedmatched2014
*Folders or fileswith names including "allsequences20052015"  contain data associated with this condition*


- - -

### 6. Sort fastas divided by year and passage history into experimental groups.  Also, take random samples for matched conditions
* In **run_analysis/** $ bash step3_sort_conditions.bash
* This script calls sort_conditions.sh for each condition, and sorts/randomly samples FASTAs according to parameters stored in /condition_parameters/
* Requires script randomdraw.py 
* For each FASTA in a condition's experimental set, this step uses FastTree to reconstruct  a phylogenetic tree

### 7. Manually format trees
* For each tree  in  **/trees**/allpassages_trees/, **trees**/matched_allpassages_trees, **/trees**/matched_nonsiatunpassaged_trees, and **trees**/matched_siatnonsiat_trees:
* Open tree in FigTree (or other tree visualization software)
* Select the outgroup branch of sequences from 1968-1977, and click Reroot (ctrl + r)
* Sort branches ascending (ctrl + u)
* Select the non outgroup branch and copy (ctrl + c)
* Open new FigTree window (ctrl + n)
* Paste in non-outgroup branch (ctrl + v)
* For an original tree named outgroup_X_N_20052014.tree, save the new non-outgroup containing tree in the same folder with the prefix samp_ or complete_ depending on if it derives from a random sample or not. Only trees from the allpassages condition should be named complete_.  Trees from matched conditions should be named samp_. Ex.outgroup_samp_siat_229a_2014.tree (unrooted tree with outgroup)->  samp_siat_229a_2014.tree (rooted tree without outgroup)

### 8. Reconstruct dN/dS
In **/run_analysis** run: $ bash step4_analyze_conditions.bash 
This script calls start_SLAC for each condition, which formats tree files for SLAC analysis, starts SLACrun.sh, sorts output data files to rate_measurement_data, and calls consolidate.py to compile output dN lists to slac_output.csv in **/data_analysis/**
*  Requires SLACrun.sh, and consolidate.py
*  It is important that .tree and .fasta base filenames match exactly, ie. complete_pooled_all_20052014.tree and complete_pooled_all_20052014.fasta
*  The formatting step creates a temporary tree files with removed spaces, extra text, pipes (|), apostrophes, and tabs, which cause errors in the HyPhy SLAC analysis.
*  slac_output.csv is the input data file for figures and statistical analysis
- - -


### 9. Map dN/dS onto structure
*Requires PyMol https://www.pymol.org/*
* First, run stats_and_figs.Rmd to generate correlations between dN and moveable inverse distance as well as a file of sitewise dN/dS (see paper for description). 
* This script will generate: 
*    nonsiat_inverse_dnds.corr -> Data for Figure 5A
*    unpassaged_inverse_dnds.corr -> Data for Figure 5B, 6A
*    nonsiat_dnds.raw
*    unpassaged_dnds.raw -> Data for Figure 6B

* Ensure files are saved in **/data_analysis** directory
* In pymol GUI command line, navigate to **/data_analysis**
* Modify input filename in color_script.py
* In the pymol GUI command line, input "run color_script.py"
* This will open 2YP7clean.pdb
* In the pymol GUI command line, input "import spectrumany"
* In the pymol GUI command line, input "spectrumany b, white red, [structure name], [minvalue], [maxvalue]"
* Save image, and repeat for each .corr or .raw file



### Extra instructions to generate a new structure_map.txt and distances.dat for a different influenza structure. Files structure_map.txt and distances.dat for pdb:2YP7 are already provided in **/data_analysis**.
*For more details see Meyer and Wilke, 2015*
*scripts and files for this analysis are in structure_mapping/*
* Download the H3N2 2YP7.pdb or other file from the Protein Data Bank
* Open in Pymol GUI
* Click S at the lower right
* Then  Display -> Sequence mode -> Chains
* Then click to highlight all chains after B, and right click delete
* Then Display -> Sequence mode -> Residues codes, and delete until first aa is position 10.
* Make sure each alpha carbon CA corresponds to one amino acid, ie. consolidate CA1 and CA2 lines to one CA 
* Check to make sure the end is around 570 aa
* Run python /scripts/translate_align_mapping.py /fastas/formatting_fastas/protein.fasta [structure_name].pdb 
*This generates structure_map.txt
*protein.fasta was generated from the formatted input FASTA by /scripts/align_and_translate.py called in step2_divide_passage_and_year.bash 
* See how many lines the structure_map.text is
* See how long any sequence in protein.fasta is
* Delete -'s from end of structure_map.txt until they match the length of a protein in protein.fasta (ex. 577 lines)
* Run /scripts/distances.py [clean structure name] to generate distances.dat for data analysis 


- - -


## Notes
*  After running step2_divide_passage_and_year.bash to remove any clades that stick out as long branch, manually check the output outgroup_pooled_all_20052014.tree first for any long branch clades remaining in the dataset. If any are found, add them to ab.txt, and rerun starting from step2_divide_passage_and_year.bash

* Random sample size can be modified in any sort_matched_type.sh script by placed the desired sample size as the first argument to python randomdraw.py, prior to the list of input files

* The regex for dividing sequences by passage type in passageparser.py is checked only for accuracy only for passage annotations in the dataset used for this project. Passage sorting of any new dataset should be manually checked for accuracy.  Useful files for checking passage sorting are created by step2_divide_passage_and_year.bash, and stored in input_fasta_summaries/.  Check unsortable.txt for sequences that can't be separated by year. Check passageIDs_all.txt to make sure passage annotations match categories, i.e. egg or generic cell.  

## Table of contents 

**/data_analysis** 
scripts for making paper figures, as well as raw data used by these scripts

  *  stats_and_figs_influenza_passaging.Rmd - R markdown script for making figures. Open in R studio, and set current working directory to **/data_analysis** and run 
  *  slac_output.csv - dN data generated from SLAC analysis
  *  color_script.py - Run from pymol command line.  Colors amino acids in a pymol structure by assigned values. 
  *  H3N2clean.pdb - modified structure from PDB:2YP7. Used as structure in figures
  *  distances.dat - Each line contains distance measurements between a reference amino acid and every other amino acid in Renumbered_Structure.pdb
  *  structure_map.txt - Guides the alignment of an input FASTA alignment and a pdb structure for generating correlations between sitewise dNs and amino acids in a structure
  *  spectrumany.py - script imported by color_script.py for custom structure coloring 


**/run_analysis**: Starting point for running analysis on an input fasta of Influenza hemagglutinin sequences annotated with passage information (available from gisaid.org).  Pulls scripts from /scripts.  Stores output data in **/rate_measurement_data**, and creates summary of evolutionary rates, slac_output.csv, stored in **/data_analysis** 
  *  step1_format_fasta.bash - Requires filename of influenza sequences with passaging information as an argument.  Input FASTA headers must have format >[passage\_abbreviation]\_|\_[strain\_ID]
  *  step2_divide_passage_and_year.bash -  Requires output of step 1, and manually confirmed phylogenetic trees. Divides sequences from the formatted FASTA by passage history and year 
  *  step3_sort_conditions.sh - Compiles FASTAs for each experimental condition in **/condition_parameters** and builds phylogenetic trees of each sample group
  *  step4_analyze_conditions - Starts the HyPhy SLAC analysis for each sample group

 
**/input_data**: Folder where user places input data for analysis
  *  Holds input FASTA from GISAID, as well as user created ab.txt file of abnormal clade identifiers from manual tree trimming after step 1

**/input_fasta_summary**: Folder stores summary data of sequences in the starting FASTA file  
  *  This folder will contain counts of sequences divided by passage history and year created during run_step2.sh
  *  timeseries_all.txt - counts of sequences from each passage type
  *  timeseries_yearly.txt - counts of sequences from each passage type by year 
  *  identifiers_all.txt - all FASTA headers divided by passage type
  *  identifiers_yearly.txt - all FASTA headers divided by passage type and year
  *  passageIDs_all.txt - all nonredundant passage identifiers - useful to check that passage history sorting from passageparser.py is correct

 
**/trees**: Storage of phylogenetic trees constructed by FastTree 2.0
  *  /formatting_trees - Trees used in course of formatting input FASTA. Will hold formatted.tree (the tree created during step 1)
  *  /allpassages_trees  - see above or **/condition_parameters** below
  *  /matched_allpassages_trees- see above or  **/condition_parameters** below
  *  /matched_nonsiatunpassaged_trees - see above or **/condition_parameters** below
  *  /matched_siatnonsiat_trees - see above or **/condition_parameters** below

**/fastas**: Storage of all FASTAs
  *  /formatting_fastas - FASTAs created in course of formatting input FASTA, including outgroup.fasta, trimmed.fasta, unsortable.fasta, unusedyears.fasta, protein.fasta, nucleotide.fasta, and abnormal_clade.fasta
  *  /passage_divided_fastas - naming format allyears_X.fasta
  *  /passage_and_year_divided_fasta - naming format div_X.fasta
  *  /tenyear_passage_divided_fastas - naming format complete_X.fasta
  *  /allsequences20052015_fastas  - see above or **/condition_parameters** below
  *  /eggmatched20052015_fastas - see above or **/condition_parameters** below
  *  /monkeymatched20052015_fastas - see above or **/condition_parameters**below
  *  /siatmatched20052015_fastas- see above or **/condition_parameters** below
  *  /unpassagedmatched20052015_fastas - see above or **/condition_parameters**below
  *  /unpassaged2014_fastas- see above or **/condition_parameters** below


**/rate_measurement_data**: Storage of all SLAC analysis evolutionary rate outputs
  *  Naming convention of files is [complete/samp]_[passage_type]_[Number of sequences]_[year range].dat
  *  complete prefix files originate from allpassaged analysis, using all available sequences from tenyear_passage_divided_fastas
  *  samp prefix files originate from matched analyses, using random samples of sequences from either 2005-2015 or 2014

**/SLAC**: Folder holds everything necessary to run SLAC on a matching FASTA and .tree file
  * /fulltree - Conventional SLAC analysis.  Models evolutionary rates from all available sequences and branches
  * /internals - Uses only internal branches of the tree to model evolutionary rates
  * /tips - Uses only tips of the tree to model evolutionary rates
  * HYPHYMP must be installed


**/scripts:**
  *  align_and_translate.py - Takes in a file of nucleotide sequences, translates, aligns, and returns both a nucleotide and protein alignment. Outputs nucleotide.fasta, protein.fasta
  *  get_unique_records.py - Takes in a FASTA of DNA sequences and removes duplicate
  *  getidentifiers.py - Takes in a FASTA of sequences and lists all record IDs
  *  getpassage.py - Takes in a FASTA of sequences with header format "PASSAGE_HISTORY_|_STRAIN_ID" and lists all passage IDs
  *  timesort.py - Takes in a FASTA of sequences and sorts them into new FASTA files by year
  *  lengthdetermine.py - Determines number of records in shortest of input FASTA files.
  *  formattingparser.py - Takes in FASTA, gets ORFS, and exclude sequences with insertions or deletions, and standardizes record ID formats.
  *  passageparser.py - Takes in FASTA of sequences, and sorts them into new FASTAs by their passage history.
  *  processtrees.sh - Takes in Newick format .tree file and corresponding FASTA file, removes pipe character from record IDs.  Starts SLACrun.sh.
  *  SLACrun.sh - Organizes files into /SLAC folder.  Starts run_dNdS.bash for fulltree, internal branches, and tips conditions. Renames and moves sites.dat file output by HYPHYMP to /rate_measurement_data. 
  *  randomdraw.py - Takes up to three random samples (without replacement) of sequences from each input FASTA file. 
  *  remove_sequences.py - This script takes a text file of identifiers-to-remove, removes them from the original FASTA, and saves a FASTA of the sequences which were removed
  *  sort_conditions.sh X Y- For condition X, this script pulls appropriate FASTAs files, add in an outgroup, and starts FastTree.  Y is either "samp" or "complete", without quotes, depending on whether a random draw is performed in the condition.

  *  start_SLAC.sh X - For condition X, this script starts processtree.sh (SLAC analysis), and adds output to slac_output.csv
  *  consolidate.py - Takes all dN columns from .dat SLAC output files in in rate_measurements, as well as "numbering_table.csv" from Meyer and Wilke, 2015, and combines them into slac_output.csv
  * run_dNdS.bash - Script to automate SLAC analysis 

**/condition_parameters:**
  *  parameters_allsequences.sh - Take every FASTA from fastas/tenyear_passage_divided_fastas/
  *  parameters_eggmatched20052015.sh - Take every FASTA from fastas/tenyear_passage_divided_fastas/ and randomly draw up to three groups of sequences from each passage type, size matched to the FASTA with the fewest number of records. 

  *  parameters_monkeymatched20052015.sh - Take monkey, cell, unpassaged, and pooled FASTAs from fastas/tenyear_passage_divided_fastas/ and randomly draw up to three groups of sequences from each passage type, size matched to the FASTA with the fewest number of records. 

  *  parameters_siatmatched20052015.sh - Take FASTAs from passage groups nonsiat, siat and unpassaged from fastas/tenyear_passage_divided_fastas/ from 2005-2015 and randomly draw up to three groups of sequences from each passage type, size matched to the FASTA with the fewest number of records.

  *  parameters_unpassagedmatched20052015.sh - Take FASTAs from passage groups nonsiat and unpassaged from fastas/tenyear_passage_divided_fastas/ from 2005-2015 and randomly draw up to three groups of sequences from each passage type, size matched to the FASTA with the fewest number of records.

  *  parameters_unpassagedmatched2014.sh - Take FASTAs from passage groups siat, nonsiat, and unpassaged from fastas/passage_and_year_divided_fastas/ from 2014 and randomly draw up to three groups of sequences from each passage type, size matched to the FASTA with the fewest number of records.
 


**/structure_measurements:**
This folder contains scripts and datafiles for generating structural measurements. Output from this analysis is prestored in **/data_analysis**

  *  distances.py - Creates a file of measurements from each amino acid in a protein structure to every other amino acid.  Each line in the output distance.dat contains measurements from one amino acid as reference point
**/structure_mapping** - Storage for files for structural measurements and mapping
  *  translate_align_mapping.py - for aligning sites with structure. outputs structure_map.txt
  *  2YP7H3N2.pdb - Raw structure from the Protein Data Bank.
  *  2YP7clean.pdb - Modifed structure compatible for structure painting (see above)
  *  structure_map.txt - for aligning sites with structure
  *  distances.dat - Distances from every site in 2YP7clean to every other site
