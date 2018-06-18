#!/usr/bin/python

import sys, subprocess, amo, os

encodings = ['Pairwise','Sequential','Binary','Commander']
if sys.argv[1] not in encodings:
	print "Invalid encoding=",sys.argv[1]
	sys.exit(0)

for f in range(2,21):
	print "Testing at-most-one with n=",f
	file = open("sat.cnf","w")
	file.write(amo.build(sys.argv[1], f))
	file.close()
	subprocess.call(['java', '-jar', 'amo-checker.jar','sat.cnf',str(f)])

os.remove("sat.cnf")
