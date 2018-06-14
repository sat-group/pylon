import pairwise
import binary
import sequential

def printEncoding(cnf):
	print(cnf)

def main():
	#assign things
	vars = input("Enter variables:\n")
	type = input("Enter type:\n")
	if(type == 1):
		printEncoding(pairwise.cnf(vars))
	elif(type == 2):
		printEncoding(binary.cnf(vars))
	elif(type == 3):
		printEncoding(sequential.cnf(vars))

if __name__ == '__main__':
    main()