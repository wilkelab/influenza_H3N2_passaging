location=`pwd`
echo $location
sed "s|change_path|$location|g" automate_slac_temp.bf > automate_slac.bf

HYPHYMP automate_slac.bf
