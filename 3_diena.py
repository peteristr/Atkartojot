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

#_____________________________BMI calculator____________
# height = float(input("Lūdzu ievadi garumu metros, piem 1.65. "))
# weight = int(input("Lūdzu ievadi svaru kilogramos, piem 72. "))
#
# BMI = weight/(height ** 2)
#
# print(type(BMI))
# noapaļots = (round(BMI, 2))
# print(f"Tavs svara BMI indeks ir: {noapaļots} %")
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

print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L :  ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")



bill = 0
if size == "S":
    bill += 15
    if add_pepperoni == "Y":
        bill += 2
    if extra_cheese == "Y":
        bill += 1
        print(f"Thank you for choosing Python Pizza Deliveries! \nYour final bill is: ${bill}.")
    else:
        print(f"Thank you for choosing Python Pizza Deliveries! \nYour final bill is: ${bill}.")
elif size == "M":
    bill +=20
    if add_pepperoni == "Y":
        bill +=3
    if extra_cheese == "Y":
        bill += 1
        print(f"Thank you for choosing Python Pizza Deliveries! \nYour final bill is: ${bill}.")
    else:
        print(f"Thank you for choosing Python Pizza Deliveries! \nYour final bill is: ${bill}.")
elif size == "L":
    bill +=25
    if add_pepperoni == "Y":
        bill +=3
    if extra_cheese == "Y":
        bill += 1
        print(f"Thank you for choosing Python Pizza Deliveries! \nYour final bill is: ${bill}.")
    else:
        print(f"Thank you for choosing Python Pizza Deliveries! \nYour final bill is: ${bill}.")
