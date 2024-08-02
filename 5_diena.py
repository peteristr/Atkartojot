# names = ('Angela', 'Ben', 'Jenny', 'Michael', 'Chloe')
# for name in names:
#     print(name[-1]) #pēdējo burtu no katra vārda
#     print(name)
#     print(name + " vārds")
# print(names)

# TODO - 5 - Piektā diena Password manager (for loops) arī lietas par to kā papilidnāt list [] aizvietot, parādīt
#______________________
# stud_heigt = [180, 124, 165, 173, 189, 169, 146]
#
# #avg height
# total_height = 0
# for height in stud_heigt:
#     total_height += height
# print(total_height)
#
# num_OF_stud = 0
# for stud in stud_heigt:
#     num_OF_stud += 1 #par katru sarakstā pieksaita 1 var arī ar len fukciju
# print(num_OF_stud)
#
# avarage_heigt = round(total_height/num_OF_stud)
#
# print(f"Avarage heigt = {avarage_heigt}")
# TODO - 6 - Piektā diena avarage height  (for loops)
#______________________

#You are going to write a program that calculates the highest score from a List of scores.

# student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
#
# highest_scrore = 0 #mainīgais, lai atrastu saistību
#
# for score in student_scores:
#     if score > highest_scrore: #katram ejot cauri jābūt pābauda 0, pret visiem, tad 1 no sarkasta un ja tru, tad ir hig score un to salīdzina ar nākošo no saraksta
#
#         highest_scrore = score
# print(highest_scrore)
# TODO - 7 - Piektā diena hightest score  (for loops)
#______________________
#add 1 +2 + 3 + ... 100

# sum = 0
# for number in range (1,101): #katru ciparu šajā range, ja katru otro tad jārasta būtu (1, 101, 2)
#     sum += number
# print(sum)
#
# skaitlis = 6
# total_even = 0
# for number in range(2, skaitlis + 1, 2): #jāsāk ar pirmo pāra skaitli 2 tad katru otro
#     total_even += number
# print(total_even)
# #vai
# alternative_sum = 0
# for number in range(1, skaitlis + 1):
#     if number % 2 == 0:
#         alternative_sum += number
# print(alternative_sum)

# TODO - 8 - Piektā diena add 1 +2 + 3 + ... 100 (Range function)
#______________________

#
# ou are going to write a program that automatically prints the solution to the FizzBuzz game. These are the rules of the FizzBuzz game:
# Your program should print each number from 1 to 100 in turn and include number 100.
# When the number is divisible by 3 then instead of printing the number it should print "Fizz".
# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"
# e.g. it might start off like this:
#
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7

# game_number = 100
#
# for num in range (1, game_number + 1):
#     if num % 3 == 0 and num % 5 == 0:
#         print("FizzBUZZ")
#     elif num % 5 == 0:
#         print("Buzz")
#     elif num % 3 == 0:
#         print("Fizz")
#     else:
#         print(num)


# TODO - 9 - Piektā diena fizz buzz pāra nepāra skaitļi (Range function, % == 0)
#______________________

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


password = ""
for let in range(1, nr_letters + 1): #šis parāda cik jāizvēlās simboli
    password += random.choice(letters)
for sym in range(1, nr_symbols +1):
    password += random.choice(symbols)
for num in range(1, nr_numbers +1):
    password += random.choice(numbers)
print(password)

password_list = []
for let in range(1, nr_letters + 1): #šis parāda cik jāizvēlās simboli
    password_list += random.choice(letters)
for sym in range(1, nr_symbols +1):
    password_list += random.choice(symbols)
for num in range(1, nr_numbers +1):
    password_list += random.choice(numbers)
print(password_list)

random.shuffle(password_list)
print(password_list)
# TODO - 10 - Piektā diena password manager (Range , random, shuffle)
#______________________
