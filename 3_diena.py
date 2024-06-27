# print("Welcome to the rollercoastrer!")
# height = int(input("What is your heigt in cm? "))

# bill = 0
# if height >= 120: #tikai ja garums ir virs 120 cm citādi else par mazu
#     print("Garāks par nepieciešamo. ") # ja garāks, tad prasa vecumu
#     vecums = int(input("Cik gadi? "))
#     if vecums >18 : #
#         # print("Jāmaksā ir 12$")
#         bill += 12
#     elif vecums >=12 or vecums == 18:
#         # print("Jāmaksā ir 7$")
#         bill += 7
#     elif vecums < 12:
#         # print("Tev kā bērnam jāmaksā 5$")
#         bill += 5
#     foto = input("Vai vēlieties bildi? Y vai N ")
#     if foto == "Y":
#         bill += 3
#         print(f"Papildus maksa ir 3 $ kopā ar biļeti {bill}")
#     else:
#         print(f"Apmaksājiet rēķinu {bill}")
# else:
#     print("Sorry tu esi par mazu!")

# ja kāds ir zem 18 vai vienāds tad $7
# ja kāds ir virs 18 tad 12$
#TODO - 1 - Tešā diena karuselis
#_____________________________BMI calculator____________
# height = float(input("Lūdzu ievadi garumu metros, piem 1.65. "))
# weight = int(input("Lūdzu ievadi svaru kilogramos, piem 72. "))
#
# BMI = weight/(height ** 2)
#
# print(type(BMI))
# noapaļots = (round(BMI, 2))
# print(f"Tavs svara BMI indeks ir: {noapaļots} %")
#TODO - 2 - Tešā diena karuselis BMI indekss
#_____________________________Leep years (īsais garias vads)____________

# year = 1989
#
# if year % 4 == 0: #dalīt ar 4 un bez atlikuma
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year")
#         else:
#             print("Not Leap year")
#     else:
#         print("Leap year")
#
# else:
#     print("Not Leap year")



# Write a program that works out whether if a given year is a leap year.
# A normal year has 365 days, leap years have 366, with an extra day in February.
# The reason why we have leap years is really fascinating, this video does it more justice.
# This is how you work out whether if a particular year is a leap year.
# on every year that is divisible by 4 with no remainder
# except every year that is evenly divisible by 100 with no remainder
# unless the year is also divisible by 400 with no remainder
# If english is not your first language or if the above logic is confusing, try using this flow chart .
#
# e.g. The year 2000:
# 2000 ÷ 4 = 500 (Leap)
# 2000 ÷ 100 = 20 (Not Leap)
# 2000 ÷ 400 = 5 (Leap!)
# So the year 2000 is a leap year.
#
# But the year 2100 is not a leap year because:
# 2100 ÷ 4 = 525 (Leap)
# 2100 ÷ 100 = 21 (Not Leap)
# 2100 ÷ 400 = 5.25 (Not Leap)
# Warning your output should match the Example Output format exactly, including spelling an punctuation.
#
# Example Input 1
# 2400
# Example Output 1
# Leap year
# Example Input 2
# 1989
# Example Output 2
# Not leap year
#TODO - 3 - Tešā diena pāra nepāra gads
#_________________________________________

# Nosacījumi kuriem visiem jāiestājas:
# if aaa:
#     kaut kas
# if aaa:
#     kaut kas
# if aaa:
#     kaut kas
#
# Nosacījumi, kur kādam jāiestājas:
# if aaa:
#     kaut
#     kas
# elif aaa:
#     kaut
#     kas
# else:
#     kaut
#     kas
#_________________________________________Picas pasūtīšana________________________
# Instructions
# Congratulations, you've got a job at Python Pizza!
# Your first job is to build an automatic pizza order program.
# Based on a user's order, work out their final bill.
#
# Small pizza (S): $15
# Medium pizza (M): $20
# Large pizza (L): $25
#
# Add pepperoni for small pizza (Y or N): +$2
# Add pepperoni for medium or large pizza (Y or N): +$3
# Add extra cheese for any size pizza (Y or N): +$1
#
# Example Input/testēšanas scenārijs
# L
# Y
# N
# Example Output
# Thank you for choosing Python Pizza Deliveries!
# Your final bill is: $28.

