#Tip calculator
# garums_vardam = len(input("Kāds Tavs vārds?"))

# jaunais_garums = str(garums_vardam)
# # print(type(garums_vardam))
# print(jaunais_garums)
# print("Tavs vārds ir " + jaunais_garums + " zīmes")

# a = 123
# print(type(a))
# b = str(a) #var izmantot aŗi float(a) str(a) int(a)
# print(type(b))
#
# c = "100.5"
# print(type(c))
# d = float(c)
# print(70 + d)
# = 170.5

#_____________________________________________
# print(8/3)
# print(round(8/3))
# print(round(8/3, 3))
# print(8//3) #uzreiz ar divām // veselus dalījumus dod ;šis noderēs pie leap year 3.dienā
# print(type(8//3))

# result = 4/0.7
# result += 2
# print(result)

# score = 0
# print(score)
# score += 1
# print(score)
#_________________________________Tip Calcuslator______________
#
# print("Welcome the tip calculator!")
# bill = float(input("What was the total bill? $"))
# tip = float(input("How much tip would you like to give? 10, 12 ar 15? "))
# pers = int(input("How manu people to split the bill? "))
# # print(type(bill))
# # print(type(tip))
# amount1 = float((tip/100) * bill)
# amount2 = round((amount1 + bill)/pers, 2) #noapaļot līdz 2 zīmēm aiz komanta
# print(f"Each person should pay: ${amount2}")
#_________________________________Tip Calcuslator______________
# num1 = 6
# num2 =2
# rez = 6/2
# print(rez)

num1 = 5
num2 =2
rez = int(num1 / num2) #bez atlikuma
if rez % 2 == 0: #jā cipars dalot ar 2 bez atlikuma
    print("Pāra")
else:
    print("nepāra")

#TODO Otrā diena dip calculator, bez atlikuma aprēķini