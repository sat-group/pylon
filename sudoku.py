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
    if(sudoku[i] != 81): 
      #calculate x/row
      x = (i // 9)
      #calculate y/col
      y = i % 9
      z = int(sudoku[i])
      # Ruben: if the value of the sudoku is 0 then we do not want to enforce any constraint
      if z != 0:
        f.write("%d 0\n" % (x*9+y+z))
  #at most once
  for x in range(9):
    for y in range(9):
      for z in range(1,10):
        for i in range(z,9):
          f.write("-%d -%d 0\n" % (x*9+y+z,x*9+y+i))
  #each number at least once in each row
  for y in range(9):
    for z in range(1,10):
      c = ""
      for x in range(9):
        c += str(x*9+y+z)
        c += " "
      c += "0\n"
      f.write(c)
  #each number at least once in each column
  for x in range(9):
    for z in range(1,10):
      c = ""
      for y in range(9):
        c += str(x*9+y+z)
        c += " "
      c += "0\n"
      f.write(c)
  #each number at least once in each 3x3 sub-grid
  for z in range(1,10):
    c = ""
    for i in range(3):
      for j in range(3):
        for x in range(3):
          for y in range(3):
            c += str((3*i+x)*9+(3*j+y)+z)
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

def cntGivens(line):
  cnt = 0
  for i in range(81):
    if(line[i] != '0'):
      cnt += 1
  return cnt

def main():
  pathToBoard = sys.argv[1]
  f = open(pathToBoard,'r')
  for line in f.readlines():
    #print original
    b = []
    givens = cntGivens(line)
    for i in range(9):
     b.append(list(line[9*i:9*(i+1)]))
    print_sudoku(b)

    #solve ith sudoku
    genCNF(line, givens)
  #print solution
  





if __name__ == '__main__':
    main()