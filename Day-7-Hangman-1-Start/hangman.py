#Step 1 
import random

word_list = ["aardvark", "baboon", "camel"]
blanks = "" #   A placeholder for my blanks for the next steps

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
print(chosen_word)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("\n\nChoose a letter: ")
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for letter in chosen_word:
    if guess == letter:
        print(1)
    else:
        print(0)
