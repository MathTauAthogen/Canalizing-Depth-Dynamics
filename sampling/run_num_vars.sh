#! /bin/bash
for i in `seq 0 $1`;
do
  /usr/local/bin/python2.7 sample_dds.py $2 50 $1 $i
done
