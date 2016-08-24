#Input is a fasta file with outgroup added in

#mkdir rate_measurement_data/

for condition in output/outgroup_*
do

    echo $condition
    outfile=${condition%trunkseqs}
    outfile=${outfile##*/}
    outfile=complete${outfile#outgroup}trunk.dat
    echo $outfile


    #outfile=${condition%.fasta}
    #outfile=${outfile#fastas/}
    python scripts/calc_trunk_dnds.py $condition/trunk_sequences.fasta $outfile
    mv $outfile ../rate_measurement_data

done


echo "_trunk.dat files moved to /rate_measurement_data

cd ../rate_measurement_data

echo "trunk measurements consolidated into slac_output.csv
python ../scripts/consolidate.py
mv ../rate_measurement_data/slac_output.csv ../data_analysis/slac_output.csv

