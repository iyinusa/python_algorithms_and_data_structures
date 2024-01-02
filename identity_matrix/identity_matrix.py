'''
An identity matrix is defined as a square matrix with 1's running from the top left of the square to the bottom right. The rest are 0's. The identity matrix has applications ranging from machine learning to the general theory of relativity. 

Identity Matrix:
-----------------
Input :  4
Output : 1 0 0 0
         0 1 0 0
         0 0 1 0
         0 0 0 1

Mirror Identity Matrix:
----------------------
Input :  4
Output : 0 0 0 1
         0 0 1 0
         0 1 0 0
         1 0 0 0
'''

# Using smart logic, loops, and algorithms to output the mirror image of an identity matrix

print("\nMirror image of an identity matrix\n")

size = int(input("Input matrix size: "))

# Create matrix
for row in range(0, size):
  for col in range(0, size):
    # Mirror image of identity matrix occurs when the sum of the row and column is equal matrix index size
    if((row + col) == (size-1)):
      print("1 ", end = " ")
    else:
      print("0 ", end = " ")
  print("\n")