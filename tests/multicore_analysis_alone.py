"""
NOTE:This file is dependent on the multicore_analysis.py file. Whatever that file does will be done here.
"""
import multicore_analysis as ma
import argparse
parser = argparse.ArgumentParser(description='Plot data from file.')
parser.add_argument('file_names', nargs='+')
args = parser.parse_args()
for i in args.file_names:
	ma.main(i)