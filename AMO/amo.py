#!/usr/bin/python

import sys

class AMO(object):

  def binary(a, b):
    clause=str(a) + " " + str(b)
    return clause

  def ternary(a, b, c):
    clause=str(a) + " " + str(b) + " " + str(c)
    return clause    

  def quaternary(a, b, c, e):
    clause=str(a) + " " + str(b) + " " + str(c) + " " + str(e)
    return clause   

  def printFormula(formula, variables, clauses):
    print "p cnf " + str(variables) + " " + str(clauses)
    for f in formula:
      print f

  def encoding(type):
    if type == "Pairwise":
      return Pairwise()
    if type == "Sequential":
      return Sequential()
    assert 0, "Invalid encoding: " + type
 
  encoding = staticmethod(encoding)
  binary = staticmethod(binary)
  printFormula = staticmethod(printFormula)
 
class Pairwise(AMO):
  def build(self, n): 
    print("c Pairwise encoding with n=" + str(n))
    formula = []
    variables = n
    clauses = 0

    for x in range(1,n+1):
      for y in range(x+1,n+1):
        formula.append(AMO.binary(-x,-y))
        clauses += 1

    AMO.printFormula(formula, variables, clauses)
 
class Sequential(AMO):
  def build(self, n): 
    print("c Sequential encoding with n=" + str(n))
 
#obj = AMO.encoding("Sequential")

obj = AMO.encoding(sys.argv[1])
obj.build(int(sys.argv[2]))