# print("Thank you for choosing Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L :  ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
#
#
#
# bill = 0
# if size == "S":
#     bill += 15
#     if add_pepperoni == "Y":
#         bill += 2
#     if extra_cheese == "Y":
#         bill += 1
#         print(f"Thank you for choosing Python Pizza Deliveries! \nYour final bill is: ${bill}.")
#     else:
#         print(f"Thank you for choosing Python Pizza Deliveries! \nYour final bill is: ${bill}.")
# elif size == "M":
#     bill +=20
#     if add_pepperoni == "Y":
#         bill +=3
#     if extra_cheese == "Y":
#         bill += 1
#         print(f"Thank you for choosing Python Pizza Deliveries! \nYour final bill is: ${bill}.")
#     else:
#         print(f"Thank you for choosing Python Pizza Deliveries! \nYour final bill is: ${bill}.")
# elif size == "L":
#     bill +=25
#     if add_pepperoni == "Y":
#         bill +=3
#     if extra_cheese == "Y":
#         bill += 1
#         print(f"Thank you for choosing Python Pizza Deliveries! \nYour final bill is: ${bill}.")
#     else:
#         print(f"Thank you for choosing Python Pizza Deliveries! \nYour final bill is: ${bill}.")
#
#
#


#TODO - 4 - Tešā diena karuselis picas pasūtīšana

#_________________________________________________________________________________________
# You are going to write a program that tests the compatibility between two people.
# To work out the love score between two people:
# Take both people's names and check for the number of times the letters in the word TRUE occurs.
# Then check for the number of times the letters in the word LOVE occurs.
# Then combine these numbers to make a 2 digit number.
# For Love Scores less than 10 or greater than 90, the message should be:
# "Your score is *x*, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:
# "Your score is *y*, you are alright together."
# Otherwise, the message will just be their score. e.g.:
#
# "Your score is *z*."
# e.g.
# #
# name1 = "Angela Yuuuu"
# name2 = "Jack Bauer"
# name1_lovwer = name1.upper() #pārveidot par zemajiem burtiem
# name2_lovwer2 = name2.upper()
#
# #1. Take both people's names and check for the number of times the letters in the word TRUE occurs.
# #2. Then check for the number of times the letters in the word LOVE occurs.
#
# Score_first_word = 0
# T = name1_lovwer.count("T") #skaitām burtus
# R = name1_lovwer.count("R")
# U = name1_lovwer.count("U")
# E = name1_lovwer.count("E")
# Total_first_name_word = int(T+R+U+E)
# Score_first_word += Total_first_name_word
#
# L = name1_lovwer.count("L")
# O = name1_lovwer.count("O")
# V = name1_lovwer.count("V")
# E = name1_lovwer.count("E")
# Total_first_name_word2 = int(T+R+U+E)
# Score_first_word += Total_first_name_word
# print(f"First word score {Score_first_word} ")
#
# Score_second_word = 0
# T = name2_lovwer2.count("T") #skaitām burtus
# R = name2_lovwer2.count("R")
# U = name2_lovwer2.count("U")
# E = name2_lovwer2.count("E")
# Total_second_name_word1 = int(T+R+U+E)
# Score_second_word += Total_second_name_word1
#
#
# L = name2_lovwer2.count("L")
# O = name2_lovwer2.count("O")
# V = name2_lovwer2.count("V")
# E = name2_lovwer2.count("E")
# Total_second_name_word2 = int(T+R+U+E)
# Score_second_word += Total_second_name_word2
# print(f"First word score {Score_second_word} ")
#
# #3. Then combine these numbers to make a 2 digit number.
#
# Love_score = str(Score_first_word) + str(Score_second_word)
# Final_love_score = int(Love_score) #jāpārveido par int jo uzreiz to nevar
#
# # 4.Nosacījumu pievienošana
# if Final_love_score < 10 or Final_love_score > 90:
#     print(f"Your score is {Final_love_score}, you go together like coke and mentos.")
# elif Final_love_score > 40 and Final_love_score < 50:
#     print(f"Your score is {Final_love_score}, you are alright together.")
# else:
#     print(f"Your score is {Final_love_score}.")



# print(Total_second_name_word2)
# T occurs 0 times
# R occurs 1 time
# U occurs 2 times
# E occurs 2 times
#
# Total = 5
#
# L occurs 1 time
# O occurs 0 times
# V occurs 0 times
# E occurs 2 times
#
# Total = 3
# LoveScore = 53
# Print: "Your score is 53."
#
# These functions will help you:
# lower() count()
#
# Example Input 1

# Kanye West
# Kim Kardashian
# Example Output 1
# The Love Calculator is calculating your score...
# Your score is 42, you are alright together.
# Example Input 2
# Brad Pitt
# Jennifer Aniston
# Example Output 2
# The Love Calculator is calculating your score...
# Your score is 73.
#TODO - 5 - Trešā diena love calculator(count letters convert to int, change to lover or upper case, if statements, += using)


print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")