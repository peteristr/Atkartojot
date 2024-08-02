import random

import pls

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

# names = ('Angela', 'Ben', 'Jenny', 'Michael', 'Chloe')
# import random
# #Get the total number of items in list
# num_items = len(names)
# #Ganerate random numbers between 0 and the last index.
# random_choise = random.randint(0, num_items -1)
# #Choose and print a random name.
# print(names[random_choise])
# print(names[4])
# print(names[num_items - 1])
# TODO - 3 - Ceturtā diena random name (random.choose from list) arī lietas par to kā papilidnāt list [] aizvietot, parādīt
#______________________________________________________
# names = ['Angela', 'Ben', 'Jenny', 'Michael', 'Chloe']
# last_names = ['Ops', 'Bsdfg', 'Opsse', 'Uptom', 'Kolton']
# kopejs_vards = [names, last_names] #nested lists
# print(kopejs_vards)
# #https://app.auditorium.ai/lesson/eelyNMYJKXeNJAbjssSEQz0m88XvnhX6/e806e25c-5f84-4d7c-9c7c-2c0fcd0bfe84?sl=8313e98d-83c7-40af-a89e-91e364990f7c&st=efd8a0a4-7734-42d7-9b08-294517bd6a6a
# line1 = ['[]', '[]', '[]']
# line2 = ['[]', '[]', '[]']
# line3 = ['[]', '[]', '[]']
#
# map = [line1, line2, line3]
# print("Hiding your treasure@ X mark the spot.")
# position = input() #Where do you wnat to put the treasure?
# #Jāiezīmē B3 kas ir otrajā kolonā  otrais un 3 rinda
# letter = position[0].lower()
# abc = ['a','b','c']
# letter_index = abc.index(letter) #prieš input salīdzināšanas
# # priekš numura norādīšnas
# #ja input ir B, tad index ir jābūt
# number_index = int(position[1]) - 1
# map[number_index][letter_index] = "x"
#
# print(f"{line1}\n {line2}\n {line3}")
# TODO - 4 - Ceturtā diena Hiding treasure with x (choose from list) arī lietas par to kā papilidnāt list [] aizvietot, parādīt
#______________________________________________________
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


import random
choise = [rock, paper, scissors]
num_items = len(choise)
random_choise = random.randint(0, 2)
players_choose = int(input(f"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(choise[players_choose])
game_on = True
if random_choise == players_choose:
    print("Draw")
    # print(f"UZVARĒJA {random_choise} vs {players_choose}")
elif random_choise < players_choose and players_choose !=0:
    # print(f"UZVERĒJA {random_choise} vs {players_choose}")
    print("You win")
    game_on = False
else:
    # print(f"UZVERĒJA {random_choise} vs {players_choose}")
    print("LOST")
    game_on = False

print(choise[random_choise]) #no saraksta paņem random izvēlni

# TODO - 5 - Ceturtā diena Rock paper scisors (if, list,) arī lietas par to kā papilidnāt list [] aizvietot, parādīt
#______________________