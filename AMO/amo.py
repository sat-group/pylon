#!/usr/bin/python

import sys

class AMO(object):

  def binary(a, b):
    clause=str(a) + " " + str(b) + " 0"
    return clause

  def ternary(a, b, c):
    clause=str(a) + " " + str(b) + " " + str(c) + " 0"
    return clause    

  def quaternary(a, b, c, e):
    clause=str(a) + " " + str(b) + " " + str(c) + " " + str(e) + " 0"
    return clause   

  def toString(formula, variables):
    res = ""
    res += "p cnf " + str(variables) + " " + str(len(formula)) + "\n"
    #assert int(clauses) == len(formula), "Number of clauses does not match. Expected: " + str(len(formula)) + " Header: " + str(clauses)  
    for f in formula:
      res += f + "\n"
    return res

  def encoding(type):
    if type == "Pairwise":
      return Pairwise()
    if type == "Sequential":
      return Sequential()
    assert 0, "Invalid encoding: " + type
 
  encoding = staticmethod(encoding)
  binary = staticmethod(binary)
  toString = staticmethod(toString)
 
class Pairwise(AMO):
  def build(self, n): 
    formula = []
    variables = n

    for x in range(1,n+1):
      for y in range(x+1,n+1):
        formula.append(AMO.binary(-x,-y))

    return AMO.toString(formula, variables)
 
class Sequential(AMO):
  def build(self, n): 
    formula = []
    variables = 2*n-1

    for i in range(1,n):
      formula.append(AMO.binary(-i,n+i))
      #cnf += "-%d %d 0\n"%(i,n+i)
      if(i > 1):
        formula.append(AMO.binary(-(n+i-1),n+i))
        formula.append(AMO.binary(-i,-(n+i-1)))
        # cnf += "-%d %d 0\n"%(n+i-1,n+i)
        # cnf += "-%d -%d 0\n"%(i,n+i-1)
    formula.append(AMO.binary(-n,-(2*n-1)))
    #cnf += "-%d -%d 0\n"%(n,2*n-1)
    return AMO.toString(formula, variables)
 
def build(encoding, n):
  obj = AMO.encoding(encoding)
  return obj.build(int(n))

def main():
  obj = AMO.encoding(sys.argv[1])
  print obj.build(int(sys.argv[2]))

if __name__ == '__main__':
    if len(sys.argv) != 3:
      print "Wrong number of arguments: ",len(sys.argv)
    else:
      main()
