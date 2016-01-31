#Automate sorting of FASTAs by conditions 
#Adds in outgroups and creates trees
#First input to sort_conditions requires matching 
#file in condition_parameters
#Conditions using a random sample require "samp" as a second argument
#Conditions without a random sample require "complete" as a second argument
#
#CDM 1/15/16

cd ~/influenza_passaging_effects/scripts

bash sort_conditions.sh eggmatched20052015 samp
bash sort_conditions.sh siatmatched20052015 samp
bash sort_conditions.sh monkeymatched20052015 samp
bash sort_conditions.sh unpassagedmatched20052015 samp
bash sort_conditions.sh unpassagedmatched2014 samp
bash sort_conditions.sh allsequences20052015 complete

