def cnf(n):
	header = "p cnf %d "%(n)
	clauses = (n - 1)* n / 2
	header += str(clauses)
	header += "\n"
	cnf = ""
	for i in range(1,n):
		for j in range(i+1,n+1):
			cnf += "-%d -%d 0\n"%(i,j)
	cnf = header + cnf
	return cnf
