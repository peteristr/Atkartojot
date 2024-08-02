#Step 1
import random

word_list = ["aardvark", "baboon", "camel"]

#- Randomly choose a word from the word_list and assign it to a variable called chosen_word.
choosen_word = random.choice(word_list)
print(choosen_word)
# - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guesset_letter = input("Guess the letter: \n").lower()
#- Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

for letter in choosen_word:
    if letter == guesset_letter:
        print("Right")
    else:
        print("Wrong")
