#!/usr/bin/python

import sys, subprocess, amo, os

<<<<<<< HEAD
encodings = ['Pairwise','Sequential','Binary','Commander','Product','Bimander','Totalizer','Ladder','ModelBased']
=======
encodings = ['Pairwise','Sequential','Binary','Commander','Bimander','ModelBased','Product']
>>>>>>> ef3da1251e49e04094f9a7e043f06bb04e524826
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
