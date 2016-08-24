cd fastas/

for f in complete*
do 
   cat outgroup $f > outgroup${f##complete}
done










