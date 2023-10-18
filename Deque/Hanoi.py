import timeit
from Stack import Stack

# Computes and prints the Towers of Hanoi game execution 

def Hanoi_rec(n, s, a, d):
  print(n, s, a, d)
  if n == 0: 
    single_value = s.pop()
    d.push(single_value)
  else:
    Hanoi_rec(n-1, s, d, a) 
    value = s.pop()
    d.push(value)
    Hanoi_rec(n-1, a, s, d)
    
  print(n, s, a, d)
  print()

def Hanoi(n):
  source = Stack()
  dest = Stack()
  aux = Stack()
  i = n-1
  while i >= 0:
    source.push(i)
    i = i - 1
  Hanoi_rec(n-1, source, aux, dest)

if __name__ == "__main__":
  n=5
  runtime = timeit.timeit("Hanoi(n)", setup="from __main__ import Hanoi,n", number=1)
  print("computed Hanoi(" + str(n) + ") in " + str(runtime) + " seconds.")