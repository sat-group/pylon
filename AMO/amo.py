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
    if type == "Bimander":
      return Bimander()
    assert 0, "Invalid encoding: " + type
 
  encoding = staticmethod(encoding)
  binary = staticmethod(binary)
  ternary = staticmethod(ternary)
  quaternary = staticmethod(quaternary)
  toString = staticmethod(toString)
 
class Pairwise(AMO):
  def build(self, formula,variables,lo,hi): 
    formula = []

    for x in range(lo,hi+1):
      for y in range(x+1,hi+1):
        formula.append(AMO.binary(-x,-y))

    return formula,variables
 
class Sequential(AMO):
  def build(self, formula,variables,lo,hi): 
    formula = []
    variables += variables - 1

    for i in range(lo,hi):
      formula.append(AMO.binary(-i,hi+i))
      #cnf += "-%d %d 0\n"%(i,n+i)
      if(i > 1):
        formula.append(AMO.binary(-(hi+i-1),hi+i))
        formula.append(AMO.binary(-i,-(hi+i-1)))
        # cnf += "-%d %d 0\n"%(n+i-1,n+i)
        # cnf += "-%d -%d 0\n"%(i,n+i-1)
    formula.append(AMO.binary(-hi,-(2*hi-1)))
    #cnf += "-%d -%d 0\n"%(n,2*n-1)
    return formula, variables

class Binary(AMO):
  def build(self, formula,variables,lo,hi):
    formula = []
    log = int(math.ceil(math.log(hi,2)))#auxilary
    variables += log

    for aux in range(1,log+1):
      for i in range(lo,hi+1):
        if(((i-1) % (2**aux)) < (2**(aux-1))):
          formula.append(AMO.binary(-i,hi+aux))
          # cnf += "-%d %d 0\n"%(i,n+aux)
        else:
          formula.append(AMO.binary(-i,-(hi+aux)))
          # cnf += "-%d -%d 0\n"%(i,n+aux)
    return (formula, variables)

class Commander(AMO):
  def build(self, formula,variables,lo,hi):
    def calcCommander(n):
      if(n <= 3): return 1
      l = math.floor(n / 2)
      r = math.ceil(n / 2)
      leftAcc = calcCommander(l)
      rightAcc = calcCommander(r)
      return leftAcc+rightAcc
      
    def genSubOrds(lo,hi,cnt):
      v = hi - lo + 1
      threeCount = v - (cnt * 2)
      twoCount = cnt - threeCount
      l = []
      x = lo
      for i in range(twoCount):
        l.append((x,2))
        x += 2
      for i in range(threeCount):
        l.append((x,3))
        x += 3
      return l

    comVar = int(calcCommander(hi-lo+1))
    comStart = variables + 1
    variables += comVar
    subOrds = genSubOrds(lo,hi,comVar)

    c = hi+1
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
    if (comVar > 2):
      return self.build(formula,variables,comStart,comStart+comVar);
    
    formula.append(AMO.binary(-comStart, -comStart+1));
    return (formula,variables)
    # exactly on of c true
    # TO-DO implement recursive instead of pairwise
    """
    for x in range(hi+1,hi+comVar+1):
      for y in range(hi+1,hi+comVar+1):
        formula.append(AMO.binary(-x,-y))
    


    return (formula, variables)
    """  

class Product(AMO):
  def build(self, formula,variables,lo,hi):
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
    return (formula, variables)

class Bimander(AMO):
  def build(self, formula,variables,lo,hi):

    def binRep(num,size):
      b = bin(num)[2:]
      return (size-len(b))*'0' + b


    n = hi - lo +1
    m = int(math.ceil(math.sqrt(n)))
    log = int(math.ceil(math.log(m,2)))#auxilary
    variables = n + log

    B = (n // m)
    # A = B + 1
    sizeA = int(math.floor(n/(B+1)))
    sizeB = m - sizeA
    

    # make groups
    l = []
    x = lo
    for i in range(sizeA):
      l.append((x,B+1))
      x += B+1
    for i in range(sizeB):
      l.append((x,B))
      x += B
    maxLen = len(bin(m)[2:])
    g = 0
    for s in l:
      b = binRep(g,maxLen)
      # at most one variable in group true
      (start,size) = s # inclusive start
      end = start+size # exclusive end
      for x in range(start,end):
        for y in range(maxLen-1,-1,-1):
          if(b[y] == '0'):
            formula.append(AMO.binary(-x,-(hi+y+1)))
          else: # val is 1
              formula.append(AMO.binary(-x,hi+y+1))
      g += 1

    return formula,variables


 
def build(encoding, n):
  obj = AMO.encoding(encoding)
  formula, variables = obj.build([],n,1,int(n))
  return AMO.toString(formula,variables)

def main():
  obj = AMO.encoding(sys.argv[1])
  formula, variables = obj.build([],int(sys.argv[2]),1,int(sys.argv[2]))
  print AMO.toString(formula,variables)

if __name__ == '__main__':
    if len(sys.argv) != 3:
      print "Wrong number of arguments: ",len(sys.argv)
    else:
      main()
