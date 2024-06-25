print("Welcome to the rollercoastrer!")
height = int(input("What is your heigt in cm? "))

if height >=120:
    print("Garāks par nepieciešamo.")
    vecums = int(input("Cik gadu"))
    if vecums >=7 :
        print("Jāmaksā ir 7$")
    else:
        print("Par brīvu, lūdzu")
else:
    print("Sorry tu esi par mazu!")
