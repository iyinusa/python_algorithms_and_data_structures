'''
A prison can be represented as a list of cells. Each cell contains exactly one prisoner. A 1 represents an unlocked cell and a 0 represents a locked cell. 

`[1, 1, 0, 0, 0, 1, 0]`

Starting inside the leftmost cell, you are tasked with seeing how many prisoners you can set free, with a catch. Each time you free a prisoner, the locked cells become unlocked, and the unlocked cells become locked again. You can only move from left to right and not go back. 

So, if we use the example above: 

[1, 1, 0, 0, 0, 1, 0]
# You free the prisoner in the 1st cell
# The locked cells 3rd, 4th, 5th and 7th become unlocked and the unlocked cells 1st, 2nd and 6th become locked

[0, 0, 1, 1, 1, 0, 1] 
# You free the prisoner in the 3rd cell (2nd one locked).
# The locked cell 1st, 2nd and 6th become unlocked and the unlocked cells 3rd, 4th, 5th and 7th become locked

[1, 1, 0, 0, 0, 1, 0]
# You free the prisoner in the 6th cell (3rd, 4th and 5th locked).
# The locked cells 3rd, 4th, 5th and 7th become unlocked and the unlocked cells 1st, 2nd and 6th become locked

[0, 0, 1, 1, 1, 0, 1]
# You free the prisoner in the 7th cell - and you are done!

Here, we have set free 4 prisoners in total.
Create a program that, given this unique prison arrangement, returns the number of freed prisoners.

Examples:
---------
freed_prisoners([1, 1, 0, 0, 0, 1, 0]) ➞ 4
freed_prisoners([1, 1, 1]) ➞ 1
freed_prisoners([0, 0, 0]) ➞ 0
freed_prisoners([0, 1, 1, 1]) ➞ 1

NOTE:

    You must free a prisoner in order for the locks to switch. So in the second example where the input is [1, 1, 1] after you release the first prisoner, the locks change to [0, 0, 0]. Since all cells are locked, you can release no more prisoners.
    You always start within the leftmost element in the list (the first prison cell). If all the prison cells to your right are zeroes, you cannot free any more prisoners.

'''

# Break prisoners out of a unique prison using lists, logic, and loops

prisoner = 0 # Store number of freed prisoners
cells = [1, 1, 0, 0, 0, 1, 0] # Cells

for i in range(0, len(cells)):
  # check and free prisoner
  if(cells[i] == 1):
    prisoner += 1;
    
    # unlock and re-lock cells
    for j in range(0, len(cells)):
      if(cells[j] == 0):
        cells[j] = 1
      else: 
        cells[j] = 0
    
    # Output cells states each time prisoner is freed    
    print(cells)
    
print("\nTotal Freed Prisoners: " + str(prisoner))