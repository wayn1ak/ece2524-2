#!/usr/bin/env python

import re
import fileinput

def change_grade(arg_array):

	comments=""
	values=""

	if len(arg_array) != 3:
		comments="Usage: change_grade.py STRING VALUE\n"
		return(values, comments)
		exit(1)

	for line in fileinput.input('-'):
		m = re.search(arg_array[1], line)
		values = line.rstrip().split(',')
		if m:
			values[3] = arg_array[2]
		print ",".join(values)
	return(values, comments)	

if __name__=='__main__':
	from sys import stderr,stdout,argv,exit

	(values, comments) = change_grade(argv)
	stderr.write(comments)
