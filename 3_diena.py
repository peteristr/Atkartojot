print("Welcome to the rollercoastrer!")
height = int(input("What is your heigt in cm? "))

if height >= 120: #tikai ja garums ir virs 120 cm citādi else par mazu
    print("Garāks par nepieciešamo. ") # ja garāks, tad prasa vecumu
    vecums = int(input("Cik gadi? "))
    if vecums >18 : #
        print("Jāmaksā ir 12$")
    elif vecums >=12 or vecums == 18:
        print("Jāmaksā ir 7$")
    elif vecums < 12:
        print("Tev kā bērnam jāmaksā 5$")
else:
    print("Sorry tu esi par mazu!")

# ja kāds ir zem 18 vai vienāds tad $7
# ja kāds ir virs 18 tad 12$