'''
Creating a program that represents the movements of the line for the lady's bathroom. To begin, create a list that represents the line. It must contain the five names of the women initially waiting (you can make these up).

The following events occur, and you must represent them in the list and print the list out after each action.

    A woman named Jenny arrives who only wanted to check her lipstick, she asks to join the front of the line, and all the women let her.
    The woman third in line’s phone started ringing, and she left the line to answer.
    A new woman named Alice joined the line.

'''

# initial women on the line
women = ["Amo", "Carl", "Angela", "Flora", "Kelly"]
print("\nInitial women on the line:")
print(women)

# Jenny joins the front line
women.insert(0, "Jenny")
print("\nWhen Jenny joins:")
print(women)

# Third woman left on phone call
women.pop(2)
print("\nWhen third woman left:")
print(women)

# Alice joins the line
women.append("Alice")
print("\nWhen Alice join the line:")
print(women)