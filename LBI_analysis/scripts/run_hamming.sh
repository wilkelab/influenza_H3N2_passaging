



python scripts/hamming.py unpassaged_all_2015_rankseq/ancestral_sequences.fasta clairefastas/samp_unpassaged_249a_2014.fasta unpassaged_249a_2014_rankseq/sequence_ranking_terminals.txt unpassaged2014unpassaged2015.txt

sort -nk1 unpassaged2014unpassaged2015.txt > tmp
mv tmp unpassaged2014unpassaged2015.txt


python scripts/hamming.py unpassaged_all_2015_rankseq/ancestral_sequences.fasta clairefastas/samp_nonsiat_249a_2014.fasta nonsiat_249a_2014_rankseq/sequence_ranking_terminals.txt nonsiat2014unpassaged2015.txt

sort -nk1 nonsiat2014unpassaged2015.txt > tmp
mv tmp nonsiat2014unpassaged2015.txt

python scripts/hamming.py unpassaged_all_2015_rankseq/ancestral_sequences.fasta clairefastas/samp_siat_249a_2014.fasta siat_249a_2014_rankseq/sequence_ranking_terminals.txt siat2014unpassaged2015.txt
sort -nk1 siat2014unpassaged2015.txt > tmp
mv tmp siat2014unpassaged2015.txt

