import math

def cnf(n):
	header = "p cnf %d "%(2*n-1)
	clauses = n*3-4
	header += str(clauses)
	header += "\n"
	cnf = ""
	for i in range(1,n):
		cnf += "-%d %d 0\n"%(i,n+i)
		if(i > 1):
			cnf += "-%d %d 0\n"%(n+i-1,n+i)
			cnf += "-%d -%d 0\n"%(i,n+i-1)
	cnf += "-%d -%d 0\n"%(n,2*n-1)
	cnf = header + cnf
	return cnf