#!/usr/bin/python

import sys
import math

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
    if type == "Binary":
      return Binary()
    if type == "Commander":
      return Commander()
    if type == "Product":
      return Product()
    assert 0, "Invalid encoding: " + type
 
  encoding = staticmethod(encoding)
  binary = staticmethod(binary)
  ternary = staticmethod(ternary)
  quaternary = staticmethod(quaternary)
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

class Binary(AMO):
  def build(self,n):
    formula = []
    log = int(math.ceil(math.log(n,2)))#auxilary
    variables = n + log

    for aux in range(1,log+1):
      for i in range(1,n+1):
        if(((i-1) % (2**aux)) < (2**(aux-1))):
          formula.append(AMO.binary(-i,n+aux))
          # cnf += "-%d %d 0\n"%(i,n+aux)
        else:
          formula.append(AMO.binary(-i,-(n+aux)))
          # cnf += "-%d -%d 0\n"%(i,n+aux)
    return AMO.toString(formula, variables)

class Commander(AMO):
  def build(self, n):
    formula = []
    def calcCommander(n):
      if(n <= 3): return 1
      l = math.floor(n / 2)
      r = math.ceil(n / 2)
      leftAcc = calcCommander(l)
      rightAcc = calcCommander(r)
      return leftAcc+rightAcc
      
    def genSubOrds(n,cnt):
      threeCount = n - (cnt * 2)
      twoCount = cnt - threeCount
      l = []
      x = 1
      for i in range(twoCount):
        l.append((x,2))
        x += 2
      for i in range(threeCount):
        l.append((x,3))
        x += 3
      return l

    comVar = int(calcCommander(n))
    variables = int(n) + comVar
    subOrds = genSubOrds(n,comVar)

    c = n+1
    for s in subOrds:
      # at most one variable in group true
      (start,size) = s # inclusive start
      end = start+size # exclusive end
      # TO-DO change to be able to call pairwise
      for x in range(start,end):
        for y in range(x+1,end):
          formula.append(AMO.binary(-x,-y))

      # if c true then at least one var true
      if(size == 2):
        formula.append(AMO.ternary(-c,start,start+1))
        pass
      else: # size == 3
        formula.append(AMO.quaternary(-c,start,start+1,start+2))

      # if c false then all var false
      for i in range(start,end):
        formula.append(AMO.binary(c,-i))
      c += 1


    # exactly on of c true
    # TO-DO implement recursive instead of pairwise
    for x in range(n+1,n+comVar+1):
      for y in range(x+1,n+comVar+1):
        formula.append(AMO.binary(-x,-y))


    return AMO.toString(formula, variables)

class Product(AMO):
  def build(self, n):
    p = (math.ceil(math.sqrt(n)))
    q = int(math.ceil(n/p))
    p = int(p)
   
    formula = []
    variables = n + p +q
  
    #pairwise p
    for x in range(n+1,n+p+1):
      for y in range(x+1,n+1+p):
        formula.append(AMO.binary(-x,-y))
    #pairwise q
    for x in range(n+p+1,n+p+1+q):
      for y in range(x+1,n+p+1+q):
        formula.append(AMO.binary(-x,-y))
    
    x = 1 
    for u in range(n+1,n+1+p):
      for v in range(n+p+1,n+p+1+q):
        if(x <= n): #account that u*v may be greater than x
           formula.append(AMO.binary(-x,u))
           formula.append(AMO.binary(-x,v))
           x += 1
    return AMO.toString(formula, variables)

class Bimander(AMO)
  def build(self,n):
    m = int(math.ceil(math.sqrt(n)))

    formula = []
    log = int(math.ceil(math.log(m,2)))#auxilary
    variables = n + log

    B = (n // m)
    # A = B + 1
    sizeA = n % (n // m)
    sizeB = m - sizeB

    l = []
    x = 1
    for i in range(sizeA):
      l.append((x,B+1))
      x += B+1
    for i in range(sizeB):
      l.append((x,B))
      x += B

    for s in l:
      # at most one variable in group true
      (start,size) = s # inclusive start
      end = start+size # exclusive end
      # TO-DO change to be able to call pairwise
      for x in range(start,end):
        for y in range(x+1,end):
          formula.append(AMO.binary(-x,-y))


 
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
