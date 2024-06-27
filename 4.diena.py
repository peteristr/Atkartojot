import random

# number = random.randint(1,100)
# print(number)
#
# random_float = random.random()
# print(random_float)
#
# #random float can bi from 0.0000-0.999999
# random_float = random.random()
# print(random_float)
#
# love_score = random.randint(1, 100)
# print(f"Your love score ir {love_score}")

# You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
#
# Important, the first letter should be capitalised and spelt exactly like in the example e.g. "Heads", not "heads".
#
# There are many ways of doing this. But to practice what we learnt in the last lesson, you should generate a random number,
# either 0 or 1. Then use that number to print out "Heads" or "Tails".
#
# e.g. 1 means Heads 0 means Tails
#
# Example Output
# Heads
# or
#
# Tails

# Heads = 0
# Tails = 1
#
# random_h_t = random.randint(0,1)
# print(random_h_t)
#
# game = int(input("Heads or tails? Type 0 or 1 "))
# # game_to_int = int(game)
# print(type(game))
# if game == 0 and game == random_h_t or game == 1 and game == random_h_t:
#     print(f"You win {random_h_t}")
# elif game == 0 and game != random_h_t:
#     print(f"You lose {random_h_t}")
# # elif game == 1 and game == random_h_t:
# #     print(f"You win {random_h_t}")
# else:
#     print(f"You lose {random_h_t}")

#______________________________________________________
#TODO - 1 - Ceturtā diena head or tails (if, ==, if and or, random)

#Lists
# cipari = [1,2,3]
# print(cipari[-1]) #izpintē pēdējo no sarkasta
#
# cipari[2] = 4 #aizvieto pēdējo jeb trijnieku (2 jo 0,1,2) ar jaunu skaitli
# print(cipari)
#
# cipari.append(5) #ievieto ar .apend funkciju saraksta beigās
# print(cipari)
#
# cipari.extend([0,8,99]) #extend izmanto lai pieiktu sarakstu galā
# print(cipari)

#______________________________________________________

# You are going to write a program that will select a random name from a list of names.
# The person selected will have to pay for everybody's food bill.
# Important: You are not allowed to use the choice() function.
#
# NOTE: In this exercise, you are working collaboratively with another programmer.
# They already dealt with input() and writing the code needed to get hold of the names in the
# input area, so you don't need to worry about that.
#
# The other programmer has written the code to separate the names in the input area into individual names and
# puts them inside a List called names. For their code to work correctly, you must enter all the names in the
# input area followed by comma then space. e.g. name, name, name
#
# You can try printing names to see what it looks like (but remember to remove that code when you submit the assignment).
# Assume that names works like this:
#
# input area: x, y, z,
# names = ["x", "y", "z"]
# Example Input
# Angela, Ben, Jenny, Michael, Chloe
# Note: notice that there is a space between the comma and the next name.
#
# Example Output
# Michael is going to buy the meal today!
# Hints
# You might need the help of the len() function. https://stackoverflow.com/questions/1712227/how-do-i-get-the-number-of-elements-in-a-list
#
# Remember that Lists start at index 0!

# #
# payers_list = ['Angela', 'Ben', 'Jenny', 'Michael', 'Chloe']
# random_payer = random.choice(payers_list)
# print(f"{random_payer} is going to buy the meal today! ")
# TODO - 2 - Ceturtā diena random bill player (random.choose from list) arī lietas par to kā papilidnāt list [] aizvietot, parādīt
#______________________________________________________
