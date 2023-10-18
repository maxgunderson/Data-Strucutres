import sys # for sys.argv, command-line arguments
from Stack import Stack

# Returns True if the delimiters (), [], and {} are balanced and False otherwise.
# Executed using the command: python Delimiter_Check.py file_to_check.py

def delimiter_check(filename):
  file = open(filename, 'r')
  stack = Stack()
  for i in file:
    if i in "()[]{}":
     if (stack.peek() == '(' and i == ')') or (stack.peek() == '[' and i == ']') or (stack.peek() == '{' and i == '}'):
       stack.pop() 
     else:
       stack.push(i)
  return len(stack) == 0

if __name__ == '__main__':

  if len(sys.argv) < 2:
    print('Usage: python Delimiter_Check.py file_to_check.py')
  else:
    if delimiter_check(sys.argv[1]):
      print('The file contains balanced delimiters.')
    else:
      print('The file contains IMBALANCED DELIMITERS.')


