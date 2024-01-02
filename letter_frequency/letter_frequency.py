'''
Frequency analysis is the study of the frequency of letters or combination of letters in encrypted text. Frequency analysis is based on the fact that in a particular language, certain letters, and groups of letters, appear with essentially the same frequency in almost all text. For example 'A' is a relatively common letter in the English language while 'Z' is less common.

Remember that a list is an ordered sequence of elements that can be modified or changed. Each element inside of a list is called an item. Lists enable you to keep similar data together, condense your code, and perform the same methods and operations on multiple values at once. In Python, lists are created by placing items, separated by commas, between square brackets []. Lists work similarly to strings; you use square brackets [] to access data and the first element has an index of 0. The values or items in a list can be strings, integers, floats, other lists or a mix of different types.
'''

word = "This is the sample given string"

# Convert letter to lowercase
word.lower()

# Alphabet list
alphabet = ["a","b","c","d","e","f","g","h","i","i","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

# iterate and count
for i in range(0, 25):
  # Store frequency of letter
  count = word.count(alphabet[i])
  
  # Output letter and occurance
  print(alphabet[i] + " : " + str(count))