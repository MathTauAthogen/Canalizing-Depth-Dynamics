#Order of passing is $1=number of DDSes, $2=number of cores, $3=number of variables and $4=canalyzing depth.
python threading_python_multicore.py $1 $2 $3 $4
python multicore_analysis.py $3 $4 $2 $1