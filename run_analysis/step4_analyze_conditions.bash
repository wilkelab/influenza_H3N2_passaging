#Automate conditions for running HyPhyMP analysis 
#on rooted trees and nucleotide FASTAs
#First arguments to start_SLAC.sh require a matching file in condition_parameters/
#
#conditions which include a random draw require "samp" as a second argument
#conditions which do not include random draw require "complete" as a second argument
#conditions from one year have div ans second argument
#CDM 1/15/16
cd ~/influenza_passaging_effects/scripts

#bash start_SLAC.sh eggmatched20052015 samp
#bash start_SLAC.sh siatmatched20052015 samp
#bash start_SLAC.sh monkeymatched20052015 samp
#bash start_SLAC.sh unpassagedmatched20052015 samp
#bash start_SLAC.sh unpassagedmatched2014 samp
#bash start_SLAC.sh allsequences20052015 complete
#bash start_SLAC.sh allsequencesSingleyears complete
#bash start_SLAC.sh singleserial20052015 samp
bash start_SLAC.sh randomsamples20052015 samp 
