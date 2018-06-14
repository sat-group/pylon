import sys
import subprocess
#
#TO-DO:
"""
  - read 81 length string that rep sudoku
  - write constraint file
  - call jar file and solve it
  - read solution
  - show inital board and solved board
"""
def cntGivens(size,line):
  cnt = 0
  for i in range(size**4):
    if(line[i] != '0'):
      cnt += 1
  return cnt

def index2Coord(size, i):
  z = math.ceil((i / (size**4)))
  i = i - (z-1)*(size**4)
  y = i % (size**2)
  if(y == 0):
      y = 9
  x = math.ceil(i / size**2)
  return (x,y,z)

def coord2Index(size, x,y,z):
  return ((x-1)*((size)**2)+y)+(z*((size)**4))



class Sudoku(object):

  def __init__(self, size, origin):
    self.size = size
    self.origin = origin
    self.sol = origin
    self.givens = cntGivens(size,origin)
    self.f = open("sat.cnf","w")
    self.l = 0

  def genHeader(self):
    s = "p cnf %d \n"%(size**6)
    # how to add line count at end?
    self.f.write(s)

  def genGivenConstr(self):
    i = 0
    for c in self.origin:
      if(c != '0'): 
        self.l += 1
        #calculate x/row
        x = (i // 9) + 1
        #calculate y/col
        y = (i % 9) + 1
        z = int(c)
        self.f.write("%d 0\n" % (index2Coord(self.size, (x,y,z)))




def genCNF(sudoku,given):
  #11988 clauses plus given
  #constraint for givens
  f = open("sat.cnf","w")
  s = "p cnf 729 "
  s += str(11988+given)
  f.write("p cnf 729 %d\n" % (11988+given))
  # Ruben: You should start at index 0 and go until index 81
  for i in range(0, 81):
    # Ruben: why is this check being done?
    # Ruben: if the sudoku[i] stores the values of sudoku these will be between 0 and 9
    if(sudoku[i] != '0'): 
      #calculate x/row
      x = (i // 9)
      #calculate y/col
      y = (i % 9) + 1
      z = int(sudoku[i]) - 1
      # Ruben: if the value of the sudoku is 0 then we do not want to enforce any constraint
      f.write("%d 0\n" % ((x*9+y)+(z*81)))
  #at most once
  for x in range(9):
    for y in range(1,10):
      for z in range(9):
        for i in range(z+1,9):
          f.write("-%d -%d 0\n" % ((x*9+y)+(z*81),(x*9+y)+(i*81)))
  #each number at least once in each row
  for y in range(1,10):
    for z in range(9):
      c = ""
      for x in range(9):
        c += str((x*9+y)+(z*81))
        c += " "
      c += "0\n"
      f.write(c)
  #each number at least once in each column
  for x in range(9):
    for z in range(9):
      c = ""
      for y in range(1,10):
        c += str((x*9+y)+(z*81))
        c += " "
      c += "0\n"
      f.write(c)
  #each number at least once in each 3x3 sub-grid
  f.write("c\n")
  for z in range(9):
    for i in range(2):
      for j in range(2):
        c = ""
        for x in range(1,4):
          for y in range(1,4):
            X = 3*i+x
            Y = 3*j+y
            c += str((x*9+y)+(z*81))
            c += " "
        c += "0\n"
        f.write(c)

  # Ruben: changed the name of the directory
  subprocess.call(['java', '-jar', 'jars/org.sat4j.core.jar','sat.cnf'])

  return

#def solve(sudoku):
#  return


#from https://stackoverflow.com/questions/37952851/formating-sudoku-grids-python-3
def print_sudoku(board):
    print("-"*37)
    for i, row in enumerate(board):
      print(("|" + " {}   {}   {} |"*3).format(*[x if x != 0 else " " for x in row]))
      if i == 8:
        print("-"*37)
      elif i % 3 == 2:
        print("|" + "---+"*8 + "---|")
      else:
        print("|" + "   +"*8 + "   |")

def main():
  pathToBoard = sys.argv[1]
  f = open(pathToBoard,'r')
  for line in f.readlines():
    #TO-DO: implement generic size
    s = Sudoku(3,line)
    s.genGivenConstr()
    """
    #print original
    b = []
    givens = cntGivens(line)
    for i in range(9):
     b.append(list(line[9*i:9*(i+1)]))
    print_sudoku(b)

    #solve ith sudoku
    genCNF(line, givens)
  #print solution
  """





if __name__ == '__main__':
    main()