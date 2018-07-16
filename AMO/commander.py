import math

def calcCommander(n):
      if(n <= 3): return 1
      l = math.floor(n / 2)
      r = math.ceil(n / 2)
      while(l > 3 or r > 3):
        leftAcc = calcCommander(l)
        rightAcc = calcCommander(r)
        return leftAcc+rightAcc

 
	