#Order of passing is $1=number of DDSes, $2=number of cores, $3=number of variables and $4=canalyzing depth.
seq $1 | parallel -n 0 -j $2 "python multicore.py $3 $4 $2 $1"
python multicore_analysis.py $3 $4 $2 $1