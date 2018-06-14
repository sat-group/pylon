import math

def cnf(n):
	log = int(math.ceil(math.log(n,2)))#auxilary
	header = "p cnf %d "%(n+log)
	clauses = n * log
	header += str(clauses)
	header += "\n"
	cnf = ""
	for aux in range(1,log+1):
		for i in range(1,n+1):
			if(((i-1) % (2**aux)) < (2**(aux-1))):
				cnf += "-%d %d 0\n"%(i,n+aux)
			else:
				cnf += "-%d -%d 0\n"%(i,n+aux)
	cnf = header + cnf
	return cnf

	